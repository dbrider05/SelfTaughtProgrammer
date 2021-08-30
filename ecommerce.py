class Customer:
    def __init__(self, name, _id):
        self.name = name
        self._id = _id

    def purchased_product(self, product, _inventory):
        inventory = _inventory.dict
        if product.name not in inventory:
            print("We will soon add the Product {}! Stay Tuned!!".format(product.name))
        else:
            if inventory[product.name] > 0:
                inventory[product.name] -= 1
                print("You purchased a {} of price Rs.{} Woe! Thanks for Shopping in this Outlet:)".format(product.name, product.price))
            else:
                inventory.pop(product.name)
                print("Lo Siento! We are Out of Stock:(")

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Inventory:

    def __init__(self):
        self.dict = {}

    def add_product(self, product, quantity):
        if product.name not in self.dict:
            self.dict[product.name] = quantity
        else:
            self.dict[product.name] += quantity

    def print_inventory(self):
        for key, value in self.dict.items():
            print(key + ":" + str(value))


bruno = Customer("bruno", "bruno@gmail.com")
Mac = Product("Mac", 100)
inventory = Inventory()
inventory.add_product(Mac, 100)
inventory.add_product(Mac, 300)
inventory.print_inventory()
bruno.purchased_product(Mac, inventory)
inventory.print_inventory()
iphone = Product("Iphone", 400)
bruno.purchased_product(iphone, inventory)