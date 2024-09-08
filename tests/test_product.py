from classes.product import Product

# Unit tests for Product class
def test_product_default_constructor() -> None:
    product = Product(10)
    display_text = ("Product ID: 10"
                    ", Name: Default"
                    ", Category: Default"
                    ", Price: $0.00"
                    ", Stock: 1")
    assert product.product_info == display_text

def test_product_add_stock() -> None:
    product = Product(10, "Test", "TestCategory", 100.00, 10)
    product.add_stock(4)
    assert product.stock_quantity == 14

def test_product_add_negative_stock() -> None:
    product = Product(10, "Test", "TestCategory", 100.00, 10)
    product.add_stock(-4)
    assert product.stock_quantity == 10

def test_product_remove_stock() -> None:
    product = Product(10, "Test", "TestCategory", 100.00, 10)
    product.remove_stock(2)
    assert product.stock_quantity == 8

def test_product_remove_too_much_stock() -> None:
    product = Product(10, "Test", "TestCategory", 100.00, 10)
    product.remove_stock(11)
    assert product.stock_quantity == 10

def test_product_setters_and_getters() -> None:
    product = Product(10, "Test", "TestCategory", 100.00, 10)
    product.set_product_id(15)
    product.set_name("NewTest")
    product.set_category("NewTestCategory")
    product.set_price(200.00)
    display_text = ("Product ID: 15"
                    ", Name: NewTest"
                    ", Category: NewTestCategory"
                    ", Price: $200.00"
                    ", Stock: 10")
    assert product.product_info == display_text

def test_product_total() -> None:
    product = Product(10, "Test", "TestCategory", 100.00, 10)
    assert product.total_value == 1000.00
    
    