from flask import Flask
from flask_restful import Api, Resource, reqparse

user = Flask(__name__)
api = Api(user)

users = [
    {
        "name": "Adralia Nelson",
        "username":"nadralia",
        "password":"123456",
        "phonenumber":"0779003145",
        "role":"admin",
        "age": 42,
        "occupation": "Software Engineer"
    },
    {
        "name": "Elvin",
        "username":"elvin",
        "password":"12345",
        "phonenumber":"0779003145",
        "role":"shop",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "username":"jass",
        "password":"12345@",
        "phonenumber":"0779003145",
        "role":"manager",
        "age": 22,
        "occupation": "Web Developer"
    }
]

class User(Resource):
    def get_single_user(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

    def add_user(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "username":args["username"],
            "password":args["password"],
            "phonenumber":args["phonenumber"],
            "role":args["role"],
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def edit_user(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        
        user = {
            "name": name,
            "age": args["age"],
            "username":args["username"],
            "password":args["password"],
            "phonenumber":args["phonenumber"],
            "role":args["role"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def remove_user(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200
      
api.add_resource(User, "/user/<string:name>")

user.run(debug=True)