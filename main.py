from classes.product import Product
from classes.inventory import Inventory
import typer
import pytest


# Create CLI object, display help message on startup
app = typer.Typer(no_args_is_help=True)

# CLI Command Definitions
@app.command()
def add_product(product_id: int, 
                name: str,
                category: str,
                price: float,
                stock: int):
    product = Product(product_id,
                name,
                category,
                float(price),
                int(stock))
    inventory.add_product(product)
    print("\nAdded product:"
          f"{product.product_info}")

@app.command()
def add_stock(product_id: int, stock_quantity: int):
    inventory.find_product(product_id).add_stock(stock_quantity)

@app.command()
def display_product(product_id: int):
    print(inventory.find_product(product_id).product_info)

@app.command()
def generate_report(): inventory.generate_report()

@app.command()
def generate_low_stock_report(): inventory.generate_low_stock_report()

@app.command()
def remove_product(product_id: int): inventory.remove_product(product_id)

@app.command()
def remove_stock(product_id: int, stock_amount: int): 
    inventory.find_product(product_id).remove_stock(stock_amount)


if __name__ == '__main__':

    # Run unit tests for Inventory and Product classes
    pytest.main(["tests\\"]) 
    
    # Create inventory object
    inventory = Inventory()
    
    # Adding products
    inventory.add_product(Product(1,"Laptop","Electronics",1000,10))
    inventory.add_product(Product(2, "Headphones","Electronics",150.00,3))
    inventory.add_product(Product(3, "Coffee Mug","Kitchenware",10.00,20))
    
    # Removing stock
    inventory.find_product(1).remove_stock(2)
    
    # Generating reports
    inventory.generate_report()
    inventory.generate_low_stock_report()
    
    # Display total inventory value
    print(f"Total Value of Inventory: ${inventory.total_value}\n\n")
    
    # Run CLI
    app()