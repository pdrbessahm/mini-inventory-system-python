class Product:
    # defining what a product is and its attributes
    def __init__ (self, product_id: int, name: str, price: float):
        self.id = product_id
        self.name = name
        self.price = price

    # defining how the product behaves when its called
    def __repr__(self):
        return f"<Product {self.id}: {self.name} - ${self.price:.2f}>"
    
