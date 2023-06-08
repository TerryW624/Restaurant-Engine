class Order:
    def __init__(self, dish_name, price):
        self.dish_name = dish_name
        self.price = price
        self.ingredients = []

    def add_ingredients(self, item1, item2, item3):
        if item3 is None and item2 is None:
            self.ingredients += item1
        elif item3 is None:
            self.ingredients += (item1 + item2)
            return self.ingredients
        else:
            self.ingredients += (item1 + item2 + item3)
            return self.ingredients

class Pizza(Order):
    def __init__(self, dish_name, price, toppings, cheese):
        super().__init__(dish_name, price)
        self.cheese = cheese
        self.toppings = toppings
        self.ingredients = ["Dough", "Tomato Sauce"]

class Pasta(Order):
    def __init__(self, dish_name, price, pasta, sauce, meat):
        super().__init__(dish_name, price)
        self.pasta = pasta
        self.sauce = sauce
        self.meat = meat
        self.ingredients = []

class Salad(Order):
    def __init__(self, dish_name, price, toppings):
        super().__init__(dish_name, price)
        self.toppings = toppings
        self.ingredients = ["Lettuce"]