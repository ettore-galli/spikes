from queue import Empty, Queue
from threading import Thread

import time
from typing import Dict


def prodcons(target):
    QSIZE = 8
    WORKERS = 5

    producers_queue = Queue(QSIZE)
    consumers_queue = Queue(QSIZE)

    def producer(top: int):
        for item in range(top):
            producers_queue.put(item)
            time.sleep(0.1)

    def worker():
        while True:
            item = producers_queue.get()
            time.sleep(1)
            result = target(item)
            consumers_queue.put(result)
            producers_queue.task_done()

    thread_work: Dict[int, Thread] = {}
    for nwork in range(WORKERS):
        thread_work[nwork] = Thread(name="worker", target=worker)
        thread_work[nwork].setDaemon(True)
        thread_work[nwork].start()

    thread_prod = Thread(name="producer", target=producer, args=(30,))
    thread_prod.setDaemon(True)
    thread_prod.start()

    def consumer():
        while True:
            try:
                item = consumers_queue.get(timeout=2)
                yield item
                consumers_queue.task_done()
            except Empty:
                if producers_queue.qsize() == 0 and consumers_queue.qsize() == 0:
                    break

    return consumer


def example_target(input: float) -> float:
    return (input, float(input) ** 0.5)


if __name__ == "__main__":
    for item in prodcons(target=example_target)():
        print(f"***{item}***")
