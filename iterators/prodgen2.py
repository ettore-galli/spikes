from queue import Empty, Queue
from threading import Thread

import time
from typing import Dict


class WorkerPoisonPill:
    pass


def prodcons(target):
    QSIZE = 8
    WORKERS = 5

    producers_queue = Queue(QSIZE)
    consumers_queue = Queue(QSIZE)
    thread_work: Dict[int, Thread] = {}

    def one_is_alive() -> bool:
        return any(thread.is_alive() for thread in thread_work.values())

    def producer(top: int):
        for item in range(top):
            producers_queue.put(item)
            time.sleep(0.1)

        while True:
            print("poisoning...")
            producers_queue.put(WorkerPoisonPill())

    def worker():
        while True:
            item = producers_queue.get()
            if isinstance(item, WorkerPoisonPill):
                print("poisoned...")
                break
            time.sleep(1)
            result = target(item)
            consumers_queue.put(result)
            producers_queue.task_done()

    for nwork in range(WORKERS):
        thread_work[nwork] = Thread(name="worker", target=worker)
        # *NO* thread_work[nwork].setDaemon(True)
        thread_work[nwork].start()

    thread_prod = Thread(name="producer", target=producer, args=(30,))
    thread_prod.setDaemon(True)
    thread_prod.start()

    def consumer():
        while True:
            try:
                item = consumers_queue.get(block=False)
                yield item
                consumers_queue.task_done()
            except Empty:
                # if "Ho finito"...
                if not one_is_alive():
                    break

    return consumer


def example_target(input: float) -> float:
    return (input, float(input) ** 0.5)


if __name__ == "__main__":
    for item in prodcons(target=example_target)():
        print(f"***{item}***")
