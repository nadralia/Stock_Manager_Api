import unittest
from app import app
import json


class TestSaleViews(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client
        