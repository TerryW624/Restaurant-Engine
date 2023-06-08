from Food import Pasta

class FettuciniAlfredo(Pasta):
    def __init__(self):
        super().__init__("Fettucini Alfredo", 16.99, pasta, sauce, meat)
        pasta = ["Fettucini"]
        sauce = ["Alfredo sauce"]
        meat = ["Chicken"]

class SpagehttiAndMeatBalls(Pasta):
    def __init__(self):
        super().__init__("Spaghetti and Meat Balls", 17.99, pasta, sauce, meat)
        pasta = ["Spaghetti"]
        sauce = ["Marinara sauce"]
        meat = ["Meat Balls"]
        
class FourCheeseRavioli(Pasta):
    def __init__(self):
        super().__init__("Four-Cheese Ravioli", 17.99, pasta, sauce, cheeses)
        pasta = ["Ravioli"]
        sauce = ["Marinara"]
        cheeses = ["Ricotta Cheese", "Cream Cheese", "Mozarella", "Provolone"]
