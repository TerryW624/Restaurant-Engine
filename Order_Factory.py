from Pizza import *
from Pasta import *
from Salad import *

class Order_Factory:
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
        orders = [Pepperoni(), Meatlovers(), Supreme(), FettuciniAlfredo(), SpagehttiAndMeatBalls(), FourCheeseRavioli(), ChickenCaesar(), Garden(), Italian()]
        for meal in orders:
            if order == meal.name:
                print(f"You ordered the {meal.menu_number}, {meal.__name__}.")
                print(f"Your total is {meal.price}")

Order_Factory.display_menu()