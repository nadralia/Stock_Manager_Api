from flask import jsonify, request
import re


class Validate:
    # add product validation.
    def product_validation(self, data):
        # Validates the product fields
        try:
            if data['prod_name'] == "":
                return "Product name is missing"
            if not data['prod_name']:
                return "Product name is missing"
            if len(data['prod_name']) < 4:
                return "Product name should be more than 4 characters long"
            if not re.match(r"^([a-zA-Z]+\s)*[a-zA-Z]+$", data['prod_name']):
                return "Product name must have no white spaces", 400
            if data["prod_quantity"] == "":
                return "Enter the product quantity", 400
            if not data["prod_quantity"]:
                return "Enter the product quantity", 400
            if not re.match(r"^[0-9_]*$", data['prod_quantity']):
                return "quantity should contain integers only", 400

            if data['unit_price'] == "":
                return "Enter the unit price of the product", 400
            if not re.match(r"^[0-9_]*$", data['unit_price']):
                return "Unit price should contain integers only", 400
            else:
                return "Valid"
        except KeyError:
            return "Invalid Key Fields"

    # add user validation
    def user_validation(self, data):
        # Validates user fields
        try:
            if len(data.keys()) == 0:
                return "No user added", 400
            if data['user_name'] == "":
                return "User name cannot be blank", 400
            if data['email'] == "":
                return "Email cannot be blank", 400
            if data['password'] == "":
                return "Password cannot be blank", 400
            if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", data['email']):
                return "Invalid email format", 400
            if not re.match(r"([a-zA-Z0-9])", data['user_name']):
                return "Only alphanumerics allowed in user name", 400
            if re.match(r"([0-9])", data['user_name']):
                return "user name cannot contain numbers only", 400
            if len(data['password']) < 5:
                return "Password too short", 400
            else:
                return "is_valid"
        except KeyError:
            return "Invalid"