from init import db, ma
from marshmallow import fields

class Rating(db.Model):
    # name of the table
    __tablename__ = "ratings"

    # attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String)
    date = db.Column(db.Date)

    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    store = db.relationship("Store", back_populates='ratings')
    user = db.relationship("User", back_populates='ratings')
    


class RatingSchema(ma.Schema):

    store = fields.Nested('StoreSchema', only=["store_name"])
    user = fields.Nested('UserSchema', only=["first_name", "email"])

    class Meta:
        fields = ("id", "score", "review", "date", "store", "user")


# handle a single user object
rating_schema = RatingSchema()

# handles a list of user objects
ratings_schema = RatingSchema(many=True)