from Food import Pizza, Order

class Pepperoni(Pizza):
    def __init__(self):
        super().__init__("Pepperoni Pizza", 9.99, ["Pepperoni"], ["Cheddar"], "No.1")
        Order.add_ingredients(self.ingredients, self.toppings, self.cheese, None)

class Meatlovers(Pizza):
    def __init__(self):
        super().__init__("Meatlovers Pizza", 12.99, ["Bacon", "Sausage", "Pepperoni", "Ground Beef", "Ham"], ["Gouda"], "No.2")
        Order.add_ingredients(self.ingredients, self.toppings, self.cheese, None)

class Supreme(Pizza):
    def __init__(self):
        super().__init__("Supreme Pizza", 15.99, ["Bell Pepper", "Mushroom", "Black Olive", "Onion", "Sauasage", "Pepperoni", "Ham"], ["Swiss", "Cheddar"], "No.3")
        Order.add_ingredients(self.ingredients, self.toppings, self.cheese, None)