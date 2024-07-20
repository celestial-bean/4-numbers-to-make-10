GNU nano 7.2                                 10.py
import os
try:
    import time
except ImportError:
    os.system("pip install time")
    import time

ops = ["+", "*", "/", "-"]
def calculate(num1, num2, num3, num4, op1, op2, op3, parenthesis, end):
    result=0
    try:
        calc=nums[num1] + ops[op1] + nums[num2] + ops[op2] + nums[num3] + ops[op3] +nums[num4]
        if (parenthesis != 6):
            calc=calc[:parenthesis]+"("+calc[parenthesis:end]+")"+calc[end:]
        result= eval(calc)
    except ZeroDivisionError:
        print("Can't divide by zero")
    #print(calc)
    if result == 10:
        print(calc)
#4+6+8+3
def main():
    num1=0
    num2=1
    num3=2
    num4=3
    for op1 in range(4):
        for op2 in range(4):
            for op3 in range(4):
                for parenthesis in range(0,8,2):
                    for end in  range(parenthesis+3, 8, 2):
                        calculate(num1,num2,num3,num4,op1,op2,op3,parenthesis, end)
tryAgain = "y"
while tryAgain == "y":
    nums = [input("number " + str(i + 1) + ": ") for i in range(4)]
    main()
    tryAgain = input("Try again? (y/n) ").lower()
quit()
