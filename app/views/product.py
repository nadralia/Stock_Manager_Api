from flask import Blueprint, jsonify, request, make_response
from app.models.product import Product
from app.validation import Validate
from datetime import datetime
from flasgger import swag_from

product = Blueprint('product', __name__)

products = []

@product.route('/api/v1/products', methods=['POST'])
@swag_from('../api/v1/products/add_product.yml')
def add_product():
    """Creates a new product"""
    data = request.get_json()
    validate = Validate()
    valid = validate.product_validation(data)
    try:
        if valid == "Valid":
            prod_id = len(products)
            prod_id += 1
            date_added = datetime.now()
            new_product = Product(prod_id, data['prod_quantity'],
                                  data['prod_category'], data['unit_price'], data['prod_name'],
                                  date_added)
            products.append(new_product)
            return jsonify({"message": "Product successfully created"}), 201
        return make_response(valid)
    except ValueError:
        return jsonify({"message": "Invalid fields"}), 400


@product.route('/api/v1/products', methods=['GET'])
@swag_from('../api/v1/products/fetch_all_products.yml')
def fetch_products():
    """Fetches all the available products"""
    Products = [product.serialize() for product in products]
    return jsonify({"Products": Products}), 200


@product.route('/api/v1/products/<int:prod_id>', methods=['GET'])
@swag_from('../api/v1/products/fetch_single_product.yml')
def fetch_single_product(prod_id):
    fetched_product = []
    if prod_id != 0 and prod_id <= len(products):
        product = products[prod_id - 1]
        fetched_product.append(product.serialize())
        return jsonify({"Product": fetched_product}), 200
    return jsonify({"message": "Index out of range!"}), 400
