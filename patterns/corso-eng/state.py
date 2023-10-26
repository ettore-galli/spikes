from abc import ABC, abstractmethod
from random import randint, random
from typing import List
from threading import Thread


class Avvisabile:
    @abstractmethod
    def tempo_scaduto(self):
        ...


def annuncia(nome, n_risposte):
    print(f"Sono {nome} e ho dato {n_risposte} risposte")


class Allievo(Avvisabile):
    def __init__(self, nome) -> None:
        super().__init__()
        self.nome = nome
        self.risposte = 0
        self.lavoro = None
        self.stop = False

    def tempo_scaduto(self):
        self.stop = True

    def lavora(self):
        import time

        def work():
            while True:
                if self.stop:
                    break
                time.sleep(random() / 10)
                self.risposte += 1
                # print(self.nome, self.risposte)

            annuncia(self.nome, self.risposte)

        self.lavoro = Thread(target=work)
        self.lavoro.start()


class Timer:
    def __init__(self) -> None:
        self.da_avvisare: List[Avvisabile] = []

    def add_da_avvisare(self, avv: Avvisabile):
        self.da_avvisare.append(avv)

    def avvisa_tutti(self):
        for avv in self.da_avvisare:
            avv.tempo_scaduto()

    def start(self):
        import time

        def wait_task():
            time.sleep(2)
            self.avvisa_tutti()

        Thread(target=wait_task).start()


if __name__ == "__main__":
    allievi = [Allievo("Ettore"), Allievo("Pierino"), Allievo("Luigino")]

    timer = Timer()

    for allievo in allievi:
        timer.add_da_avvisare(allievo)

    timer.start()
    for allievo in allievi:
        allievo.lavora()
