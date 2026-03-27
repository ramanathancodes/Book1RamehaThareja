'''
----------------------------------------------------------------------------------------------------------------------------------------------------
Chapter 5 by Rahema Thareja

Why we Need Funtions ?

1. *Modularity*: Think of large code spanning 10000 lines of scipt , Funtions make them modular (consisting of separate parts that, when combined, form a complete whole). so if they are made modular , creation and maintanence are a) easy b) can be divided and owned by multiple ppl. so functions make code convienient to write,understand and maintain.

2. *Code reusability* : Funtions by definition is a block of reusable code , so abstract repeating code and put it as fucntion , so can be resuable. Resuability cant be emphasised more by DRY and WET principles . good Quality code follows D.R.Y (Dont repeat yourself) and bad quality folows W.E.T (we enjoy typing) 

Examples include input(), print() and int() are functions which does specific job without revelaing entire code behind the task , so making it convienient.

Terminologies :

1. Calling Function: the function a which calls another function b. after b exected control returns back to a.
2. Called Fumction: in above example b is called function , a is calling function 
3. Arguments/ Parameters : The inputs function take 
4. Funtion definition : Consists of function header and  Body of function 

def function_name(args):     <========= Funtion header 

    Documentation string     -|
    statement block           | ------->  Funtion body 
    return [expression]      -|  
----------------------------------------------------------------------------------------------------------------------------------------------------

'''
###############################################

print(f"Program5.2 #Write a simple , empty arg funtion that displays string repeatedly")

def repeatStr():
    for i in range(4):
        print("Hello , world")
        
repeatStr()

###############################################

print(f"Program5.1 Program the two variables for function that substract two numbers")

def subtr(x,y):
    print(f"Result is {x-y}")
    
subtr(6,4)
###############################################

'''
In General , Arguments passed to the Function should match the order and number . 
demonstrate that.
'''
###############################################

print(f"Example5.3 Demonstrate mismatch between function paramaters & arguments. Pass less arguments and more arguments")
import traceback
def display(colour1,colour2):
    pass
try:
    display('green')
except TypeError:
    traceback.print_exc()
try:
    display('green','yellow')
except TypeError:
    traceback.print_exc()
try:
    display('green','yellow','red')
except TypeError:
    traceback.print_exc()
###############################################
   
'''
Parameters take different variable names as args & expressions
''' 
###############################################


print(f"Example 5.7 Pass expressions to functions")

def yearlySalary(salary):
    print(f"Your yearly salary is {salary}")

yearlySalary(1000+1000+1000+1000+1000+1000+1000+1000+1000+2*200)   

###############################################


'''
Variable scopes in python 

*Global Variables* : They have global scope and can be accessed from anywhere in full program 
use "global" statement inside Funtion turn local var to global var 

*Local Variables* :  Theyhave local scope and can be accessible only inside the function 

You cannot make variable in funtion header as global. syntax error raised to address local & global conflict

Variables in for or while , They dont have scope themselves and often inherit where they exists. 
if they exist in main program , loop variables persist after loop throughout main program.
But if they are inside funtion , they will act within scope of fucntion 
'''
###############################################

print(f"Example5.9 Write a program for num1 in global scope , num2 & num3 in local scope. access all in main program")
import traceback
num1 = 10 
def func(num2):
    num3 = 30
    print(f"Inside func, num1 is {num1}")
    print(f"Inside func, num2 is {num2}")
    print(f"Inside func, num3 is {num3}")
    
func(20)

print(f"outside func, num1 is {num1}")
try:
    print(f"outside func, num2 is {num2}")
except NameError:
    traceback.print_exc()
try:
    print(f"outside func, num3 is {num3}")
except NameError:
    traceback.print_exc()
###############################################
    
print(f"Example5.10 Write a program for num1 in global scope , num2 & num3 in local scope. access all in main program")
import traceback
num1 = 10 
def func(num2):
    global num3    #num2 cannot be declared global as its in function header , that creates global & local conflict. num3 is fine
    num3 = 30
    print(f"Inside func, num1 is {num1}")
    print(f"Inside func, num3 is {num3}")
    
func(20)

print(f"outside func, num1 is {num1}")
print(f"outside func, num3 is {num3}")   

