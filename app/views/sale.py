from flask import Blueprint, jsonify, request, make_response
from app.models.sale import Sale
from app.validation import Validate
from datetime import datetime

sale = Blueprint('sale', __name__)

sales = list()


@sale.route('/api/v1/sales', methods=['POST'])
def create_sale_record():
    """ Creates a new sale record"""
    data = request.get_json()
    validate = Validate()
    valid = validate.product_validation(data)
    try:
        if valid == "Valid":
            record_id = len(sales)
            record_id += 1
            total = int(data['unit_price']) * int(data['prod_quantity'])
            date_added = datetime.now()
            new_record = Sale(record_id, data['prod_name'],
                                    data['unit_price'],
                                    data['prod_quantity'],
                                    str(total), date_added)
            sales.append(new_record)
            return jsonify({"message": "record created successfully"}), 201
        return jsonify({"message": "Invalid fields"}), 400
    except ValueError:
        return jsonify({"message": "Invalid"})


@sale.route('/api/v1/sales', methods=['GET'])
def fetch_sale_orders():
    """This endpoint fetches all sale records"""
    Sales = [record.get_sale_dictionary() for record in sales]
    return jsonify({"All Sales": Sales}), 200


@sale.route('/api/v1/sales/<int:sale_id>', methods=['GET'])
def get_single_record(sale_id):
    single_record = []
    if sale_id != 0 and sale_id <= len(sales):
        record = sales[sale_id - 1]
        single_record.append(record.get_sale_dictionary())
        return jsonify({"Record": single_record}), 200
    return jsonify({"message": "Index out of range!"}), 400
