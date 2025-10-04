class Shop:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.sellers = []
        self.products = []

    def register_customer(self, name, email, password):
        from customer import Customer
        c = Customer(name, email, password)
        self.customers.append(c)
        print(f"Customer account create for {name}")
        return c

    def register_seller(self, name, email, password):
        from seller import Seller
        s = Seller(name, email, password)
        self.sellers.append(s)
        print(f"Seller account created for {name}")
        return s

    def find_product(self, product_name):
        for p in self.products:
            if p.name.lower() == product_name.lower() and p.stock > 0:
                return p
        return None

    def show_products(self):
        print("\n--- Products in Shop ---")
        for p in self.products:
            if p.stock > 0:
                print(f"{p.name} - {p.price} BDT (Stock: {p.stock})")
        print("------------------------")