from flask import Blueprint

from init import db, bcrypt
from models.user import User

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

    db.session.commit()

    print("Tables seeded")