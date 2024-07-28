from flask import Blueprint

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.store import Store, store_schema, stores_schema


stores_bp = Blueprint("stores", __name__, url_prefix="/stores")

# GET all stores
@stores_bp.route("/")
def get_all_stores():
    stmt = db.select(Store)
    stores = db.session.scalars(stmt)
    return stores_schema.dump(stores)

# GET a single store
@stores_bp.route("/<int:store_id>")
def get_one_store(store_id):
    stmt = db.select(Store).filter_by(id=store_id)
    # stmt = db.select(store).where(store.id==store_id)
    store = db.session.scalar(stmt)
    if store:
        return store_schema.dump(store)
    else:
        return {"error": f"Store with id {store_id} not found"}, 404
    
# Create a new Store
@stores_bp.route("/", methods=["POST"])
@jwt_required()
def create_store():
    # get the data from the body of the request
    body_data = store_schema.load(request.get_json())
    # create a new Store model instance
    store = Store(
        store_name=body_data.get("store_name"),
        description=body_data.get("description"),
        supplier_id=get_jwt_identity()
    )
    # add and commit to DB
    db.session.add(store)
    db.session.commit()
    # respond
    return store_schema.dump(store)

# /stores/<id> - DELETE - delete a store
@stores_bp.route("/<int:store_id>", methods=["DELETE"])
@jwt_required()
def delete_store(store_id):
    # fetch the store from the database
    stmt = db.select(Store).filter_by(id=store_id)
    store = db.session.scalar(stmt)
    # if store
    if store:
        
        # delete the store
        db.session.delete(store)
        db.session.commit()
        return {"message": f"Store '{store.store_name}' deleted successfully"}
    # else
    else:
        # return error
        return {"error": f"Store with id {store_id} not found"}, 404
    
# /stores/<id> - PUT, PATCH - edit a store
@stores_bp.route("/<int:store_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_store(store_id):
    # get the data from the body of the request
    body_data = store_schema.load(request.get_json(), partial=True)
    # get the store from the database
    stmt = db.select(Store).filter_by(id=store_id)
    store = db.session.scalar(stmt)
    # if store exists
    if store:
        store.store_name = body_data.get("store_name") or store.store_name
        store.description = body_data.get("description") or store.description
        # commit to the DB
        db.session.commit()
        # return a response
        return store_schema.dump(store)
    # else
    else:
        # return an error
        return {"error": f"Store with id {store_id} not found"}, 404
    