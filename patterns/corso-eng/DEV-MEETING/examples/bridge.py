from abc import ABC, abstractmethod
from tkinter import *


class DrawAPI(ABC):
    @abstractmethod
    def draw_circle(self, x, y, radius):
        ...

    @abstractmethod
    def display(self):
        ...


class RedCircle(DrawAPI):
    def __init__(self) -> None:
        super().__init__()
        self.screen = Tk()
        self.canvas = Canvas(self.screen, width=400, height=400)
        self.screen.title = "Blue Circle"
        self.screen.geometry("400x400")

    def draw_circle(self, x, y, radius):
        self.canvas.create_oval(
            x - radius,
            y - radius,
            x + radius,
            y + radius,
            outline="#ff0000",
            fill=f"#ff32{(int(x)%256):x}",
            width=5,
        )
        self.canvas.pack(expand=True, fill="both")

    def display(self):
        self.screen.mainloop()


class TextCircle(DrawAPI):
    def __init__(self) -> None:
        super().__init__()
        self.lines = []

    def draw_circle(self, x, y, radius):
        from math import sin, pi

        rt = int(radius / 10)
        v_space = int(y / 10)
        h_space = int(x / 10)

        for _ in range(v_space):
            self.lines.append("")

        for d in range(2 * rt):
            dots = int(rt * sin((d / (2 * rt)) * pi))
            blanks = 2 * rt - dots
            line = " " * h_space + " " * blanks + "." * 2 * dots + " " * blanks
            self.lines.append(line)

    def display(self):
        for line in self.lines:
            print(line)


class Dispayer(ABC):
    @abstractmethod
    def draw(self):
        ...

    @abstractmethod
    def show(self):
        ...


class Single(Dispayer):
    def __init__(self, draw_api: DrawAPI, x, y, radius) -> None:
        super().__init__()
        self.draw_api: DrawAPI = draw_api
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.draw_api.draw_circle(self.x, self.y, self.radius)

    def show(self):
        self.draw_api.display()


class Repeated(Dispayer):
    def __init__(self, draw_api: DrawAPI, x, y, radius) -> None:
        super().__init__()
        self.draw_api: DrawAPI = draw_api
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        delta = self.radius + 1
        self.draw_api.draw_circle(self.x - delta, self.y, self.radius)
        self.draw_api.draw_circle(self.x, self.y, self.radius)
        self.draw_api.draw_circle(self.x + delta, self.y, self.radius)

    def show(self):
        self.draw_api.display()


if __name__ == "__main__":
    single_viewer = Single(RedCircle(), 200, 200, 75)
    single_viewer.draw()
    single_viewer.show()

    single_viewer_txt = Single(TextCircle(), 200, 200, 75)
    single_viewer_txt.draw()
    single_viewer_txt.show()

    repeated = Repeated(RedCircle(), 200, 200, 75)
    repeated.draw()
    repeated.show()

    repeated_text = Repeated(TextCircle(), 200, 200, 75)
    repeated_text.draw()
    repeated_text.show()
