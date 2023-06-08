from Food import Salad
class ChickenCaesar(Salad):
    def __init__(self):
        super().__init__("Chicken Caesar Salad", 11.50, toppings)
        toppings = ["Chicken", "Parmesan Cheese", "Croutons", "Caesar Dressing"]

class Garden(Salad):
    def __init__(self):
        super().__init__("Garden Salad", 9.85, toppings)
        toppings = ["Tomato", "Cucumber", "Mushrooms", "Black Olives", "Carrots", "Croutons"]

class Italian(Salad):
    def __init__(self):
        super().__init__("Italian Salad", 12.49, toppings)
        toppings = ["Raddichio", "Cherry Tomatoes", "Onions", "Croutons", "Black Olives", "Pepperoncinis"]
