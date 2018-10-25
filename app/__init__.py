from flask import Flask, redirect
from app.views.product import product
from app.views.sale import sale
from app.views.user import user


app = Flask(__name__)

app.register_blueprint(product)
app.register_blueprint(sale)
app.register_blueprint(user)


@app.route('/')
def index():
    return redirect('/api/')