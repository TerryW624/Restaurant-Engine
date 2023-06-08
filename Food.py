class Order:
    def __init__(self, dish_name, price):
        self.dish_name = dish_name
        self.price = price
        self.ingredients = []
        
    def add_ingredients(self, toppings, cheese):
        self.ingredients += toppings
        self.ingredients += cheese
        return self.ingredients

class Pizza(Order):
    def __init__(self, dish_name, price, toppings, cheese):
        super().__init__(dish_name, price)
        self.cheese = cheese
        self.toppings = toppings
        self.ingredients = ["Dough", "Tomato Sauce"]

class Pasta(Order):
    def __init__(self, dish_name, price):
        super().__init__(dish_name, price)
        self.ingredients = []

class Salad(Order):
    def __init__(self, dish_name, price):
        super().__init__(dish_name, price)