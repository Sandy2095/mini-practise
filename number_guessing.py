import random
import sys

largestnumber = 50
number_to_guess = random.randint(1,largestnumber)

chance = 1
print(number_to_guess)

while True:
    read_input = int(input("enter number to guess between (1 -{0}):".format(largestnumber)))
    if read_input > largestnumber:
        print("entered number is greater than {0}".format(largestnumber))
        sys.exit(0)
    else:
        if read_input == number_to_guess:
            print("Goot it... at chance {0}".format(chance))
            break
        elif read_input < number_to_guess:
            print("your number is less than random number")
        else:
            print("your number is greater than random number")
        chance += 1
