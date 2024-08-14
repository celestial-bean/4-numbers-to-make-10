import itertools

try:
    from pyscript import document
    HTMLoutput=document.querySelector(".HTMLoutput")
    website=True
except ImportError:
    website=False

def click(event):
    HTMLoutput.innerHTML=""
    nums=filter(lambda x: x.isdigit(), document.querySelector(".HTMLinput").value)
    print(event)
    main(nums)

print(f'website: {website}')
def output(value=""):
    if website:
        HTMLoutput.innerHTML+=value+"</br>"
    else:
        print(value)

answers=[]
ops = ["+", "*", "/", "-"]
def calculate(num1, num2, num3, num4, op1, op2, op3, parenthesis, end):
    result=0
    try:
        calc=num1 + ops[op1] + num2 + ops[op2] + num3 + ops[op3] +num4
        #output(parenthesis)
        if (parenthesis != 6):
            calc=calc[:parenthesis]+"("+calc[parenthesis:3+end]+")"+calc[3+end:]
        else:
            #output(calc)
            pass
        if(calc[0]=="(" and calc[-1]==")"):
            calc=calc[1:-1]
        result=eval(calc)
    except ZeroDivisionError:
        #output("Can't divide by zero")
        pass
    #output(calc)
    if result == 10 and not calc in answers:
        answers.append(calc)
        output(calc)
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
                        #output(parenthesis)
                        for end in  range(parenthesis, 7, 2):
                            #output(parenthesis)
                            calculate(*nums,op1,op2,op3,parenthesis,end)
        count=count+1
    output()
    output("Total: "+str(len(answers)))
if not website:
    tryAgain = "y"
    while tryAgain == "y":
        nums = [input("number " + str(i + 1) + ": ") for i in range(4)]
        main(nums)
        tryAgain = input("Try again? (y/n) ").lower()
    quit()
