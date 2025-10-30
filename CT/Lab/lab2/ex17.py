class Product:
    def __init__(self, name, price, stock):
        self.name, self.price, self.stock = name, price, stock


class Order:
    def __init__(self):
        self.items = []
        self.discount = 0

    def add_product(self, product, qty):
        if qty <= product.stock:
            self.items.append((product, qty))
            product.stock -= qty
        else:
            print(f"{product.name} out of stock")

    def apply_discount(self, percent):
        self.discount = percent

    def get_total(self):
        total = sum(p.price * q for p, q in self.items)
        return total * (1 - self.discount / 100)

    def show_invoice(self):
        print("\n🧾 Bill:")
        for p, q in self.items:
            print(f"- {p.name} x{q}: {p.price * q}VND")
        print(f"Discount: {self.discount}%")
        print(f"Total: {self.get_total():,.0f}VND")

p1 = Product("Mouse", 150000, 10)
p2 = Product("Key board", 300000, 5)
p3 = Product("Screen", 2500000, 2)

order = Order()
order.add_product(p1, 2)
order.add_product(p2, 1)
order.add_product(p3, 1)
order.apply_discount(10)
order.show_invoice()
