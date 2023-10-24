from enum import Enum
from typing import *

from mousse import Dataclass

from .base import Annotation, CocoDataset

__all__ = ["BBox", "ODAnnotation", "ODCocoDataset", "BBoxFormat"]


class BBoxFormat(str, Enum):
    ltrb: str = "ltrb"
    ltwh: str = "ltwh"
    xywh: str = "xywh"
    xyah: str = "xyah"


class BBox(Dataclass):
    left: float
    top: float
    bottom: float
    right: float

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.bottom - self.top

    @property
    def area(self):
        return (self.right - self.left) * (self.bottom - self.top)

    def ltrb(self, dtype: Type = float):
        return dtype(self.left), dtype(self.top), dtype(self.right), dtype(self.bottom)

    def ltwh(self, dtype: Type = float):
        return dtype(self.left), dtype(self.top), dtype(self.width), dtype(self.height)

    def __hash__(self) -> int:
        return id(self)

    def __contains__(self, other: "BBox") -> bool:
        return (
            self.left <= other.left
            and self.right >= other.right
            and self.top <= other.top
            and self.bottom >= other.bottom
        )

    def __lt__(self, other: "BBox") -> bool:
        if self.left < other.left:
            return True

        if self.left == other.left:
            return self.top < other.top

        return False

    def __le__(self, other: "BBox") -> bool:
        if self.left < other.left:
            return True

        if self.left == other.left:
            return self.top <= other.top

        return False

    def __gt__(self, other: "BBox") -> bool:
        return not other <= self

    def __ge__(self, other: "BBox") -> bool:
        return not other < self

    def __eq__(self, other: "BBox") -> bool:
        return (
            self.left == other.left
            and self.right == other.right
            and self.top == other.top
            and self.bottom == other.bottom
        )

    def __and__(self, other: "BBox") -> Optional["BBox"]:
        if (
            self.left <= other.right
            or self.right <= other.left
            or self.bottom >= other.top
            or self.top <= other.bottom
        ):
            return None

        left = max(self.left, other.left)
        top = max(self.top, other.top)
        right = min(self.right, other.right)
        bottom = min(self.bottom, other.bottom)

        return BBox(left=left, top=top, right=right, bottom=bottom)


class ODAnnotation(Annotation):
    bbox: Tuple[float, float, float, float]
    area: float = 0
    score: float = 1

    def get_bbox(self, format: BBoxFormat = BBoxFormat.ltwh) -> BBox:
        if format == BBoxFormat.ltwh:
            x_min, y_min, width, height = self.bbox
            return BBox(
                left=x_min, top=y_min, right=x_min + width, bottom=y_min + height
            )

        if format == BBoxFormat.ltrb:
            left, top, right, bottom = self.bbox
            return BBox(left=left, top=top, right=right, bottom=bottom)

        if format == BBoxFormat.xywh:
            x_center, y_center, width, height = self.bbox
            return BBox(
                left=x_center - width / 2,
                top=y_center - height / 2,
                right=x_center + width / 2,
                bottom=y_center + height / 2,
            )

        if format == BBoxFormat.xyah:
            x_center, y_center, aspect_ratio, height = self.bbox
            width = aspect_ratio * height
            return BBox(
                left=x_center - width / 2,
                top=y_center - height / 2,
                right=x_center + width / 2,
                bottom=y_center + height / 2,
            )
            
        raise ValueError(format)


class ODCocoDataset(CocoDataset):
    annotations: List[ODAnnotation] = []
