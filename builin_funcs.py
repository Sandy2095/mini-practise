a = (3 - 4j)

print(abs(a))

alist = [0,1,2,3,4]

print(all(alist))

adict = {1:0,2:2}
print(any(adict))
print(all(adict))
print(all([]))

text = "pythön heelö".split()

print(ascii(text))

a =0b1010
print(bin(a))

class Quan:
    apple = 1
    orange = 2

    def __index__(self):
        return self.apple + self.orange

print(bin(Quan()))

print(bool(10))
print(bool({}))


text = "python is simple"

arr = bytearray(text,encoding='utf8')

print(arr)

s = 10

# print(bytearray(s,encoding='utf8'))


print(callable(s)) ## s just variable not callable


class callFoo:
    def __call__(self, *args, **kwargs):
        print("callable")

print(callable(callFoo()))


class callFoo1:
    def fic(self, *args, **kwargs):
        print("callable")
print(callable(callFoo1))


print(chr(100)) ## outupt d => 100 == d alaphet
### value error , name error(str)  range (0,1114)


str = "a=10\nprint(a)\n"
compiled = compile(str,'builin_funcs','exec')

print(exec(compiled))


## class method



