from Order_Factory import *
from Logger import *

class Franchise:
    def __init__(self, location):
        self.name = "Bucket of Peppers"
        self.location = location
        self.local_revenue = 0
        

    def place_order(self):
        Order_Factory.display_menu()
        order = input("What would you like to order? \nType the number (No.) of your order > ")
        Order_Factory.create_order(order)
        order_save = Order_Factory.menu_dictionary[order]
        self.local_revenue += order_save.price
        simple_books.log_transaction(order_save, self.location)
        
