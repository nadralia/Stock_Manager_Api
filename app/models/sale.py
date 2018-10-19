class Sale:
    def __init__(self, sale_id, prod_name, price, prod_quantity,
                 total_amount, date_added):
        self.sale_id = sale_id
        self.prod_name = prod_name
        self.price = price
        self.prod_quantity = prod_quantity
        self.total_amount = total_amount
        self.date_added = date_added

    def get_dict(self):
        dict = {
            "sale_id": self.sale_id,
            "prod_name": self.prod_name,
            "price": self.price,
            "prod_quantity": self.prod_quantity,
            "total_amount": self.total_amount,
            "date_added": self.date_added
        }
        return dict
