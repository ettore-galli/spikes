import csv
import time
import random
from dataclasses import dataclass
from enum import Enum
from queue import Queue
from threading import Thread

from typing import Any, Dict, Generator, Optional, Tuple


class ThreadDataType(Enum):
    NORMAL = "NORMAL"
    TERMINATE = "TERMINATE"


@dataclass
class ThreadData:
    payload: Optional[Any] = None
    data_type: ThreadDataType = ThreadDataType.NORMAL


def prodcons():
    QSIZE = 8
    WORKERS = 5
    DELAY_BASE = 2
    producers_queue = Queue(QSIZE)
    consumers_queue = Queue(QSIZE)

    def delayrand():
        time.sleep(DELAY_BASE * random.random())

    def producer(top: int):
        for item in read_input("input/input.csv"):
            delayrand()
            producers_queue.put(ThreadData(payload=item))
        for _ in range(WORKERS):
            producers_queue.put(ThreadData(data_type=ThreadDataType.TERMINATE))

    def worker():
        while True:
            data_item: ThreadData = producers_queue.get()
            if data_item.data_type == ThreadDataType.TERMINATE:
                consumers_queue.put(data_item)
                print("Terminate worker")
                break
            result = f"[PROCESSED: {data_item.payload}]"

            result_item = ThreadData(payload=result)
            delayrand()
            consumers_queue.put(result_item)
            producers_queue.task_done()

    def threads_are_alive(threads: Dict[int, Thread]) -> bool:
        return any(tread.is_alive() for tread in threads.values())

    def consumer(workers: Dict[int, Thread]):
        while True:
            data_item: ThreadData = consumers_queue.get()
            if data_item.data_type == ThreadDataType.TERMINATE:
                if not threads_are_alive(workers):
                    print("Terminate consumer")
                    break
                else:
                    print("Workers still running")
            result = f"[CONSUMED: {data_item.payload}]"
            print(result)
            consumers_queue.task_done()

    thread_work: Dict[int, Thread] = {}

    thread_consumer = Thread(name="consumer", target=consumer, args=(thread_work,))
    thread_consumer.daemon = False
    thread_consumer.start()

    for nwork in range(WORKERS):
        thread_work[nwork] = Thread(name="worker", target=worker)
        thread_work[nwork].daemon = False
        thread_work[nwork].start()

    thread_prod = Thread(name="producer", target=producer, args=(30,))
    thread_prod.daemon = False
    thread_prod.start()


def read_input(filename: str) -> Generator[Tuple[int, int], None, None]:
    with open(filename, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(
            csvfile,
            delimiter="|",
            quotechar='"',
        )
        for row in reader:
            yield tuple(row.values())


if __name__ == "__main__":
    prodcons()
