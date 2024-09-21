from datetime import datetime
from multi_processing.common.connection import create_session_maker
from multi_processing.repo.data_repo import DataRepo


if __name__ == "__main__":
    database_url = (
        "mysql+pymysql://root:password@localhost:3306/sandbox?charset=utf8mb4"
    )

    session_maker = create_session_maker(database=database_url)

    with session_maker() as session:
        repo: DataRepo = DataRepo(session=session)
        repo.add_data(f"add data demo {datetime.now().isoformat()}")
