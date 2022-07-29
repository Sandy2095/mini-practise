#### class is blue print

class softwareEngg:

    ## class variable
    hobby = "developer"

    ## constructor
    def __init__(self,name,age,level):
        ### instance variable
        self.name = name
        self.age = age
        self.level = level

    ## instance method
    def code_lang(self,lang):
        return f'{self.name} is writing code in {lang}'

    ### dunder method, str representation
    def __str__(self):
        return f'name={self.name}, age={self.age}, level={self.level}'

    def __eq__(self,other):
        return self.name == other.name and self.age == other.age

    ### static method
    @staticmethod
    def sal_cal(age):
        if age <24:
            return 50000
        elif age >30 and age <40:
            return 100000
        return 200000

#instace or object
se1 = softwareEngg('sandy',23,'level1')
print(se1.name)
# print(softwareEngg.name) ### errro becoz name is instace variable cannt be access via class name
print(softwareEngg.hobby)
print(se1.hobby)
## Instace method called
print(se1.code_lang('Python'))
print(se1)
se2 = softwareEngg('sandy',23,'level1')
# print(se1 == se2)  ## memory location are diff so False before __eq__ implements
print(se1 == se2)

### calling static method using instance / class name
print(softwareEngg.sal_cal(23))

print(se2.sal_cal(34))
