class Order:
    def __init__(self, dish_name, price, menu_number):
        self.dish_name = dish_name
        self.price = price
        self.ingredients = []
        self.menu_number = menu_number
    @staticmethod
    def add_ingredients(ingredients, item1, item2, item3):
        if item3 is None and item2 is None:
            ingredients += item1
            return ingredients
        elif item3 is None:
            ingredients += (item1 + item2)
            return ingredients
        else:
            ingredients += (item1 + item2 + item3)
            return ingredients

class Pizza(Order):
    def __init__(self, dish_name, price, toppings, cheese, menu_number):
        super().__init__(dish_name, price, menu_number)
        self.cheese = cheese
        self.toppings = toppings
        self.ingredients = ["Dough", "Tomato Sauce"]

class Pasta(Order):
    def __init__(self, dish_name, price, pasta, sauce, meat, menu_number):
        super().__init__(dish_name, price, menu_number)
        self.pasta = pasta
        self.sauce = sauce
        self.meat = meat
        self.ingredients = []

class Salad(Order):
    def __init__(self, dish_name, price, toppings, menu_number):
        super().__init__(dish_name, price, menu_number)
        self.toppings = toppings
        self.ingredients = ["Lettuce"]