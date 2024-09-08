from classes.product import Product

class Inventory:
    
    # Inventory constructor
    def __init__(self):
        self.products = {}
    
    # Search for product by ID and return the object
    def find_product(self, product_id): return self.products[product_id]
    
    # Displays all attributes for all products in inventory to user
    def generate_report(self):
        if len(self.products) > 0:
            print("Product Report:")
            for product_id in self.products:
                print(f"{self.find_product(product_id).product_info}")
            print("\n")
        else:
            print("Inventory empty, please add products.")
    
    # Displays all attriubutes for low stock products to user
    def generate_low_stock_report(self):
        print("Low Product Report:")
        for product_id in self.products:
            if self.find_product(product_id).get_stock_quantity() < 5:
                print(self.find_product(product_id).product_info)
        print("\n")

    # Adds products to inventory, increments stock for existing products
    def add_product(self, product):
        if product.product_id not in self.products:
            self.products[product.product_id] = product
        else:
            for product_id in self.products:
                self.find_product(product_id).add_stock(1)
    
    # Removes product from inventory
    def remove_product(self, product_id):
        if product_id in self.products:
            print(f"Removed {self.find_product(product_id).name}"
                    " from inventory.\n")
            self.products.__delitem__(product_id)
            self.generate_report()
        else:
            print(f"Product ID '{product_id}' is invalid.\n"
                  "Please select one of the following products:")
            self.generate_report()
    
    # Calculates the total inventory value
    @property
    def total_value(self) -> float:
        inventory_total = 0.00
        for product_id in self.products:
            #print(f"Product Price: {self.find_product(product_id).total_value}")
             inventory_total += self.find_product(product_id).total_value
        return inventory_total
                    
    
    
    
    