class Product:
    
    # Product constructor
    def __init__(self, product_id, name="Default", category="Default",
                 price=0.00, stock_quantity=1):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = format(price, ".2f")
        self.stock_quantity = stock_quantity
    
    # Setter methods
    def set_product_id(self, product_id): self.product_id = product_id
    def set_name(self, name): self.name = name
    def set_category(self, category): self.category = category
    def set_price(self, price): self.price = format(price, ".2f")
    
    # Getter methods
    def get_product_id(self): return self.product_id
    def get_name(self): return self.name
    def get_category(self): return self.category
    def get_price(self): return self.price
    def get_stock_quantity(self): return self.stock_quantity
    
    # Increases stock by user defined amount
    def add_stock(self, amount): 
        if amount > 0:
            self.stock_quantity += amount
            print(f"\n{self.name} stock increased from "
                  f"{self.stock_quantity - amount} to "
                  f"{self.stock_quantity}.")
        else:
            print("Please enter an additional stock quantity greater than 0.")
    
    # Decreases stock by user defined amount
    def remove_stock(self, amount): 
        if amount > 0 and (self.stock_quantity - amount) >= 0:
            self.stock_quantity -= amount
            print(f"\n{self.name} stock decreased from "
                  f"{self.stock_quantity + amount} to "
                  f"{self.stock_quantity}.")
        else:
            print(f"Stock quantity to be removed ({amount}) greater "
                  f"than current stock ({self.stock_quantity}).\n" 
                  "Please enter a lower amount.\n")
    
    # Returns a string for all attributes to user
    @property
    def product_info(self):
        return (f"Product ID: {self.get_product_id()}"
                f", Name: {self.get_name()}"
                f", Category: {self.get_category()}"
                f", Price: ${self.get_price()}"
                f", Stock: {self.get_stock_quantity()}")
        
    # Calculates and returns total product value
    @property
    def total_value(self) -> float: 
        return float(self.price) * self.stock_quantity