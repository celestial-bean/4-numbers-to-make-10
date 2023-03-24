                                                           10.py
import os
try:
    import random
except ImportError:
    os.system("pip install random")
    import random

operators = ["+", "*", "/", "-"]
triedCombos = []
numbers = [input("number " + str(i + 1) + ": ") for i in range(4)]

def calculate(first, sec, third):
    try:
        value = eval(numbers[0] + first + numbers[1] + sec + numbers[2] + third + numbers[3])
    except ZeroDivisionError:
        print("Failed to divide by zero")

    if value == 10:
        print(str(numbers[0]) + first + str(numbers[1]) + sec + str(numbers[2]) + third + str(numbers[3]))

def main():
    while len(triedCombos) != 1025:
        for i in range(4):
            for x in range(4):
                for o in range(4):
                    calculate(operators[i], operators[x], operators[o])

        random.shuffle(numbers)
        combo = "".join(str(numbers))
        while combo in triedCombos:
            random.shuffle(numbers)
            combo = "".join(str(numbers))
        triedCombos.append(combo)

tryAgain = "y"
while tryAgain == "y":
    main()
    tryAgain = input("Try again? (y/n) ").lower()
quit()
