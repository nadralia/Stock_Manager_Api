import unittest
from app.validation import Validate
from app import app


class TestValidator(unittest.TestCase):
    """ Tests Product validation """

    def setUp(self):
        """Sets up the validator class """
        self.validate = Validate()

    def test_validate_product(self):
        # Tests to ensure the correct data definition passes
        data = {
            "prod_name": "foods",
            "prod_quantity": "4",
            "unit_price": "5000",
        }
        self.assertEqual(self.validate.product_validation(data), "Valid")


    def test_empty_product_price(self):
        # Tests to ensure the function fails if price is empty
        data = {
            "prod_name": "sugar",
            "prod_quantity": "3",
            "unit_price": ""
        }
        with app.app_context():
            self.assertEqual(self.validate.product_validation(data),
                             ("Enter the unit price of the product", 400))

    def test_empty_product_quantity(self):
        # Tests the function fails if product quantity is empty
        data = {
            "prod_name": "sugar",
            "prod_quantity": "",
            "unit_price": "40000"
        }
        with app.app_context():
            self.assertEqual(self.validate.product_validation(data),
                             ("Enter the product quantity", 400))

    def test_product_name_characters(self):
        # Tests the product name doesnot accept non alphanumeric characters
        data = {
            "prod_name": "Jeans****",
            "prod_quantity": "54",
            "unit_price": "40000"
        }
        with app.app_context():
            self.assertEqual(self.validate.product_validation(data),
                             ("productname should contain alphanumerics only",
                             400))

    def test_price_value(self):
        # Tests the price accepts integers only
        data = {
            "prod_name": "Skinny Jeans",
            "prod_quantity": "54",
            "unit_price": "price"
        }
        with app.app_context():
            self.assertEqual(self.validate.product_validation(data),
                             ("Unit price should contain integers only", 400))

    def test_product_quantity_value(self):
        # Tests the product quantity only accepts integers
        data = {
            "prod_name": "cream",
            "prod_quantity": "quantity",
            "unit_price": "17000"
        }
        with app.app_context():
            self.assertEqual(self.validate.product_validation(data),
                             ("quantity should contain integers only", 400))

    def test_wrong_key_values(self):
        # Tests that the function raises an exception with wrong key value
        data = {
            "": "pens",
            "prod_quantity": "5000",
            "unit_price": "17000"
             }
        with app.app_context():
            self.assertEqual(self.validate.product_validation(data),
                             ("Invalid Key Fields"))
