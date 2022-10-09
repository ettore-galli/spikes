from typing import Dict, List, Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel


class Item(BaseModel):
    id: str
    name: str
    age: Union[int, None] = None
    address: str

    def to_csv(self):
        return f"{self.id}|{self.name}|{self.age}|{self.address}\n"


app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATAFILE = "./data.txt"
SEPARATOR = "|"


def read_item_csv(item_csv: str) -> Dict:
    parts = item_csv.strip().split(SEPARATOR)
    return Item(
        id=parts[0],
        name=parts[1],
        age=parts[2] if parts[2].isnumeric() else 0,
        address=parts[3]
    )


def get_db_items():
    with open(DATAFILE, 'r', encoding='utf-8') as data_file:
        result = list(map(read_item_csv, data_file.readlines()))
        return result


def set_item(item: Item) -> None:

    current_items: List[Item] = get_db_items()

    with open(DATAFILE, 'w', encoding='utf-8') as data_file:

        found_for_update = False

        for record in current_items:
            if record.id == item.id:
                data_file.write(item.to_csv())
                found_for_update = True
            else:
                data_file.write(record.to_csv())

        if not found_for_update:
            data_file.write(item.to_csv())


def set_items_bulk(items: List[Item]) -> None:

    current_items: List[Item] = get_db_items()

    with open(DATAFILE, 'w', encoding='utf-8') as data_file:
        for record in current_items:

            found_for_update: bool = False

            for item in items:
                if record.id == item.id:
                    data_file.write(item.to_csv())
                    found_for_update = True
                    break

            if not found_for_update:
                data_file.write(record.to_csv())

        for item in items:
            if item.id not in [record.id for record in current_items]:
                data_file.write(item.to_csv())


@app.get("/items/")
async def get_items():
    print("get_items...")
    return get_db_items()


@app.post("/items/")
async def create_item(item: Item):
    try:
        set_item(item)
        return {"success": True, "message": "OK"}
    except Exception as e:
        return {"success": False, "message": str(e)}


@app.post("/items/bulk/")
async def create_items_bulk(items: List[Item]):
    print(items)
    try:
        set_items_bulk(items)
        return {"success": True, "message": "OK"}
    except Exception as e:
        return {"success": False, "message": str(e)}
