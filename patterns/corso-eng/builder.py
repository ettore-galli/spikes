from abc import ABC, abstractmethod
from dataclasses import dataclass


class Diagram(ABC):
    def __init__(self) -> None:
        self.class_a = None
        self.class_b = None
        self.association = None

    @abstractmethod
    def add_class_a(self, class_name):
        ...

    @abstractmethod
    def add_class_b(self, class_name):
        ...

    @abstractmethod
    def add_association(self):
        ...


@dataclass
class EntityRectangle:
    name: str


@dataclass
class Arrow:
    arrow_from: EntityRectangle
    arrow_to: EntityRectangle


class TextDiagram(Diagram):
    def __init__(self) -> None:
        super().__init__()

    def add_class_a(self, class_name):
        self.class_a = class_name

    def add_class_b(self, class_name):
        self.class_b = class_name

    def add_association(self):
        self.association = [self.class_a, self.class_b]

    def __str__(self) -> str:
        return f"TEXT: {self.class_a} ==[{self.association}]=> {self.class_b}"


class GraphicDiagram(Diagram):
    def __init__(self) -> None:
        super().__init__()

    def add_class_a(self, class_name):
        self.class_a = EntityRectangle(class_name)

    def add_class_b(self, class_name):
        self.class_b = EntityRectangle(class_name)

    def add_association(self):
        self.association = Arrow(self.class_a, self.class_b)

    def __str__(self) -> str:
        return f"[{self.class_a}] -------> [{self.class_b}]"


class DiagramBuilder(ABC):
    def __init__(self) -> None:
        self.diagram = None

    @abstractmethod
    def add_class_a(self, class_name):
        ...

    @abstractmethod
    def add_class_b(self, class_name):
        ...

    @abstractmethod
    def add_association(self):
        ...

    def get_diagram(self) -> Diagram:
        return self.diagram


class BuildGraphicDiagram(DiagramBuilder):
    def __init__(self) -> None:
        super().__init__()
        self.diagram = GraphicDiagram()

    def add_class_a(self, class_name):
        self.diagram.add_class_a(class_name)

    def add_class_b(self, class_name):
        self.diagram.add_class_b(class_name)

    def add_association(self):
        self.diagram.add_association()


class BuildTextDiagram(DiagramBuilder):
    def __init__(self) -> None:
        super().__init__()
        self.diagram = TextDiagram()

    def add_class_a(self, class_name):
        self.diagram.add_class_a(class_name)

    def add_class_b(self, class_name):
        self.diagram.add_class_b(class_name)

    def add_association(self):
        self.diagram.add_association()


class DiagramBuildManager:
    def __init__(self, type) -> None:
        if type == "T":
            self.builder = BuildTextDiagram()
        if type == "G":
            self.builder = BuildGraphicDiagram()

    def build_diagram(self, class_a, class_b) -> Diagram:
        diag = self.builder.get_diagram()
        diag.add_class_a(class_a)
        diag.add_class_b(class_b)
        diag.add_association()

        return diag


if __name__ == "__main__":
    bmt = DiagramBuildManager("T")
    print(bmt.build_diagram("AAA", "BBB"))

    bmg = DiagramBuildManager("G")
    print(bmg.build_diagram("QQQ", "WWW"))
