import random


while True:
    dice_number = random.randint(1, 6)
    print("your number is {}".format(dice_number))
    input_number = input("Please press Y to close this simulator or press enter key for roll again...")
    if input_number.upper() == "Y":
        break

