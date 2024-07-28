from init import db, ma

class User(db.Model):
    # name of the table
    __tablename__ = "users"

    # attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    contact = db.Column(db.Integer)
    is_admin = db.Column(db.Boolean, default=False)

    ratings = db.relationship("Rating", back_populates="user")

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "surname", "email", "password", "contact", "is_admin")


# handle a single user object
user_schema = UserSchema(exclude=["password"])

# handles a list f user objects
users_schema = UserSchema(many=True, exclude=["password"])