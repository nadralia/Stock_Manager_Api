from flask import request, jsonify, Blueprint, make_response
from app.models.user import Attendant
from werkzeug.security import generate_password_hash
from flasgger import swag_from
from app.validation import Validate
import datetime

user = Blueprint('user', __name__)

users = []

@user.route('/api/v1/users', methods=['POST'])
@swag_from('../api/v1/users/add_user.yml')
def register_user():
    """ registers a user"""
    data = request.get_json()
    user_validation = Validate()
    is_valid = user_validation.user_validation(data)
    for attendant in users:
        if attendant.email == data['email']:
            return "user already exists!", 400
    try:
        if is_valid == "is_valid":
            employee_id = len(users)
            employee_id += 1
            hashed_password = generate_password_hash(data['password'],method='sha256')
            user = Attendant(employee_id, data['employee_name'], data['email'],
                             data['gender'], data['user_name'],
                             hashed_password)
            users.append(user)
            return jsonify({"message":"Attendant registered successfully"}), 201
        return make_response(is_valid)
    except KeyError:
        return "Invalid key fields"
