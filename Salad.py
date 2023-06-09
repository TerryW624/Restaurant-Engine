from Food import Salad, Order
class ChickenCaesar(Salad):
    def __init__(self):
        super().__init__("Chicken Caesar Salad", 11.59, ["Chicken", "Parmesan Cheese", "Croutons", "Caesar Dressing"], "No.7")
        Order.add_ingredients(self.ingredients, self.toppings, None, None)

class Garden(Salad):
    def __init__(self):
        super().__init__("Garden Salad", 9.85, ["Tomato", "Cucumber", "Mushrooms", "Black Olives", "Carrots", "Croutons"], "No.8")
        Order.add_ingredients(self.ingredients, self.toppings, None, None)

class Italian(Salad):
    def __init__(self):
        super().__init__("Italian Salad", 12.49, ["Raddichio", "Cherry Tomatoes", "Onions", "Croutons", "Black Olives", "Pepperoncinis"], "No.9")
        Order.add_ingredients(self.ingredients, self.toppings, None, None)
