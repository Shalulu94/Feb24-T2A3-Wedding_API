from flask import Blueprint

from init import db, bcrypt
from models.user import User
from models.supplier import Supplier

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

    db.session.commit()

    print("Tables seeded")