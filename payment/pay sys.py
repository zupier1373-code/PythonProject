class Payment :
    def __init__(self , amount):
        self.amount = amount
    def pay (self):
        print("Processing payment...")

class CreditCard(Payment):
    def __init__(self , amount , card_number):
        super().__init__(amount)
        self.card_number = card_number
    def pay(self):
        print("Paying" ,self.amount ,"with credit card")

class Cash(Payment):
    def __init__(self , amount , cash_received):
        super().__init__(amount)
        self.cash_received = cash_received
    def pay(self):
        print("Recieved", self.cash_received , "cash")


p2 = Cash(500, 500)
p2.pay()