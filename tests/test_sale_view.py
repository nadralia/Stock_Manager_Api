import unittest
from app import app
import json


class TestSaleViews(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client

    def test_create_a_sale(self):
        # Tests that a sale record is created
        post_data = ({
            "prod_name": "Brown shirt",
            "unit_price": "88000",
            "prod_quantity": "6"
        })
        response = self.client().post('/api/v1/sales',
                                      content_type='application/json',
                                      data=json.dumps(post_data))
        self.assertEqual(response.status_code, 201)
    
    def test_fetch_all_sales(self):
        # Tests that the end point fetches all sale records
        response = self.client().get('/api/v1/sales',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_fetch_a_single_record(self):
        # Tests that the end point successfully returns a single sale record
        response = self.client().get('/api/v1/sales/1',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_fetch_one_sale_id(self):
        # Tests that the function returns invalid for wrong indices
        response = self.client().get('/api/v1/sales/0',
                                     content_type='application/json')
        self.assertEqual(response.status_code, 400)