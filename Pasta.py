from Food import Pasta, Order

class FettuciniAlfredo(Pasta):
    def __init__(self):
        super().__init__("Fettucini Alfredo", 16.99, ["Fettucini"], ["Alfredo sauce"], ["Chicken"], "No.4")
        Order.add_ingredients(self.ingredients, self.pasta, self.meat, self.sauce)

class SpagehttiAndMeatBalls(Pasta):
    def __init__(self):
        super().__init__("Spaghetti and Meat Balls", 17.99, ["Spaghetti"], ["Marinara sauce"], ["Meat Balls"], "No.5")
        Order.add_ingredients(self.ingredients, self.pasta, self.meat, self.sauce)

class FourCheeseRavioli(Pasta):
    def __init__(self):
        super().__init__("Four-Cheese Ravioli", 17.99, ["Ravioli"], ["Marinara"], ["Ricotta Cheese", "Cream Cheese", "Mozarella", "Provolone"], "No.6")
        Order.add_ingredients(self.ingredients, self.pasta, self.meat, self.sauce)