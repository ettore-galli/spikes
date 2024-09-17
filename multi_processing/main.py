from datetime import datetime

from multiprocessing import Queue
import multiprocessing
from time import sleep

from multi_processing.common.app_logger import make_logger
from multi_processing.common.connection import create_session_maker
from multi_processing.repo.data_repo import DataRepo


POISON_PILL: str = "*END"


def worker(database_url: str, data_q: Queue):
    session_maker = create_session_maker(database=database_url)
    with session_maker() as session:
        while True:
            data = data_q.get()
            if data == POISON_PILL:
                break
            repo: DataRepo = DataRepo(session=session)
            sleep(0.3)
            result = f"processing data: {data} {datetime.now().isoformat()}"
            # logger.info("adding data: %s", data)
            print(f"processing {data} ...")
            repo.add_data(result)


def process_main(database_url: str, log_file: str):
    data_q: Queue = Queue()
    workers = 3

    multiprocessing_context = multiprocessing.get_context("spawn")

    processes = [
        multiprocessing_context.Process(
            target=worker,
            args=(
                database_url,
                data_q,
            ),
        )
        for _ in range(workers)
    ]

    for process in processes:
        process.start()

    logger = make_logger(log_file=log_file, name=__name__)

    input_data = [f"item [{index}]" for index in range(100)]

    for item in input_data:
        data_q.put(item)

    for _ in range(workers):
        data_q.put(POISON_PILL)
    data_q.close()

    for process in processes:
        process.join()


if __name__ == "__main__":
    database_url = (
        "mysql+pymysql://root:password@localhost:3306/sandbox?charset=utf8mb4"
    )

    log_file: str = "./logs/app.log"

    process_main(database_url=database_url, log_file=log_file)
