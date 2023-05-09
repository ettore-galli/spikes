import contextlib
from queue import Empty, Queue
from threading import Thread

import time
from typing import Dict, Generator


class Executor:
    def __init__(self, target):
        self.target = target

        self.QSIZE = 8
        self.WORKERS = 5

        self.producers_queue = Queue(self.QSIZE)
        self.consumers_queue = Queue(self.QSIZE)

    def worker(self):
        while True:
            item = self.producers_queue.get()
            time.sleep(0.4)
            result = self.target(item)
            self.consumers_queue.put(result)
            self.producers_queue.task_done()

    def consumer(self):
        while True:
            try:
                item = self.consumers_queue.get()
                time.sleep(0.3)
                print("RESULT:", item)
                self.consumers_queue.task_done()
            except Exception as error:
                print("ERROR:", error)

    def setup(self):
        thread_work: Dict[int, Thread] = {}

        for nwork in range(self.WORKERS):
            thread_work[nwork] = Thread(name="worker", target=self.worker)
            thread_work[nwork].setDaemon(True)
            thread_work[nwork].start()

        thread_cons = Thread(name="consumer", target=self.consumer)
        thread_cons.setDaemon(True)
        thread_cons.start()

    def load(self, item):
        self.producers_queue.put(item)

    def barrier(self):
        self.producers_queue.join()
        self.consumers_queue.join()

    @contextlib.contextmanager
    def runner(self):
        self.setup()
        yield self
        self.barrier()


def example_target(input: float) -> float:
    return (input, float(input) ** 0.5)


if __name__ == "__main__":
    executor = Executor(example_target)

    with executor.runner() as runner:
        for x in range(10):
            executor.load(x)

    print("POST CONTEXT MANAGER")
