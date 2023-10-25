from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Tuple


class Diagram(ABC):
    def __init__(self) -> None:
        self.classes = []
        self.associations = []

    @abstractmethod
    def add_class(self, class_name):
        ...

    @abstractmethod
    def add_association(self, class_from, class_to):
        ...


@dataclass
class EntityRectangle:
    name: str


@dataclass
class Arrow:
    arrow_from: EntityRectangle
    arrow_to: EntityRectangle

    def __str__(self) -> str:
        return f"--- {self.arrow_from.name} {self.arrow_to.name} -->"


class TextDiagram(Diagram):
    def __init__(self) -> None:
        super().__init__()

    def add_class(self, class_name):
        self.classes.append(class_name)

    def add_association(self, class_from, class_to):
        self.associations.append([class_from, class_to])

    def __str__(self) -> str:
        classes = [f"\tClass: {classname.upper()}" for classname in self.classes]
        associations = [
            f"\t{association[0]} ----> {association[1]}"
            for association in self.associations
        ]
        return "\n".join(["Classes:"] + classes + ["Associations:"] + associations)


class GraphicDiagram(Diagram):
    def __init__(self) -> None:
        super().__init__()

    def add_class(self, class_name):
        self.classes.append(EntityRectangle(class_name))

    def add_association(self, class_from, class_to):
        self.associations.append(Arrow(class_from, class_to))

    def __str__(self) -> str:
        classes = [f"\t[{class_item.name.upper()}]" for class_item in self.classes]
        associations = [
            f"\t[{association.arrow_from}] ----> [{association.arrow_to}]"
            for association in self.associations
        ]
        return "\n".join(["Classes:"] + classes + ["Associations:"] + associations)


class DiagramBuilder(ABC):
    def __init__(self) -> None:
        self.diagram = None

    @abstractmethod
    def add_class(self, class_name):
        ...

    @abstractmethod
    def add_association(self, class_from, class_to):
        ...

    def get_diagram(self) -> Diagram:
        return self.diagram


class BuildGraphicDiagram(DiagramBuilder):
    def __init__(self) -> None:
        super().__init__()
        self.diagram = GraphicDiagram()

    def add_class(self, class_name):
        self.diagram.add_class(class_name)

    def add_association(self, class_from, class_to):
        self.diagram.add_association(class_from, class_to)


class BuildTextDiagram(DiagramBuilder):
    def __init__(self) -> None:
        super().__init__()
        self.diagram = TextDiagram()

    def add_class(self, class_name):
        self.diagram.add_class(class_name)

    def add_association(self, class_from, class_to):
        self.diagram.add_association(class_from, class_to)


class DiagramBuildManager:
    def __init__(self, type) -> None:
        if type == "T":
            self.builder = BuildTextDiagram()
        if type == "G":
            self.builder = BuildGraphicDiagram()

    def build_diagram(
        self, classes: List[str], associations: List[Tuple[str]]
    ) -> Diagram:
        diag = self.builder.get_diagram()
        for class_item in classes:
            diag.add_class(class_item)
        for association in associations:
            diag.add_association(*association)

        return diag


if __name__ == "__main__":
    bmt = DiagramBuildManager("T")
    print(
        bmt.build_diagram(
            classes=["AAA", "BBB", "CCC"], associations=[("AAA", "CCC"), ("BBB", "CCC")]
        )
    )

    bmg = DiagramBuildManager("G")
    print(
        bmg.build_diagram(
            classes=["Alfa", "Beta", "Gamma"],
            associations=[("Alfa", "Beta"), ("Beta", "Gamma"), ("Gamma", "Alfa")],
        )
    )
