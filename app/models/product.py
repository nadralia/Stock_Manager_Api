class Product:
    """This class defines the product sold by the store"""
    def __init__(self, prod_id, prod_quantity,prod_category, unit_price, prod_name, date_added):
        self.prod_id = prod_id
        self.prod_quantity = prod_quantity
        self.prod_category = prod_category
        self.unit_price = unit_price
        self.prod_name = prod_name
        self.date_added = date_added

    def serialize(self):
        return {
            "prod_id": self.prod_id,
            "prod_name": self.prod_name,
            "unit_price": self.unit_price,
            "prod_category": self.prod_category,
            "prod_quantity": self.prod_quantity,
            "date_added": self.date_added,
            }
