from tutorial.table_objects_core import (
    phonebook,
)


def test_phonebook_entry_type_properties():
    assert [
        foreign_key.target_fullname for foreign_key in list(phonebook.foreign_keys)
    ] == ["phonebook_entry_type.entry_type_id"]


def test_phonebook_properties():
    assert [column.name for column in phonebook.primary_key.columns] == ["entry_id"]
