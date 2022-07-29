# Counter, namedtuple, OrderedDict,defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
from functools import reduce
from json import JSONEncoder

a= 'aaaaaabbbbbcccccc'
my_count = Counter(a)
print(my_count.items())
print(my_count.most_common())

###### named tuple
Point = namedtuple('Point','x,y')
pt = Point(1,-40)
print(pt)
print(pt.x)

###### Ordereddict

orderDic = OrderedDict()
orderDic[1] = 10
orderDic[2] = 20
orderDic[3] = 30
print(orderDic)

##### DefaultDict

dedic = defaultdict(int) ## int/float

dedic[1] = 10
dedic[2] = 20
print(dedic[3])


#### deque

d = deque()
d.append(10)
d.append(20)

print(d)

d.appendleft(100)
print(d)

d.extendleft([10,20])
print(d)



######## ITERTOOLS

from itertools import product,permutations, \
    combinations, combinations_with_replacement, accumulate, groupby,count,cycle,repeat
import operator

a = [1,2]
b = [4,5]

prod = product(a,b)
print(list(prod))

######### permutations

a = [1,2,3,]
perm = permutations(a)
print(list(perm))

##### combinations

a = [1,2,3,4]
comb =combinations(a,3)
print(list(comb))

###combination with replacements

a = [1,2,3,4,]
comb_wr = combinations_with_replacement(a,2)
print(list(comb_wr))

####### accumulate

a = [1,2,3,4]
acc = accumulate(a,func=operator.mul)  ### multuply
print(list(acc))

###### groupby
def smaller_than_3(x):
    return x < 3  # return True or False

a=[1,2,3,4]
grp_obj = groupby(a,key=smaller_than_3)
for key,val in grp_obj:
    print(key,list(val))

persons = [{'name':'sandy','age':10},{'name':'sandy1','age':100},
           {'name':'sandy','age':10},{'name':'sandy1','age':100}]
g_oj = groupby(persons, key=lambda x:x['age'])
for k,v in g_oj:
    print(k,list(v))

#### count

for i in count(10):
    print(i)
    if i == 20:
        break

### break
for i in repeat(1, 4):
    print(i)

####### Lambda Fucntion

lam = lambda x : x +10
print(lam(10))

twomul = lambda  x,y: x * y
print(twomul(10,10))

### map
maped = map(lambda x:x+10, [1,2,3,4])

print(list(maped))

#### filter
filt = filter(lambda x:x % 2==0,[1,2,3,4,5])

print(list(filt))

print(list(filter(lambda x:x % 2==0,[1,2,3,4,5])))

### reduce

redu = reduce(lambda x,y:x*y,[1,2,3,4])
print(redu)

######### Exceptions
### Type Error, ModulenotfoundError, nameerror, FilenotFoundError
### ValueError, IndexError, KeyError,
### raise Exception('somthing wrong'), assertError assert(x=0, 'not postivie')
## try
  #somethign
## except Exception as e:
    #eomsthign
## else:
    ##something
## finally
     ### something


#print(10+'sas') ## typeError
#import something  ## ModulenotfoundError

#print(anv) ## nameerror

# if 100>10:
#     raise Exception('error something wrong')  ### raise Exception

# x=1
# assert (x>10), 'x object issue' ## assert

# class valHighError(Exception):   ### custom defined Exception
#     pass
#
# def test_value(x):
#     if x>100:
#         raise valHighError("Value is higher")
#
# test_value(1000)

#### Logging


import logging

# logging.getLogger(__name__)
# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%m%d%Y %H:%M:%S')
# logging.debug('this is debug')  ## default warning and above print on screen
# logging.info('this is info')
# logging.error('this is error')
# logging.warning('this is warning')
# logging.critical('this is critical')

### log hadlers  streamhandler, Filehandler

logger = logging.getLogger(__name__)

# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level & format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formmater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formmater)
file_h.setFormatter(formmater)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is warning logger')
logger.error('this is error logger')

#### logging.ini or logging.conf
# import logging.config
#
# logging.config.fileConfig('logging.conf')
#
# logger = logging.getLogger('simple')
# logging.debug('this is debug msg')

