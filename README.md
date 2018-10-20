[![Build Status](https://travis-ci.com/nadralia/Stock_Manager_Api.svg?branch=develop)](https://travis-ci.com/nadralia/Stock_Manager_Api)
<a href="https://codeclimate.com/github/nadralia/Stock_Manager_Api/maintainability"><img src="https://api.codeclimate.com/v1/badges/4649fec978eb24a0c50e/maintainability" /></a>
# Stock_Manager_Api
 Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.
## Features 
- Admin can add a product
- Admin or store attendant can get all products
- Admin or store attendant can get a specific product.
- Store attendant can add a sale order.
- Admin can get all sale order details.

## API Endpoints
| REQUEST | ROUTE | FUNCTIONALITY |
| ------- | ----- | ------------- |
| GET | /api/v1/products | Fetches all products|
| GET | api/v1/products/&lt;product_id&gt; | Fetches a single product |
| GET | api/v1/sales | Fetches all sales records |
| GET | api/v1/sales/&lt;sales_id&gt; | Fetches a single sales record |
| POST | api/v1/products | Creates a product |
| POST | api/v1/sales | Creates a sales order |

**Getting started with the app**

**Technologies used to build the application**

* [Python 3.7](https://docs.python.org/3/)

* [Flask](http://flask.pocoo.org/)


## Installation

Create a new directory and initialize git in it. Clone this repository by running
```sh
$ git clone https://github.com/nadralia/Stock_Manager_Api/tree/develop
```
Create a virtual environment. For example, with virtualenv, create a virtual environment named venv using
```sh
$ virtualenv venv
```
Activate the virtual environment
```sh
$ cd venv/scripts/activate
```
Install the dependencies in the requirements.txt file using pip
```sh
$ pip install -r requirements.txt
```

Start the application by running
```sh
$ python run.py
```
Test your setup using [postman](www.getpostman.com) REST-client

**Running tests**
* Install pytest 
* navigate to project root then app/tests

### Link to Store Manager on Heroku
### [StoreManager](https://adralia-store-api.herokuapp.com/)
