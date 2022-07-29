#### _var, single underscore or __ underscore protected & private variable

class laptop:

    def __init__(self):
        self.__maxprice = 10000  ## private object
        self._protect_mix_price = 5000 ## protected variable

    #### gettter
    def get_max_lap_price(self):
        return f'laptop max price is {self.__maxprice}'

    ### setter
    def set_lap_price(self,price):
        self.__maxprice = price

lp = laptop()
print(lp.get_max_lap_price())
lp.__maxprice = 9000  ## this became local variable, not access from class objects, so we encapsulate
print(lp.__maxprice)

lp.set_lap_price(11000)
print(lp.get_max_lap_price())

print(lp._protect_mix_price)  ### proctected can be access outside class
# print(lp.__maxprice)  ## private cannt be acesssed outside class
