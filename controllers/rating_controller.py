from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.rating import Rating, rating_schema, ratings_schema
from models.store import Store


ratings_bp = Blueprint("ratings", __name__, url_prefix="/<int:store>/ratings")

# create ratings

@ratings_bp.route("/", methods=["POST"])
@jwt_required()
def create_rating(store_id):
    # get the rating object from the request body
    body_data = request.get_json()
    # fetch the store with that particular id - store_id
    stmt = db.select(Store).filter_by(id=store_id)
    store = db.session.scalar(stmt)
    # if store exists
    if store:
        # create an instance of the rating model
        rating = Rating(
            score=body_data.get("score"),
            review=body_data.get("review"),
            date=date.today(),
            store=store,
            user_id=get_jwt_identity()
        )
        # add and commit the session
        db.session.add(rating)
        db.session.commit()
        # return the created commit
        return rating_schema.dump(rating), 201
    # else
    else:
        # return an error like store does not exist
        return {"error": f"Store with id {store_id} not found"}, 404