###############################################

print(f"Example5.11&12 declare outer var , declare inner value inside function , now access outer variable")

# to check if outer variables are affected by inner var with same name 

var = "Morning"
def func():
    var = "Evening"
    print(f"Inside var is {var}")
print(f"Outside var is {var}")

print(f"Outside var is {var}")  #check outer var first
func()                          # call func 
print(f"Outside var is {var}")  #check outer var after func 
var = "Evening"
print(f"Outside var is {var}")  #check outer after changing

###############################################


print(f"Example5.14 Nestes functions and variable scopes ")

def func_inner():
    var = "Evening"
    print(f"Var- inside called function -2 is {var}")
    
def func_inner_most():
    var = "Night"
    print(f"Var- inside called function -3 is {var}")

def func_outer():
    var = "Morning"
    print(f"Var- inside called function -1 is {var}")
    func_inner()
    func_inner_most()
    
func_outer()  

###############################################

'''
Every Function has a implicit return statement which return None 
which can be modified by return [expression] . As square bracket indicates its expression optional
'''

print(f"case1: implicit return  ")

def func():
    pass
print(func())

print(f"case2: return statement without args  ")

def func():
    return
print(func())

print(f"case3: return statement with args  ")

def func():
    return "home" "sweet" "home"
print(func())

###############################################

# 1) Required arguments
print(f"Required arguments Example")

def display(name, age, salary):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Salary: {salary}")
    
display("Ram", "12", "1")
display("1", "12", "Ram")  # Required args expect exact args with exact order as seen before 

# 2) keyword arguments
print(f"keyword arguments Example")
display(salary="1", age="12", name="Ram") 

