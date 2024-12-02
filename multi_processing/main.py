from __future__ import annotations

from datetime import datetime

from multiprocessing import Queue
import multiprocessing
from time import sleep
from typing import Callable, Dict, List, Tuple

from multi_processing.common.app_logger import make_logger
from multi_processing.common.connection import create_session_maker
from multi_processing.repo.data_repo import DataRepo


POISON_PILL: str = "*END"
LOG_POISON_PILL: str = "*END"


def worker(database_url: str, data_q: Queue, logger: SharedLogger):
    session_maker = create_session_maker(database=database_url)
    with session_maker() as session:
        repo: DataRepo = DataRepo(session=session)

        while True:
            data = data_q.get()
            if data == POISON_PILL:
                break

            # sleep(0.3)
            result = f"processing data: {data} {datetime.now().isoformat()}"
            logger.info("adding data: %s", data)
            print(f"processing {data} ...")
            repo.add_data(result)


def logger_worker(log_file: str, log_q: Queue):
    logger = make_logger(log_file=log_file, name=__name__)

    log_strategy: Dict[str, Callable] = {
        SharedLogger.INFO: logger.info,
        SharedLogger.WARNING: logger.warning,
        SharedLogger.ERROR: logger.error,
        SharedLogger.EXCEPTION: logger.exception,
    }

    while True:
        data = log_q.get()

        if data == LOG_POISON_PILL:
            break

        log_type, args, kwargs = data
        log_strategy.get(log_type, logger.info)(*args, **kwargs)


class SharedWriterExecutor:
    def __init__(
        self,
        executor_queue: Queue[Tuple[str, List, Dict]],
    ) -> None:
        self.executor_queue: Queue[Tuple[str, List, Dict]] = executor_queue

    def _send_to_shared_writer(self, type: str, args: List, kwargs: Dict):
        self.executor_queue.put((type, args, kwargs))


class SharedLogger(SharedWriterExecutor):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    EXCEPTION = "exception"

    def info(self, *args, **kwargs):
        self._send_to_shared_writer(SharedLogger.INFO, args, kwargs)

    def warning(self, *args, **kwargs):
        self._send_to_shared_writer(SharedLogger.WARNING, args, kwargs)

    def error(self, *args, **kwargs):
        self._send_to_shared_writer(SharedLogger.ERROR, args, kwargs)

    def exception(self, *args, **kwargs):
        self._send_to_shared_writer(SharedLogger.EXCEPTION, args, kwargs)


def process_main(database_url: str, log_file: str):
    data_q: Queue = Queue()
    log_q: Queue = Queue()

    workers = 3

    multiprocessing_context = multiprocessing.get_context("spawn")

    log_process = multiprocessing_context.Process(
        target=logger_worker,
        args=(
            log_file,
            log_q,
        ),
    )
    log_process.start()

    processes = [
        multiprocessing_context.Process(
            target=worker,
            args=(database_url, data_q, SharedLogger(executor_queue=log_q)),
        )
        for _ in range(workers)
    ]

    for process in processes:
        process.start()

    input_data = [f"item [{index}]" for index in range(100)]

    for item in input_data:
        data_q.put(item)

    for _ in range(workers):
        data_q.put(POISON_PILL)
    data_q.close()

    for process in processes:
        process.join()

    log_q.put(LOG_POISON_PILL)


if __name__ == "__main__":
    database_url = (
        "mysql+pymysql://root:password@localhost:3306/sandbox?charset=utf8mb4"
    )

    log_file: str = "./logs/app.log"

    process_main(database_url=database_url, log_file=log_file)
