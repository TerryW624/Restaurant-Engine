class Logger:
    def __init__(self):
        self.transaction_count = 0
        self.daily_sales = 0

    def log_transaction(self, order, int):
        self.transaction_count += 1
        self.daily_sales += order.price
        self.file = open("log.txt", "a")
        self.file.write(f"Transaction No: {self.transaction_count}\n")
        self.file.write(f"Store {int}: An order of {order.dish_name}\n")
        self.file.write(f"The total revenue of all Bucket of Peppers is {self.daily_sales}\n")
        self.file.close()

simple_books = Logger()