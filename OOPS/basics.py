import csv

class Books:
    pay_rate = 0.8
    all = []
    def __init__(self,name,price:int):
        assert price >=0, "price cannot be less than Zero"
        self.name = name
        self.price = price
        Books.all.append(self)

    def applyDiscount(self):
        return self.price * self.pay_rate  ## also possblie self.discount

    @classmethod
    def initiate_csv(cls):
        with open('books.csv','r') as f:
            result = list(csv.DictReader(f))
            for book in result:
                Books(
                    name=book.get('name'),
                    price=int(book.get('price'))
                )

    def __repr__(self):
        return f"Books('{self.name}',{self.price})"

    @staticmethod
    def is_integer(num):
        if not isinstance(num,int):
            return False
        return True

# class harcopy(Books):
#     all = []
#     def __init__(self, name, price, damage=False):
#         assert price >= 0, "price cannot be less than Zero"
#
#         self.name = name
#         self.price = price
#         self.damage = damage
#
#         harcopy.all.append(self)


Books.initiate_csv()
print(Books.all)

if Books.is_integer(10):
    print("Its Integer")
