"""
Example of core style table definitions.

https://docs.sqlalchemy.org/en/20/tutorial/metadata.html
"""

from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey


database_metadata = MetaData()

phonebook_entry_type = Table(
    "phonebook_entry_type",
    database_metadata,
    Column("entry_type_id", Integer, primary_key=True),
    Column("type", String),
)

phonebook = Table(
    "phonebook_table",
    database_metadata,
    Column("entry_id", Integer, primary_key=True),
    Column("name", String),
    Column(
        "entry_type",
        ForeignKey("phonebook_entry_type.entry_type_id"),
        nullable=True,
    ),
    Column("phone", String(30)),
)
