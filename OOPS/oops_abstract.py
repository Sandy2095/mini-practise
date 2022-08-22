#### abstract is just declartion no defintion
### @abstract method contain will be abstract class
### we cant inistatie object for abstract class
### all th classs inherting from abstract class must also inherit method

from abc import ABC, abstractmethod

class Polygon(ABC):

    # @abstractmethod  ## comment for called
    def noofsides(self):
        print('abstractmethod noofsides')

class Triangle(Polygon):

    def noofsides(self):
        print('Triangle noofsides..!')


t = Triangle()
t.noofsides()

p = Polygon()
p.noofsides()  ### Can't instantiate abstract class Polygon with abstract methods noofsides

