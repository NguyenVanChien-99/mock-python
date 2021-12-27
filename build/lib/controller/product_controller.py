from entity.product import Product
from flask_restful import Resource, reqparse
from repository.product_repository import ProductRepository
from flask import request
from flask_jwt_extended import jwt_required


class ProductDetail(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help="Name is required")
    parser.add_argument("quantity", type=str, required=True, help="quantity is required")
    parser.add_argument("desc", type=str, required=True, help="desc is required")

    @jwt_required()
    def get(self, product_id: int):
        product = ProductRepository.find_by_id(product_id)
        if product:
            return product.json(), 200
        return {"message": f"Product not found with id : {product_id}"}, 404

    @jwt_required()
    def put(self, product_id: int):
        data = ProductDetail.parser.parse_args()
        product = ProductRepository.find_by_id(product_id)
        if product is None:
            return {"message": f"Product not found with id : {product_id}"}, 404
        product.name = data.name
        product.quantity = data.quantity
        product.desc = data.desc
        saved = ProductRepository.update(product)
        return saved.json(), 200


class ProductGetAll(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help="Name is required")
    parser.add_argument("quantity", type=str, required=True, help="quantity is required")
    parser.add_argument("desc", type=str, required=True, help="desc is required")

    @jwt_required()
    def get(self):
        page_str = request.args.get("page")
        page = 1
        if page_str is not None:
            try:
                page = int(page_str)
                if page <= 0:
                    page = 1
            except:
                return {"message": "Page should be number"}, 400
        size_str = request.args.get("pageSize")
        size = 10
        if size_str is not None:
            try:
                size = int(size_str)
                if size <= 0:
                    size = 10
            except:
                return {"message": "Page size should be number"}, 400
        sort_field = request.args.get("sortField")
        sort_type = request.args.get("sortType")
        search_key = request.args.get("searchKey")
        products = []
        if search_key is None:
            products = ProductRepository.get_all(sort_field, sort_type, page, size)
        else:
            products = ProductRepository.search(search_key, sort_field, sort_type, page, size)
        return {
                   "content": list(map(lambda x: x.json(), products)),
                   "pagination": {
                       "page": page,
                       "pageSize": size,
                       "sortType": sort_type,
                       "sortField": sort_field
                   }
               }, 200

    @jwt_required()
    def post(self):
        data = ProductGetAll.parser.parse_args()
        product = Product(None, data.name, data.quantity, data.desc)
        saved = ProductRepository.save(product)
        return saved.json(), 200
