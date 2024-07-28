from init import db, ma
from marshmallow import fields

class Supplier(db.Model):
    # name of the table
    __tablename__ = "suppliers"

    # attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String, nullable=False)
    company_email = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    stores = db.relationship('Store', back_populates='supplier')

class SupplierSchema(ma.Schema):

    stores = fields.List(fields.Nested('StoreSchema', exclude=["supplier"]))

    class Meta:
        fields = ("id", "company_name", "company_email", "description", "password", "is_admin")


# handle a single Supplier object
supplier_schema = SupplierSchema(exclude=["password"])

# handles a list f Supplier objects
suppliers_schema = SupplierSchema(many=True, exclude=["password"])