import csv
from dataclasses import dataclass
from enum import Enum
from queue import Queue
from threading import Thread

import time
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

    producers_queue = Queue(QSIZE)
    consumers_queue = Queue(QSIZE)

    def producer(top: int):
        for item in read_input("input/input.csv"):
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
            consumers_queue.put(result_item)
            producers_queue.task_done()

    def consumer():
        while True:
            data_item: ThreadData = consumers_queue.get()
            if data_item.data_type == ThreadDataType.TERMINATE:
                print("Terminate consumer")
                break
            result = f"[CONSUMED: {data_item.payload}]"
            print(result)
            consumers_queue.task_done()

    thread_consumer = Thread(name="consumer", target=consumer)
    thread_consumer.daemon = False
    thread_consumer.start()

    thread_work: Dict[int, Thread] = {}

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
