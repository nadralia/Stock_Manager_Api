class Sale:
    def __init__(self, sale_id, prod_name, unit_price, prod_quantity,
                 total_amount, date_added):
        self.sale_id = sale_id
        self.prod_name = prod_name
        self.unit_price = unit_price
        self.prod_quantity = prod_quantity
        self.total_amount = total_amount
        self.date_added = date_added

    def get_sale_dictionary(self):
        return {
            "sale_id": self.sale_id,
            "prod_name": self.prod_name,
            "unit_price": self.unit_price,
            "prod_quantity": self.prod_quantity,
            "total_amount": self.total_amount,
            "date_added": self.date_added
        }
         
