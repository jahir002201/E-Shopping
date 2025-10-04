from user import User

class Seller(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.products = []

    def add_product(self, shop, name, price, stock):
        product = Product(name, price, stock, self)
        shop.products.append(product)
        self.products.append(product)
        print(f"{self.name} added {name} to shop")

class Product:
    def __init__(self, name, price, stock, seller):
        self.name = name
        self.price = price
        self.stock = stock
        self.seller = seller

    def __repr__(self):
        return f"{self.name} - {self.price} BDT (Stock: {self.stock})"