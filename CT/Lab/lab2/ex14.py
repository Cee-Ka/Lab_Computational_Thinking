import json

class JsonSerializableMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

class Product(JsonSerializableMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price

p = Product("Widget", 19.99)
print(p.to_json())