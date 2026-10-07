class Product :
    def __init__(self, name , price , stock):
        self.name = name
        self.price = price
        self.stock = stock
    def sell (self , quantity ) :
        if quantity<= self.stock :
            self.stock = self.stock - quantity
        else :
            print("not enough items to sell !")
    def restock (self, quantity) :
        self.stock = self.stock + quantity
    def show_info (self) :
        print ( "name :" , self.name )
        print ( "Price :" , self.price)
        print ("remaining amount :" , self.stock)