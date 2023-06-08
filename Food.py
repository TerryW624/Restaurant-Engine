class Order:
    def __init__(self):
        self.name = None
        self.ingredients = []

class Pizza(Order):
    def __init__(self):
        super().__init__()
        self.name = "Pizza"
        self.cheese = None
        self.toppings = None
        self.ingredients = ["Dough", "Tomato Sauce", self.cheese, self.toppings]

class Pasta(Order):
    def __init__(self, sauce, pasta):
        super().__init__()
        self.sauce = sauce
        self.pasta = pasta
        self.name = "Pasta"

class Salad(Order):
    def __init__(self):
        super().__init__()
        self.name = "Salad"