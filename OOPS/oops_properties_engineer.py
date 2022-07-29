### @property , @property.setter , @property.deleter
#### getter, setter function name should be same when using @property

class bat:

    def __int__(self):
        self.__height = 5

    @property
    def bat_height(self):
        return f'height of bat is {self.__height}'

    @bat_height.setter
    def bat_height(self,height):
        self.__height = height

    @bat_height.deleter
    def bat_height(self):
        del self.__height

b = bat()
b.bat_height = 7
print(b.bat_height)  ### () should n't be used while calling
# del b.bat_height    ## will call delete property
print(b.bat_height)

