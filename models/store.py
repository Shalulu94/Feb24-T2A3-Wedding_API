from init import db, ma
from marshmallow import fields

class Store(db.Model):
    # name of the table
    __tablename__ = "stores"

    # attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    supplier_id = db.Column(db.Integer, db.ForeignKey("suppliers.id", nullable=False))

    supplier = db.relationship('Supplier', back_populates='stores')
    


class StoreSchema(ma.Schema):

    supplier = fields.Nested('SupplierSchema', only=["id", "company_name", "company_email"])

    class Meta:
        fields = ("id", "store_name", "description", "supplier")


# handle a single user object
supplier_schema = SupplierSchema(exclude=["password"])

# handles a list of user objects
suppliers_schema = SupplierSchema(many=True, exclude=["password"])