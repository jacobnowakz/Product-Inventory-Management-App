from classes.inventory import Inventory, Product

# Unit tests for Inventory class
def test_inventory_default_constructor() -> None:
    inventory = Inventory()
    assert inventory.products == {}

def test_inventory_add_product() -> None:
    inventory = Inventory()
    product = Product(10, "Test", "TestCategory", 100.00, 10)
    inventory.add_product(product)
    info = inventory.find_product(10).product_info
    assert inventory.find_product(10).product_info == product.product_info

def test_inventory_add_duplicate_product() -> None:
    inventory = Inventory()
    product = Product(10, "Test", "TestCategory", 100.00, 10)
    inventory.add_product(product)
    inventory.add_product(product)
    info = inventory.find_product(10).product_info
    assert inventory.find_product(10).stock_quantity == 11

def test_inventory_remove_product() -> None:
    inventory = Inventory()
    inventory.add_product(Product(10, "Test", "TestCategory", 100.00, 10))
    inventory.remove_product(10)
    assert inventory.products == {}

def test_empty_inventory_total() -> None:
    inventory = Inventory()
    assert inventory.total_value == 0

def test_inventory_total() -> None:
    inventory = Inventory()
    inventory.add_product(Product(10, "Test", "TestCategory", 100.00, 10))
    assert inventory.total_value == 1000.00