from __future__ import annotations
from abc import ABC, abstractmethod

from typing import Optional


class HtmlImageTag:
    def __init__(self) -> None:
        self.src = None
        self.alt = None
        self.style = None

    def render(self) -> str:
        return f"<img src=\"{self.src}\" style=\"{self.style}\", alt=\"{self.alt}\" />"


class HtmlImageTagBuildingStep(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.next = None

    def set_next(self, next: Optional[HtmlImageTagBuildingStep]):
        self.next = next

    @abstractmethod
    def perform(self, image: HtmlImageTag) -> HtmlImageTag:
        ...


class SourceStep(HtmlImageTagBuildingStep):
    def perform(self, image: HtmlImageTag) -> HtmlImageTag:
        image.src = "images/my-image.jpg"

        return self.next.perform(image)


class AltStep(HtmlImageTagBuildingStep):
    def perform(self, image: HtmlImageTag) -> HtmlImageTag:
        image.alt = "This is an image"

        return self.next.perform(image)


class StyleStep(HtmlImageTagBuildingStep):
    def perform(self, image: HtmlImageTag) -> HtmlImageTag:
        image.style = "width: 300px; height:200px"

        return self.next.perform(image)


class FinalStep(HtmlImageTagBuildingStep):
    def perform(self, image: HtmlImageTag) -> HtmlImageTag:
        return image


def build_image_tag() -> HtmlImageTag:
    source = SourceStep()
    alt = AltStep()
    style = StyleStep()
    final = FinalStep()

    source.set_next(alt)
    alt.set_next(style)
    style.set_next(final)

    return source.perform(HtmlImageTag())


if __name__ == "__main__":
    image_tag: HtmlImageTag = build_image_tag()

    print(image_tag.render())
