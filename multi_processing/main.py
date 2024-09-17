from datetime import datetime
from multi_processing.common.app_logger import make_logger
from multi_processing.common.connection import create_session_maker
from multi_processing.repo.data_repo import DataRepo


if __name__ == "__main__":
    database_url = (
        "mysql+pymysql://root:password@localhost:3306/sandbox?charset=utf8mb4"
    )

    log_file: str = "./logs/app.log"
    logger = make_logger(log_file=log_file, name=__name__)

    session_maker = create_session_maker(database=database_url)

    with session_maker() as session:
        repo: DataRepo = DataRepo(session=session)
        data = f"add data demo {datetime.now().isoformat()}"
        logger.info("adding data: %s", data)
        repo.add_data(f"add data demo {datetime.now().isoformat()}")
