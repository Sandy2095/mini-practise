### inheritance , extend, override
#### extend -> create new function name in child class
#### override -> create same function name in child class
class Employee():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def update_timesheet(self):
        return f'{self.name} updated timsheet'

class SoftwareEngg(Employee):

    def __init__(self,name, age, level):
        super().__init__(name,age)
        self.level = level

    def debug(self):
        return f'{self.name} is debugging..'

    def update_timesheet(self):
        return f'{self.name} updated in Deveplomet timsheet'
class Designer(Employee):

    def draw(self):
         return f'{self.name} is drawing..'

    def update_timesheet(self):
        return f'{self.name} updated in designing timsheet'

se1 = SoftwareEngg('sandy',30,'entry')
print(se1.name)
print(se1.update_timesheet())
print(se1.debug())
print(se1.update_timesheet())
d = Designer('siva',23)
print(d.draw())
print(d.update_timesheet())
e = Employee('palls','43')
print(e.update_timesheet())


## Polymorphism
### method, operator, object

### operator polymorphism
print(1+1) ## add two numbers
print("hello " + "world") ## adding 2 stirngs

#### function polymorpishm
len([1,3,]) ## len() is polymorphism, occurrence in different forms
     ### length of string len("str"), number of items in list len([1,2,3,]), number of keys in dict len({1:1,2:3})

### class polymorphism

class dog:

    def sound(self):
        return "bark"

    def eat(self):
        return "NonVeg"

class cat:

    def sound(self):
        return "Meow"

    def eat(self):
        return "Veg"

dg =dog()
print(dg.sound())
print(dg.eat())

ct =cat()
print(ct.sound())
print(ct.eat())

for animal in (dg,ct):  ## this is called polymorphism  becase both class can put together
    print(animal.sound())
    print(animal.sound())

## method overriding
## Redefine certain methods and attributes in child class is called method overriding


## no method overloading support in python
### same method name with difference parameter

