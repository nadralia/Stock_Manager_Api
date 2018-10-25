from flask import Blueprint, jsonify, request, make_response
from app.models.product import Product
from app.validation import Validate
from datetime import datetime

product = Blueprint('product', __name__)

products = []

@product.route('/api/v1/products', methods=['POST'])
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
def fetch_products():
    """Fetches all the available products"""
    Products = [product.get_product_dictionary() for product in products]
    return jsonify({"Products": Products}), 200


@product.route('/api/v1/products/<int:prod_id>', methods=['GET'])
def fetch_single_product(prod_id):
    fetched_product = []
    if prod_id != 0 and prod_id <= len(products):
        product = products[prod_id - 1]
        fetched_product.append(product.get_product_dictionary())
        return jsonify({"Product": fetched_product}), 200
    return jsonify({"message": "Index out of range!"}), 400


