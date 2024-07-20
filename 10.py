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
numCombos=[]
total=0
ops = ["+", "*", "/", "-"]
def calculate(num1, num2, num3, num4, op1, op2, op3, parenthesis, end):
    global total
    result=0
    if (parenthesis==0 and end==7):
        parenthesis=6
    try:
        calc=nums[num1] + ops[op1] + nums[num2] + ops[op2] + nums[num3] + ops[op3] +nums[num4]
        #print(parenthesis)
        if (parenthesis != 6):
            calc=calc[:parenthesis]+"("+calc[parenthesis:3+end]+")"+calc[3+end:]
        else:
            #print(calc)
            pass
        result=eval(calc)
    except ZeroDivisionError:
        #print("Can't divide by zero")
        pass
    #print(calc)
    if result == 10:
        total+=1
        #print(calc+"  "+str(len(numCombos)))
        print(calc)
        pass
#4+6+8+3
def main(nums):
    total=0
    while len(numCombos)<=256:
        for op1 in range(4):
            for op2 in range(4):
                for op3 in range(4):
                    for parenthesis in range(0,7,2):
                        #print(parenthesis)
                        for end in  range(parenthesis, 7, 2):
                            #print(parenthesis)
                            calculate(0,1,2,3,op1,op2,op3,parenthesis,end)
        numCombos.append([nums])
        random.shuffle(nums)
        while nums in numCombos:
            random.shuffle(nums)
tryAgain = "y"
while tryAgain == "y":
    nums = [input("number " + str(i + 1) + ": ") for i in range(4)]
    main(nums)
    print()
    print("Total: "+str(total))
    tryAgain = input("Try again? (y/n) ").lower()
    numCombos=[]
quit()
