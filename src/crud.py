from src.models import Product
from src.database import products_db

def create_product(product_id: int, name: str, price: float):
    product = Product(product_id, name, price)
    products_db.append(products_db)
    return product

def read_product():
    return products_db

def update_product(product_id: int, new_name: str, new_price: float):
    for product in products_db:
        if product.id == product_id:
            product.name = new_name
            product.price = new_price
            return product
    return None

def delete_product(product_id: int):
    global products_db
    products_db = [p for p in products_db if p.id != product_id]