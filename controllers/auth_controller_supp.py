from datetime import timedelta

from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from init import bcrypt, db
from models.supplier import Supplier, supplier_schema, SupplierSchema
# from utils import auth_as_admin_decorator

auth_supp_bp = Blueprint("auth_supp", __name__, url_prefix="/auth_supp")

@auth_supp_bp.route("/register", methods=["POST"])
def register_supplier():
    try:
        # get the data from the body of the request
        body_data = request.get_json()

        # create an instance of the User model
        supplier = Supplier(
            company_name=body_data.get("company_name"),
            company_email=body_data.get("company_email"),
            description=body_data.get("description"),
            
        )
        # extract the password from the body
        password = body_data.get("password")

        # hash the password
        if password:
            supplier.password = bcrypt.generate_password_hash(password).decode("utf-8")

        # add and commit to the DB
        db.session.add(supplier)
        db.session.commit()

        # respond back
        return supplier_schema.dump(supplier), 201
    
    # catch exceptions
    except IntegrityError as err:
        if err.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {"error": f"The column {err.orig.diag.column_name} is required"}, 409
        if err.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {"error": "Email address already in use"}, 409
        

@auth_supp_bp.route("/login", methods=["POST"])
def login_user():
    # get the data from the body of the request
    body_data = request.get_json()
    # find the user in DB with that email address
    stmt = db.select(Supplier).filter_by(company_email=body_data.get("company_email"))
    supplier = db.session.scalar(stmt)
    # if user exists and password is correct
    if supplier and bcrypt.check_password_hash(supplier.password, body_data.get("password")):
        # create jwt
        token = create_access_token(identity=str(supplier.id), expires_delta=timedelta(days=1))
        # respond back
        return {"email": supplier.email, "is_admin": supplier.is_admin, "token": token}
    
    # else
    else:
        # respond back with an error message
        return {"error": "Invalid email or password"}, 401