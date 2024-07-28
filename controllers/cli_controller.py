from flask import Blueprint

from init import db, bcrypt
from models.user import User
from models.supplier import Supplier
from models.store import Store

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command("seed")
def seed_tables():
    # create a list of User instances
    users = [
        User(
            first_name="shahrul",
            surname="nasir",
            email="admin@email.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8"),
            contact="045123789",
            is_admin=True
        ),
        User(
            first_name="User 1",
            surname="last",
            email="user1@email.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8"),
        )
    ]

    db.session.add_all(users)

    suppliers = [
        Supplier(
            company_name="Bayzie",
            company_email="bayzie@gmail.com",
            description="We sell flowers",
            password=bcrypt.generate_password_hash("1234560").decode("utf-8"),
            is_admin=True
        ),
        Supplier(
            company_name="Company1",
            company_email="copmany1@gmail.com",
            description="We sell lights",
            password=bcrypt.generate_password_hash("1234560").decode("utf-8"),
            
        )
    ]

    db.session.add_all(suppliers)

    stores = [
        Store(
            store_name="Store1",
            description="we sell food",
            supplier=suppliers[1]
        ),
        Store(
            store_name="Store2",
            description="We sell drinks",
            supplier=suppliers[0]
        ),
        Store(
            store_name="Store3",
            description="We sell snacks",
            supplier=suppliers[1]
        ),
    ]

    db.session.add_all(stores)

    db.session.commit()

    print("Tables seeded")