### traceback logging

# import logging
#
# try:
#     val = [1,2,3,4]
#     a = val[5]
# except IndexError as e:  ## with particular error
#     logging.error(e,exc_info=True)
#
# import logging
# import traceback
# try:
#     val = [1,2,3,4]
#     a = val[5]
# except: ## without mention exception catch using traceback module
#     logging.error("error somepoint",traceback.format_exc())

# ###### Rotating File Handler
# import logging
# from logging.handlers import  RotatingFileHandler
#
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# handler = RotatingFileHandler('app.log', maxBytes=20, backupCount=5)
# logger.addHandler(handler)
#
# for _ in range(1000000):
#     logging.info('Hello..World!!')
#
# ########## TimeRotatingHandler
# import logging
# import time
# from logging.handlers import TimedRotatingFileHandler
#
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# # s, m, d, midnight
# handler = TimedRotatingFileHandler('app.log', when='s', interval=1, backupCount=5)
# logger.addHandler(handler)
#
# for _ in range(1000000):
#     logging.info('Hello..World!!')
#     time.sleep(5)


###### JSON

import json

person = {"name":"Sandy","hasChild":True,"age":20,"city":"Mysore","titles":['engineer','charistts']}

json_obj = json.dumps(person,indent=4,sort_keys=True)  ## python json object to JSON data
print(json_obj)

with open('person.json','w') as fObj:
    json.dump(person,fObj,indent=4) ## python json object to JSON data


python_obj = json.loads(json_obj)  ##JSON data to python JSON object
print(python_obj)

with open('person.json','r') as openObj:
    person = json.load(openObj)  ## from json file to python object
    print(person)

class User:
    def __init__(self, name, age, hasKey):
        self.name = name
        self.age = age
        self.hasKey = hasKey

user = User('sandy',32, True)

#### customize json encoder
def encode_user(o):
    if isinstance(o,User):
        return {'name':o.name,'age':o.age,'hasKey':o.hasKey, "className":o.__class__.__name__}
    else:
        raise TypeError('Object of type User is not JSON serializable')

userJSON = json.dumps(user, default=encode_user)  ### converts class python object to JSON string
print(userJSON)

# class UserEncoder(JSONEncoder):
#     def encode_user(self, o):
#         if isinstance(o, User):
#             return {'name': o.name, 'age': o.age, 'hasKey': o.hasKey, "className": o.__class__.__name__}
#         return JSONEncoder.default(self, o)
#
# userJSON = UserEncoder.encode(user)
# print(userJSON)

######### random numbers
import random
a = random.random() ### random 0,1 float
print(a)

a= random.uniform(1,10)  ## betwwen 1 to 10 float
print(a)

A= random.randint(1,20)  ### integer 1 to 20 includes upper bound(20)
print(A)

a = random.randrange(1,20) ### 1 to 20 without upper bound(20)
print(a)

a = random.choice(list('sandy')) ## random pick from any list
print(a)

mylist = list('sandy')
a = random.choices(mylist,k=3) ## random pick from any list max =3
print(a)

random.shuffle(mylist)  ### shuffle list
print(mylist)

print(isinstance(10,int))

import secrets

secreted = secrets.randbits(4) ### 4 - converts to bits 1111
print(secreted)

sec = secrets.choice(list('sandy'))
print(sec)

###### decorator two types 1. Class Decorator 2. Function Decorator
### Function decortaor

def smaller_case(function):
    def wrapper():
        func = function()
        strinlower=  func.lower()
        return strinlower
    return wrapper

def splitter(func):
    def wrapper():
        return func().split()
    return wrapper
@splitter
@smaller_case
def hello():
    return 'HELLO WORLD'

print(hello())


def start_end_decor(func):

    def wrapper(*args, **kwargs):
        print('this is start of decorator',args)
        name = func(args)
        print('this is end of decorator',args)
        return name
    return wrapper

@start_end_decor
def name(name):
    print("hello",name)

name('sandy')

### decorator with arguments

