from Pizza import *
from Pasta import *
from Salad import *

class Order_Factory:
    menu_dictionary = {"1" : Pepperoni(),
                       "2" : Meatlovers(),
                       "3" : Supreme(),
                       "4" : FettuciniAlfredo(),
                       "5" : SpagehttiAndMeatBalls(),
                       "6" : FourCheeseRavioli(),
                       "7" : ChickenCaesar(),
                       "8" : Garden(),
                       "9" : Italian()}

    @staticmethod
    def display_menu():
        orders = [Pepperoni(), Meatlovers(), Supreme(), FettuciniAlfredo(), SpagehttiAndMeatBalls(), FourCheeseRavioli(), ChickenCaesar(), Garden(), Italian()]
        for meal in orders:
            menu_item_details = f"{meal.menu_number} {meal.dish_name} ${meal.price}"
            menu_detail_alignment = menu_item_details.center(150)
            print(menu_detail_alignment)
            menu_item_ingredients = f"This menu item includes: {meal.ingredients}\n "
            print(menu_item_ingredients.center(150))

 
    @staticmethod
    def create_order(order):
        menu_dictionary = {"1" : Pepperoni(),
                           "2" : Meatlovers(),
                           "3" : Supreme(),
                           "4" : FettuciniAlfredo(),
                           "5" : SpagehttiAndMeatBalls(),
                           "6" : FourCheeseRavioli(),
                           "7" : ChickenCaesar(),
                           "8" : Garden(),
                           "9" : Italian()}
        if order in menu_dictionary:
            comparable = int(order)
            if comparable >= 1 and comparable <= 3:
                pizza = menu_dictionary[order]
                print(f"You've selected {pizza.dish_name}!")
                print(f"You're total is {pizza.price}")
                print("Enjoy your pizza!")
            elif comparable >= 4 and comparable <= 6:
                pasta = menu_dictionary[order]
                print(f"You've selected {pasta.dish_name}!")
                print(f"You're total is {pasta.price}")
                print("Enjoy your pasta!")
            else:
                salad = menu_dictionary[order]
                print(f"You've selected {salad.dish_name}!")
                print(f"You're total is {salad.price}")
                print("Enjoy your pizza!")



