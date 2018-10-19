import unittest
from app.models.user import StoreEmployee

class TestUser(unittest.TestCase):
    def setUp(self):
        self.employee = StoreEmployee(1, "Adralia Nelson", "nadralia@gmail.com", "Male")