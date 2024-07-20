import os
try:
    import time
except ImportError:
    os.system("pip install time")
    import time
try:
    import random
except ImportError:
    os.system("pip install random")
    import random
triedCombos=[]
ops = ["+", "*", "/", "-"]
def calculate(num1, num2, num3, num4, op1, op2, op3, parenthesis, end):
    result=0
    try:
        calc=nums[num1] + ops[op1] + nums[num2] + ops[op2] + nums[num3] + ops[op3] +nums[num4]
        if (parenthesis != 6):
            calc=calc[:parenthesis]+"("+calc[parenthesis:end]+")"+calc[end:]
        result= eval(calc)
    except ZeroDivisionError:
        #print("Can't divide by zero")
        pass
    #print(calc)
    if result == 10:
        print(calc+"  "+str(len(triedCombos)))
#4+6+8+3
def main(nums):
    while len(triedCombos)<=256:
        for op1 in range(4):
            for op2 in range(4):
                for op3 in range(4):
                    for parenthesis in range(0,8,2):
                        for end in  range(parenthesis+3, 8, 2):
                            calculate(0,1,2,3,op1,op2,op3,parenthesis,end)
        triedCombos.append([nums])
        random.shuffle(nums)
        while nums in triedCombos:
            random.shuffle(nums)
tryAgain = "y"
while tryAgain == "y":
    nums = [input("number " + str(i + 1) + ": ") for i in range(4)]
    main(nums)
    tryAgain = input("Try again? (y/n) ").lower()
    triedCombos=[]
quit()
