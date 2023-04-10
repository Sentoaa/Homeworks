class Product:

    product_number = 0

    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price
        Product.product_number += 1

    def __repr__(self):
        return f'{self.type}, {self.name}, {self.price}'

class ProductStore:

    def __init__(self):
        self.products = {}
        self.income = 0

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError("Unknown product")
        if product.name not in self.products:
            self.products[product.name] = {"type": product.type, "price": product.price * 1.3, "amount": amount}
        else:
            self.products[product.name]["amount"] += amount

    def set_discount(self, identifier, percent, identifier_type='name'):
        if percent > 20:
            raise ValueError("You loosing the profit")
        for product_name, product_info in self.products.items():
            if product_name == identifier:
                product_info["price"] = product_info["price"] * (100 - percent) / 100
                return
        raise ValueError('Product not found')

    def sell_product(self, product_name, amount):
        for name, product_info in self.products.items():
            if name == product_name:
                if product_info["amount"] > amount:
                    product_info["amount"] = product_info["amount"] - amount
                    self.income = product_info["price"] * amount
                else:
                    raise ValueError("Not enough product in the stock")
                return
        raise ValueError('Product not found')

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.products

    def get_product_info(self, product_name):
        for name, product_info in self.products.items():
            if name == product_name:
                return (name, product_info['amount'])
        else:
            raise ValueError("Unknown product")


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()

s.add(p, 10)
print(s.get_all_products())
s.add(p2, 300)
print(s.get_all_products())
s.set_discount('Football T-Shirt', 20)
print(s.get_all_products())
print(s.get_income())
s.sell_product('Ramen', 10)
print(s.get_income())
s.sell_product('Football T-Shirt', 5)
print(s.get_all_products())
print(s.get_income())

assert s.get_product_info('Ramen') == ('Ramen', 290)

print(s.get_product_info('Football T-Shirt'))