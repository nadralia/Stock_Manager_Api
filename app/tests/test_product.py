import unittest
from app.models.product import Product


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product(1, 5, "Men Jeans", 50000, "Slim Mom Jeans",
                               "Tue, 16 Oct 2018 18:42:38 GMT")

    def test_product_id(self):
        # Tests that the prodct_id is equal to the given id
        self.assertEqual(self.product.prod_id, 1, "product_id must be 1")
        self.product.prod_id = 4
        self.assertEqual(self.product.prod_id, 4, "product_id is now 4")

    def test_product_id_type(self):
        # Tests the datatype of the product id
        self.assertNotIsInstance(self.product.prod_id, str)
        self.assertIsInstance(self.product.prod_id, int)
    
    def test_product_quantity(self):
        # Tests that the product quantity is equal to the given quantity
        self.assertEqual(self.product.prod_quantity, 5, "Quantity should be 5")

    def test_product_quantity_type(self):
        # Tests the datatype of the product quantity
        self.assertIsInstance(self.product.prod_quantity, int)
        self.assertNotIsInstance(self.product.prod_quantity, str)
    
    def test_product_price(self):
        # Tests that the price is equal to the given product price
        self.assertEqual(self.product.unit_price, 50000, "price must be 50000")

    def test_price_datatype(self):
        # Tests the price of the product
        self.assertIsInstance(self.product.unit_price, int)
        self.assertNotIsInstance(self.product.unit_price, float)
        self.assertNotIsInstance(self.product.unit_price, str)

    def test_product_name(self):
        # Tests that the product name is equal to the given product name
        self.assertEqual(self.product.prod_name, "Slim Mom Jeans")
        self.product.product_name = "covert jeans"
        self.assertEqual(self.product.prod_name, "covert jeans",
                         "product name is now covert jeans")

    def test_date_added(self):
        # Tests that the date is equal to the given date
        self.assertEqual(self.product.date_added,
                         'Tue, 16 Oct 2018 18:42:38 GMT')

    def test_class_instance(self):
        # Tests that the defined object is an instance of the Product class
        self.assertIsInstance(self.product, Product)


   