def repeatit(num_times):
    def deco_repeat(func):
        def wrapper(*args):
            for _ in range(num_times):
                result = func(args)
            return result
        return wrapper
    return deco_repeat

@repeatit(num_times=3)
def name(name):
    print("hello", name)

name("sannnd")


#### class decorator

class numTimes:
    def __init__(self,func):
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'this is {self.num_calls} times')

@numTimes
def hello():
    print('helo')

hello();
hello()

######### Generator

def generator():
    yield 1
    yield 3
    yield 10

g = generator()
print(g)
print(g.__next__())
print(g.__next__())

def coundown(num):
    print('Statring')
    while num > 0:
        yield num
        num -= 1
ct= coundown(2)

print(ct)
print(ct.__next__())
print(ct.__next__())

## simplest / other way to use generator

mygen = (i for i in range(100) if i%2 ==0)

print(list(mygen))

mylist = [i for i in range(100) if i%2 ==0]

print(list(mylist))

## funtion vs generator

def sum_numbers(n):
    num = 0
    nums =[]
    while num < n:
        nums.append(num)
        num +=1
    return nums

def sum_with_generator(n):
    num = 0
    while num <n:
        yield num
        num += 1

print(sum(sum_numbers(10)))
print(sum(sum_with_generator(10)))

### check memory efficient
import sys

print(sys.getsizeof(sum_numbers(1000000)))
print(sys.getsizeof(sum_with_generator(1000000)))

### fibonacci
def fibonnaci(n):
    # 0 1 1 2 3 5 8..
    a, b = 0, 1
    while a <n:
        yield a
        a, b = b, a+b

print(list(fibonnaci(100)))


### process vs thread

# process -  Instance of program(Python Interpretor, putty, firefox) , process can have multiple thread inside
# thread - entity within process

## GIL (Global Interpreter Lock)
### lock allows only one thread at time
### needed in cpython (memoty mgmt no thread safe)

### multi process
from multiprocessing import Process
import os
import time


def square_num():
    for i in range(100):
        i*i
        time.sleep(0.1)

processes=[]
print('start main')
process_count = os.cpu_count()
for _ in range(process_count):
    p = Process(target=square_num)
    processes.append(p)

#start process
for p in processes:
    p.start()

#join process
for i in processes:
    i.join()

print('end main')

### threading

from threading import Thread, Lock, current_thread
import time
#
#
# def square_num():
#     for i in range(100):
#         i*i
#         time.sleep(0.1)
#
# thread=[]
# thread_coun = 10
# print('start main')
# for _ in range(thread_coun):
#     t = Thread(target=square_num)
#     thread.append(t)
#
# #start thread
# for t in thread:
#     t.start()
#
# #join thread
# for i in thread:
#     i.join()
#
# print('end main')

### global
value = 10
print(value)
def global_check():
    global value
    value  =100
    print(value)

global_check()
print(value)

#### Lock in Threading

# db_value = 0
# def increase(lock):
#     global db_value
#     lock.acquire() ## with lock ## context manager
#     local_value = db_value
#     local_value += 1
#     time.sleep(0.1)
#     db_value = local_value
#     lock.release()
#
# if __name__ == "__main__":
#     lock = Lock
#     print('start db_val', db_value)
#     thread1 = Thread(target=increase,args=(lock,))
#     thread2 = Thread(target=increase,args=(lock,))
#
#     thread1.start()
#     thread2.start()
#
#     thread1.join()  ### wait until completes all thread
#     thread2.join()
#
#     print('end db value', db_value)
#     print('end main')

#### Queue in threading
from queue import Queue

# def worker(q, lock):  #### lock is not working yet to check
#     while True:
#         value = q.get()
#         with lock:
#             ## processing...
#             print(f'in {current_thread().name} got {value}')
#         q.task_done()
#
# q = Queue()
# lock = Lock
# num_thread = 10
# for i in range(num_thread):
#     t = Thread(target=worker, args=(q,lock))
#     t.daemon = True
#     t.start()
#
# for i in range(1,21):
#     q.put(i)
#
# q.join()
#
# print('ending queue')

