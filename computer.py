class computer:
    def __init__(self):
     self.__max_prize=900
    def sell(self):
       print(self.max_prize)
    def max_prize(self,price):
     self.__max_price=price
c= computer()
c.sell()
c.__max_price=1000
c.sell()
c.__max_price(1000)
c.sell()