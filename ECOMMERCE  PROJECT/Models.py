class Products:

    def __init__(self):
        self.product_db = []

    def add_product(self, product_name, product_type, available_quantity, unit_price):
        self.product_db.append([product_name, product_type, available_quantity, unit_price])
        return True

    def search_product(self, product_name):
        return_product = None
        for product in self.product_db:
            if product[0] == product_name:
                return_product = product
                break
        return return_product

    def fetchall(self):
        return self.product_db
