"""Load the csv data to the test db."""
from csv import DictReader
from dateparser import parse

from schemas import TransactionCreate, UserCreate
from models import create_db, get_db
from operations import create_user, create_user_transaction


def main():
    """Main function."""
    db = next(get_db())
    with open("../test.csv", mode="r") as csv_file:
        csv_reader = DictReader(csv_file, delimiter=";")
        user = create_user(
            db, UserCreate(user_name="ikl", email="ikl@gmail.com", password="test")
        )
        for row in csv_reader:
            row["date"] = parse(row["date"])
            create_user_transaction(db, TransactionCreate(**row), user.user_id)  # type: ignore


if __name__ == "__main__":
    create_db()
    main()
