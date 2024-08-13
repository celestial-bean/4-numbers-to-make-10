import os
try:
    import itertools
except ImportError:
    os.system("pip install itertools")
    import itertools
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
try:
    from pyscript import when
    from pyscript import element, document
    HTMLoutput=document.querySelector(".HTMLoutput")
    submit=element["submit"]
    website=True
except ImportError:
    website=False

def output(value):
    if website:
        HTMLoutput.textContent+=value
    else:
        print(value)

answers=[]
ops = ["+", "*", "/", "-"]
def calculate(num1, num2, num3, num4, op1, op2, op3, parenthesis, end):
    result=0
    try:
        calc=num1 + ops[op1] + num2 + ops[op2] + num3 + ops[op3] +num4
        #print(parenthesis)
        if (parenthesis != 6):
            calc=calc[:parenthesis]+"("+calc[parenthesis:3+end]+")"+calc[3+end:]
        else:
            #print(calc)
            pass
        if(calc[0]=="(" and calc[-1]==")"):
            calc=calc[1:-1]
        result=eval(calc)
    except ZeroDivisionError:
        #print("Can't divide by zero")
        pass
    #print(calc)
    if result == 10 and not calc in answers:
        answers.append(calc)
        print(calc)
        pass
#4+6+8+3
def main(nums):
    combos=list(itertools.permutations(nums))
    count=0
    global  answers
    answers=[]
    while count<len(combos):
        nums=combos[count]
        for op1 in range(4):
            for op2 in range(4):
                for op3 in range(4):
                    for parenthesis in range(0,7,2):
                        #print(parenthesis)
                        for end in  range(parenthesis, 7, 2):
                            #print(parenthesis)
                            calculate(*nums,op1,op2,op3,parenthesis,end)
        count=count+1
    
tryAgain = "y"
while tryAgain == "y":
    if website:
        nums=filter(lambda x: x.isdigit(), document.querySelector(".HTMLinput").value)
    else:
        nums = [input("number " + str(i + 1) + ": ") for i in range(4)]
    main(nums)
    print()
    print("Total: "+str(len(answers)))
    if website:
        @when("click", submit)
        def click(event):
            main()
    else:
        tryAgain = input("Try again? (y/n) ").lower()
quit()
