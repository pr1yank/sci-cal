from tkinter import *
import math




def click(value):
    ex = entryField.get()  # 789 ex[0:len(ex)-1]
    answer = ''

    try:

        if value == 'C':
            ex = ex[0:len(ex) - 1]  # 78
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'AC':
            entryField.delete(0, END)

        elif value == '√':
            answer = math.sqrt(eval(ex))

        elif value == 'π':
            answer = math.pi

        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(ex)*180/3.14))

        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(ex)))

        elif value == 'EXP':
            answer = math.exp(eval(ex))



        elif value == 'x\u02b8':  # 7**2
            entryField.insert(END, '**')
            return

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2
       
        elif value == 'ln':
            answer = math.log2(eval(ex))

        elif value == 'deg':
            answer = math.degrees(eval(ex))

        elif value == "rad":
            answer = math.radians(eval(ex))

        elif value == 'e':
            answer = math.e

        elif value == 'log':
            answer = math.log(eval(ex))

        elif value == 'x!':
            answer = math.factorial(eval(ex))

        elif value == chr(247):  # 7/2=3.5
            entryField.insert(END, "/")
            return

        elif value == '=':
            answer = eval(ex)
         
            try:
                value= eval(entryField.get())
            except Exception as e:
                value="Error"

        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        entryField.insert(0, answer)

    except SyntaxError:
        pass

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def mul(a, b):
    return a * b
def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def lcm(a,b):
    l=math.lcm(a,b)
    return l

def hcf(a,b):
    h=math.gcd(a,b)
    return h

operations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
            'SUBTRACTION':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
            'PRODUCT': mul, 'MULTIPLICATION': mul,'MULTIPLY': mul,
            'DIVISION': div, 'DIV': div, 'DIVIDE': div,
            'LCM':lcm , 'HCF':hcf,
            'MOD':mod ,'REMAINDER':mod , 'MODULUS':mod }


def findNumbers(t):
    l=[]
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l

root = Tk()
root.title('Scientific Calculator')
photo = PhotoImage(file = "image.png")
root.iconphoto(True,photo)
root.config(bg='black')
root.geometry('595x465')
root.minsize(595,465)
root.maxsize(595,465)


entryField = Entry(root, font=('lucida', 20, 'bold'), bg='powderblue', fg='black', bd=10,justify=RIGHT, relief=SUNKEN, width=35)
entryField.grid(row=0, column=0, columnspan=8)



button_text_list = ["C", "AC", "√", "%", "π", "x\u00B2", "e",
                    "1", "2", "3", "-", "x\u02b8", "x\u00B3", "x!",
                    "4", "5", "6", "*", "deg", "EXP", "log",  
                    "7", "8", "9", chr(247), "ln","(", ")",
                    ".", "0", "+", "=", "sinθ","cosθ","tanθ"] 
rowvalue = 1
columnvalue = 0
for i in button_text_list:

    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='black', fg='white',
                    font=('arial', 18, 'bold'), activebackground='grey', command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue += 1
    if columnvalue > 6:
        rowvalue += 1
        columnvalue = 0

root.mainloop()