#### Fucntion Arugments

## positional argument
def name(name):
    print(name)

def positi_argument(a,b,c):
    print(a,b,c)

positi_argument(1,2,3)

def key_argument(a,b,c):
    print(a,b,c)
    
key_argument(c=10,b=3,a=30)

def pos_key_argument(a,b):
    print(a,b)

pos_key_argument(1020,b=100)

def pos_key_default_argument(a,b,d=900): ## default argu must be last 
    print(a,b,d)

pos_key_argument(1020,b=100)

##variable length argument

def variable_len_argu(a,b,*args,**kwargs):
    print(a,b)
    for i in args:
        print(i)
    for key in kwargs:
        print(key,kwargs[key])

variable_len_argu(1,2,3,4,5,6,7,ten=10,tw=12)

##enforce keyword only argument

def enforce_key_arg(a,b,*,c,d): ## after * all are keyword only argument
    print(a,b,c,d)

enforce_key_arg(1,2,c=3,d=4)

def enforce_key_arg(*args, last):
    for arg in args:
        print(arg)
    print(last)

enforce_key_arg(1,2,last=3)

#### *args unpacking arguments

def unpack_argume(a,b,c):
    print(a,b,c)

mylist = [1,2,3] ## should match same with argurmnt , if given extra will be ignored
unpack_argume(*mylist)

#### **kwargs upacking arguments

def kwargs_unpack_argu(a,b,c):
    print(a,b,c)

mydict = {'a':1,'b':2,'c':3}
kwargs_unpack_argu(**mydict)

#### parameter passing in fun

###immutable objects cannot be changed inside function
def foo(x):
    x =10
var = 100
foo(var)
print(var)
### mutable objects can be changed inside fucntion

def foo(my_list):
    my_list.append(20)

my_list = [1,2,3,]
foo(my_list)
print(my_list)

##### astriek (*)

print([1,2]*10)

## unpack
numbers = [1,2,3,4,5,56,]

*begin, last = numbers ## unpacking , output in always list let it be tuple
print(begin)
print(last)

numbers = [1,2,3,4,5,56,34,56,778]

begin, *mid, sec_last,last = numbers
print(begin, *mid, sec_last,last)


### ternary operator

nums = [1,2,3,4]

nums.append(True) if 1==1 else nums.append(False)

print(nums)


##### shallow and deep copy
### shallow copy - one level copy meaning nested loops wont work
### Deep coup - copy entire level

import copy

## shallow copy
mylist= [1,2,3,4,[1,2]]
print(mylist)
cp = copy.copy(mylist) ## shallow copy
mylist[0] ='First'
mylist[-1][0] = 100
print(cp)  ## no affect to copied object
print(mylist)
print("--------")
### deep copy
mylist= [1,2,3,4,[1,2]]
print(mylist)
cp = copy.deepcopy(mylist) ## deep copy
mylist[0] ='First'
mylist[-1][0] = 100
print(cp)
print(mylist)

### context manager , manage resource manager
## "with" famous context manager

### create custom with context manager, must have enter & exit method as class
class manageFile():
    def __init__(self,filename):
        self.file = filename

    def __enter__(self):
        self.file = open(self.file,'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with manageFile('managefile.txt') as obj:
    obj.write('custom context manager....')


##### custom context manager using function

from contextlib import contextmanager

@contextmanager
def manfile(filename):
    file = open(filename,'w')
    try:
        yield file
    finally:
        file.close()

with manfile('func_context.txt') as obj:
    obj.write('custom context manager using fucntion..')


#### sort dict with value

dict_ = {'sand':1,'tim':32,'pop':23,'alai':3}
print(sorted(dict_.items(), key= lambda item: item[1]))


list_tup = [(1,2),(13,298),(1,12),(31,54),(11,23),]

listdummy = []

for j in list_tup:
    for i in list_tup:
        if j[-1] > i[-1]:
            maxSet = i
    listdummy.append(maxSet)

def tupesec(ele):
    return ele[1]

print(sorted(list_tup,key=tupesec,reverse=True))


print(listdummy)

