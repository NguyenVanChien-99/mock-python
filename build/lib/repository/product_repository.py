from entity.product import Product
from database.data_source import db
from sqlalchemy import text, or_


class ProductRepository:

    @classmethod
    def save(cls, product: Product):
        product.id = None
        db.session.add(product)
        db.session.commit()
        db.session.refresh(product)
        return product

    @classmethod
    def update(cls, product: Product):
        db.session.commit()
        db.session.refresh(product)
        return product

    @classmethod
    def find_by_id(cls, _id: int):
        return db.session.query(Product).filter_by(id=_id).first()

    @classmethod
    def search(cls, key, sort_field, sort_type, page: int, page_size: int):
        print("Search")
        search_query = f"%{key}%"
        filters = db.session.query(Product).filter(
            or_(Product.name.like(search_query), Product.desc.like(search_query)))
        if sort_field is not None and str(sort_field).lower() in ["name", "id", "quantity", "desc"]:
            if sort_type is None or str(sort_type).lower() not in ["desc", "asc"]:
                sort_type = "asc"
            sort_option = text(f"{sort_field} {sort_type}")
            filters = filters.order_by(sort_option)
        products = filters.paginate(page, page_size, error_out=False).items
        return products

    @classmethod
    def get_all(cls, sort_field, sort_type, page: int, page_size: int):
        print("Get all")
        filters=db.session.query(Product)
        if sort_field is not None and str(sort_field).lower() in ["name", "id", "quantity", "desc"]:
            if sort_type is None or str(sort_type).lower() not in ["desc", "asc"]:
                sort_type = "asc"
            sort_option = text(f"{sort_field} {sort_type}")
            filters = filters.order_by(sort_option)
        products = filters.paginate(page, page_size, error_out=False).items
        return products