# 3) default arguments
print(f"default arguments Example")
def display(name="Sam", age="14", salary="2"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Salary: {salary}")
    
display(salary="1", age="12", name="Ram") 
display("Sir") 
display(age="99") 
display() 

# 4) variable length arguments
print(f"Variable length arguments Example")

def display(*args):
    for each in args:
       print(each, end=" ")
       
display()
display(1,2,3,4,5,6)

def Study(name,*sub):  # Variable args , can have one or more mandatory args before them.
    print(f"\n{name} likes to study",end=" ")
    for each in sub:
       print(each, end=" ")
       
Study("Ram")
Study("Ram","maths","science")
    
'''
Anonymous Functions or lambda Functions.

Normal Functions can have statements , loops , expressions <---> Lambda functions cannot have all those , just a expression
Normal function need to be named                           <---> Lamda functions dont require name , if you want to reuse assign to var 
Normal Functions can have multiple expression              <---> Lamda functions are limited to single Expression
Normal Functions are multi line                            <---> Lamda functions are strictly single line without explicit return statement

def sum(x,y):
    return x+y
    
is same as 

sum = lambda x,y : x+y
sum(2,3)

Expression vs. Statement: Statements like if, for, or return do not evaluate to a value and are forbidden in lambdas. Function calls (even those with "side effects" like printing) are expressions.print() is a function, and calling a function is considered an expression

'''

print("\n************Lambda Functions*************")

print((lambda x,y,z: x+y+z) (1,2,3))  # Lambda with not even variables 
print((lambda x: 3*x*x+2*x+1)(2))
sum2 = lambda x,y : x+y   # does not need to have name 
print(sum2(2,3))


# Pass lamba to a function 

increment = lambda x : x+1
decrement = lambda x: x-1

def doNothing(func,args):
    print(func(args))
doNothing(increment,1)
doNothing(decrement,1)

def Greetorcurse(func):
    return(func())
    
greet = lambda : print("Good Morning")
curse = lambda : print("Get lost")

Greetorcurse(greet)
Greetorcurse(curse)

###############################################

# Documentation strings ''' or """ doent matter 

def sum(x,y):
    '''
    This is a standard funtion to perform addition
    takes x and y as args 
    both are integers
    '''
    return x+y
    
print(sum.__doc__)

###############################################

#Program 5.1 def to check if two numbers are equal or not 

def isEqual(m,n):
    if m == n:
        print(f"{m} is equal to {n}")
    else:
        print(f"{m} is not equal to {n}")
        
isEqual(5,6)
isEqual("d","d")
###############################################

#Program 5.2 Write a program to swap two numbers 

def swap(m,n):
    m,n = n,m
    return m,n
    
print(swap(2,3))
###############################################

#Program5.3 Def - take first name , last name and return full name 

def fullName(first,last):
    return first + " " + last
print(fullName("Ramanathan" , "Palaniappan"))

###############################################

# Program5.4 Write a program to return the average of its args 

def avgOfNum(*args):
    length = len(args)
    sum = 0
    for each in args:
        sum +=each 
    return sum/length
    
print(avgOfNum(1,2,3,4,5))
print(avgOfNum(10,20,30,40,50))

###############################################

# Program5.5 Write a Program to convert time in hrs & minutes  into minutes 

def convert(hrs,min):
    return (hrs*60 + min)
    
print(convert(2,10))
###############################################

# Program5.6 def to check if its even or odd 
def evenorodd(num):
    if num%2 == 0:
        return f"{num} is a even number"
    else:
        return f"{num} is a odd number"
        
print(evenorodd(24))
print(evenorodd(23))
###############################################

# Program 5.7 Write a program to calculate simple interest. If customer senior , 12 % if not 10 % 

def ROI(age,principal,years):
    if age >= 60:
        interest = principal * 0.12 * years
    else:
        interest = principal * 0.10 * years
    return interest

print(ROI(33,200000,3))
###############################################


'''
Recursive Functions has two parts 
Base case - > Problem is solved without making further calls 
Recursive case - > 1) Problem divided into sub-parts ,2)  Function calls itself to solve each sub-part 3) results are combined to solve original problem

Recursive funtion is divide and conquer
Take factorial n! = n(n-1)!..
The solving of problem yields a similar smaller problem . 

Base case return definitive 1 or 0 
recursive case return function itself with differnt arg  that will eventually deduce to base case 

'''
###############################################

# Recursive funtion to find n factorial 

def fact(n):
    if(n==1 or n==0):
        return 1                     #This is the Base case thats gonna break loop , if you remove this its indefinite loop
    else:
        return n*fact(n-1)
    
print(fact(5))

#A simple recursive function that counts down from 5:

def countdown(n):
    if n == 0:
        return "And its 0!, Done!!"
    else:
        print(f"{n}...!!")
        return countdown(n-1)

print(countdown(5))


# Fibonacci series 
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …


def fibon(n):
        if n == 0:
            return 0 
        elif n == 1:
            return 1
        else:
            return fibon(n-1) + fibon(n-2)
        
for i in range(10):
    print(fibon(i), end=" ")
    
###############################################

'''
Python Modules 

Any python code with py extenstion is a module. Module is searched in 3 places automatically without needing to use "import keyword"

1. Pythonpath directories
2. python installation directory 
3. current directories 

if your module is not in above location it can be imported in following ways , try in terminal 

1. import chapter5 (from chapter5 import * is not recommended by PEP , only import chapter5)
2. from chapter5 import subtr 
3. from chapter5 import subtr as kalithal
4. from chapter5 import subtr,swap

To display all var and function used in module use 
dir(chapter5)

Some of useful module functions are sys.argv for command line args and sys.exit to exit from execution
'''


'''
Python Namespaces 

Namespace allows us to use same variable name in a program. 
To elaborate , We know every python file is a module. Every module can have name var or function called summer.
it will be accessed as below 
module1.summer()
module2.summer()

Types of namespaces local , global , built-in 

print() , can be used in your main program , module or inside functions , its from global namespace 
if you use functions or var from modules , its called global . 
if you use var inside a functions , its local .

so you cannot access inside functio , variables in modules or python shell which have imported .

SO python follows LEGB rule 

A name is mentioned . search in LEGB hierarcy 

first in local , inside function 
second in enclosing , if its nested , search in outer enclosing functions 
thrid in global , that module file 
fouth in builtin like print , sum , abs 
'''


'''
Python packages 

Package is a folder structure for modules . 
and create a empty __init__.py in the folder to indicate it cotains modules.

we created two files named chapter4.py & chapter5.py in Desktop->study->studypy
create a __init__.py in study 
now go to study directory 
from studypy import chapter4
''''
