from tutorial.orm_models import PhoneBookEntry


def test_phonebook_entry():
    phone_book_entry = PhoneBookEntry(id=3, name="ettore", phone="123 456 789")
    assert phone_book_entry.id == 3
    assert phone_book_entry.name == "ettore"
    assert phone_book_entry.phone == "123 456 789"
