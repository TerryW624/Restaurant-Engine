from Food import Pizza

class Pepperoni(Pizza):
    def __init__(self):
        super().__init__("Pepperoni Pizza", 7.99, toppings, cheese)
        toppings = ["Pepperoni"]
        cheese = ["Cheddar"]

class Meatlovers(Pizza):
    def __init__(self):
        super().__init__("Meatlovers Pizza", 12.99, toppings, cheese)
        toppings = ["Bacon", "Sausage", "Pepperoni", "Ground Beef", "Ham"]
        cheese = ["Gouda"]

class Supreme(Pizza):
    def __init__(self):
        super().__init__("Supreme Pizza", 15.99, toppings, cheese)
        toppings = ["Bell Pepper", "Mushroom", "Black Olive", "Onion", "Sauasage", "Pepperoni", "Ham"]
        cheese = ["Swiss", "Cheddar"]
