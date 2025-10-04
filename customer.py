from user import User
class Customer(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.orders=[]

    def place_order(self,shop,product_name,quantity):
        product=shop.find_product(product_name)
        if product:
            if product.stock>=quantity:
                product.stock-=quantity
                self.orders.append((product.name,quantity))
                print(f"{self.name} bought {quantity} x {product.name}")
            else:
                print("Not enough stock!")
        else:
            print("Product not found")