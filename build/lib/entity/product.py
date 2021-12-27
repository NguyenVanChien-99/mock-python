from database.data_source import db


class Product(db.Model):
    __tablename__ = "tbl_product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    desc = db.Column(db.String(255))

    def __init__(self, _id: int, name, quantity: int, desc):
        self.name = name
        self.quantity = quantity
        self.desc = desc
        self.id = _id

    def __str__(self):
        return "Product[id={}, name={}, quantity={}, desc={}]".format(self.id, self.name, self.quantity, self.desc)

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
            "desc": self.desc
        }
