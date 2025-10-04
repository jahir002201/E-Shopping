from shop import Shop

shop = Shop("SuperZone")

s1 = shop.register_seller("Jahir", "jahir@sell.com", "1234")
s1.add_product(shop, "pc", 50000, 5)
s1.add_product(shop, "phone", 60000, 3)

c1 = shop.register_customer("kamal", "kamal@cust.com", "abcd")

shop.show_products()

c1.place_order(shop, "pc", 1)

shop.show_products()