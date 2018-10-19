from flask import Flask, redirect
from app.views.product import product
from app.views.sale import sale
from app.views.user import user
from flasgger import Swagger


app = Flask(__name__)

app.register_blueprint(product)
app.register_blueprint(sale)
app.register_blueprint(user)

# Define a swagger template
template = {
    "swagger": "2.0",
    "info": {
        "title":
        "Store Manager API",
        "description":
        " Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.",
        "version":
        "1.0.0"
    },
    "schemes": ["http", "https"]
}


# Instantiate swagger docs
swagger = Swagger(app, template=template)


@app.route('/')
def index():
    return redirect('/api/')