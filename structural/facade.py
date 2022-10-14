"""
- This design pattern is used to give face/interface for a complex application.
- User --> Facade ---> Complex Modules of the application
- Facade combines the services of all components of a system and provides an interface to the user
- Mostly used in layered structure systems where upper layer has interface for lower layers
"""


class CustomerDB(object):
    def __init__(self):
        self.customers_data = {}

    def add_customer(self, customer_id: str, phone_number: str):
        self.customers_data[customer_id] = phone_number

    def get_customer_id(self, phone_number: str) -> str:
        for customer_id, p_no in self.customers_data.items():
            if p_no == phone_number:
                return customer_id


class CashRegister(object):
    def __init__(self):
        self.cash = 0

    def add_cash(self, amount: int):
        self.cash += amount

    def remove_cash(self, amount: int):
        self.cash -= amount


class ProductsDB(object):
    def __init__(self):
        self.products = {}

    def add_quantity(self, product_id: str, quantity: int):
        if product_id in self.products:
            self.products[product_id] += quantity
        else:
            self.products[product_id] = quantity

    def remove_quantity(self, product_id: str, quantity: int):
        assert product_id in self.products, "Product id not found"
        assert self.products[product_id] > quantity, "Decrease the extra quantity"
        self.products[product_id] -= quantity


class ProcurementDB(object):
    def __init__(self):
        self.products = {}

    def add_procurement(self, product_id: str, quantity: int):
        if product_id in self.products:
            self.products[product_id] += quantity
        else:
            self.products[product_id] = quantity


class LoyaltyDB(object):
    def __init__(self):
        self.customers_data = {}
        self.loyalty_value = 2

    def add_customer(self, customer_id: str):
        assert customer_id not in self.customers_data,  "Customer already exists"
        self.customers_data[customer_id] = 0

    def update_loyalty(self, customer_id: str, price_paid: int):
        assert customer_id in self.customers_data, "Customer id not found"
        loyalty = price_paid / self.loyalty_value
        self.customers_data[customer_id] = loyalty


# FACADE
class POS(object):
    def __init__(self):
        self.customer_db = CustomerDB()
        self.cash_db = CashRegister()
        self.products_db = ProductsDB()
        self.procurement_db = ProcurementDB()
        self.loyalty_db = LoyaltyDB()

        self.products_db.add_quantity(product_id="P345", quantity=10)
        self.customer_db.add_customer(customer_id="C78", phone_number="+923336664142")
        self.loyalty_db.add_customer(customer_id="C78")

    def transaction(self, phone_number: str, product_id: str, quantity: int, price_paid: int):
        try:
            customer_id = self.customer_db.get_customer_id(phone_number=phone_number)
            self.products_db.remove_quantity(product_id=product_id, quantity=quantity)
            self.loyalty_db.update_loyalty(customer_id=customer_id, price_paid=price_paid)
            self.cash_db.add_cash(amount=price_paid)
            print("Transaction successful")
        except Exception as err:
            print(f"Error in transaction: {err}")


if __name__ == '__main__':
    pos = POS()
    pos.transaction(phone_number="+923336664142", product_id="P345", quantity=5, price_paid=1000)
