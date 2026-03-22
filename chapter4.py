'''
Python Programming by Rameha Thareja

#feedback of chapter4 

1.  braces , quoatations are not balanced 
2. logical and is not there 
3. strings are not enclosed in quotes 
4. not thinking of variables going to be used and initialising those variables . 
5. Be mindful of variables . dont use diff variables without thinking
6. always in nexted loop , check if preveious conditions overlap. if yes shuffle to bottom .. 
7. math logic to be remembered for 
    a) armstrong number , 
    b) dec to binary conv & bin to decimal 
    c) GCD 
    d) string reverse 
    e) factorial
    f) Prime numbers
    g) leap year 
    
8. For math problems , handle the edges like 0 and 1 also 


#Learn
1.str and int are indeed distinct types. string has isdigit method wil tell if its digit(int). How cool is that 
2.string doesnt have append, It have concatenation
3. if is not a loop , its a statement (doubt arises when we see break or continue inside if
4. when loops like while and for are considered 
    a) while can be counter controlled or condition controlled 
        i) Counter controlled 
i = 8
while i > 0:
    print(i , end='') #prints 87654321 , so 8 times loop executes controlled by counter i 
    i -= 1
        ii) condition controlled 
i = 8
while i > 0:
    i -= 1
    if i % 2 == 0:
        print(i , end='') #prints 6420 , so only 4 times loop executes controlled by conditional statement
        continue 
5. break , continue , pass diff , all affect nearest enclosing loop (not statement) 

i = 1
while i <= 10:
    print(i , end='') #prints 1234 , loop terminates at i ==5 because of break 
    if i == 5:
        break
    i += 1


i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i , end='') #prints 1234678910 , loop skips at i ==5 alone because of continue 

i = 0
while i < 10:
    i += 1
    if i == 5:
        pass
    print(i , end='') #prints 12345678910 , loop does nothing and treats as placeholder at i ==5 alone because of pass 
6. Remember range(1,n) is will always eands at n-1
7. Remember pep guildelines recommends spaces instead tabs for indentation
    
''' 

#chapter4

###############################################
"""
#Program4.1 Write a program to determine whether a person is eligible to vote 

age = int(input("Enter your age:"))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
    
###############################################

#Program4.2 Write a program to determine the character entered by the user

input_char = input("Enter any char: ")
if input_char.isalpha(): 
    print("The " + input_char + " is a alphabet")
elif input_char.isdigit():
    print("The " + input_char + " is a number")
elif input_char.isspace():
    print("The " + input_char + " is a white space") 

###############################################

#Program4.3 Write a program to determine whether a person is eligible to vote or not if he is not 
#eligible , display how many years are left to be eligible 

age = int(input("Enter your age:"))
if age >= 18:
    print("You are eligible to vote")
else:
    print(f"you are eligible to vote in {18-age} years")
    
###############################################

#Program4.4 Write a program to find larger of two numbers

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

if num1 > num2:
    print(f"{num1} is larger than {num2}")
else:
    print(f"{num2} is larger than {num1}")

###############################################
   

#Program4.5 Write a program to find given number is odd or even 

num = int(input("Enter the number:"))
if num % 2 == 0:
    print(f"The {num} is even number")
else:
    print(f"The {num} is odd number")
    
###############################################

#Program4.6 Write a program to enter any character. if the enetered character is in lowercase then convert it to uppercase charcater or vice-versa

char = input("Enter the character:")
if char.islower():
    print(chr(ord(char)-32))
else:
    print(chr(ord(char)+32))
###############################################


# Program 4.7 if male 5 % bonus , female 10 % bonus , overall if salary less than 10k , extra 2 % . display salary

gender = input("Enter your gender male or female:")
salary = int(input("Enter your current salary:"))
if salary < 10000 and gender == 'male':
    salary += salary * 0.07
elif salary > 10000 and gender == 'male':
    salary += salary * 0.05
elif salary > 10000 and gender == 'female':
    salary += salary * 0.1
elif salary < 10000 and gender == 'female':
    salary += salary * 0.12
    
print(f"Congrats!! Your bonus is {salary}")
    
###############################################


#Program 4.8 Write a program to find whether given year is leap year or not 

year = int(input("Enter the year:"))
if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    print(f"The entered year {year} is leap year")
else:
    print(f"The entered year {year} is not leap year")

###############################################    

#Program4.9 Write a program to determine whether characted entered is vowel or not 

char = input("Enter char:")
if char in ['a','e','i','o','u']:
    print("The character is vowel")
else:
    print("The character is not vowel")

###############################################    
#Program4.10 Write a program to find the greatest number from three numbers 

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

if num1 > num2 and num1 > num3:
    print(f"{num1} is larger than {num2} and {num3}")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is larger than {num1} and {num3}")
elif num3 > num1 and num3 > num2:
    print(f"{num3} is larger than {num1} and {num2}")

###############################################    
     
#Program4.11 Write a program that prompts the user to enter a num between 1-7 and then displays a corresponding day of the week 

num = int(input("Enter the num between 1-7:"))
if num ==1:
    print("The day of the week is Sunday")
elif num ==2:
    print("The day of the week is Monday")
elif num ==3:
    print("The day of the week is Tuesday")
elif num ==4:
    print("The day of the week is Wednesday")
elif num ==5:
    print("The day of the week is Thursday")
elif num ==6:
    print("The day of the week is Friday")
elif num ==7:
    print("The day of the week is Saturday")

###############################################    

#Program 4.12 Write a Program to calulate tax given in following situations 
#if taxable income is less than 1,50,000 then no tax 
# 1,50,001 - 300000 then charge 10% tax , 300001 - 500000 then charge 20 % 
# 5,00001 above 30 % 

income = int(input("Enter your income:"))
taxable_income = income - 150000 
if income < 150000:
    print("You are not required to pay nay tax")
elif 150001 < income < 300000:
    print(f"Need to pay tax {taxable_income * 0.1}")
elif 300001 < income < 500000:
    print(f"Need to pay tax {taxable_income * 0.2}")
else:
    print(f"Need to pay tax {taxable_income * 0.3}")

###############################################    
 

#Program 4.13 Write a Program to take input from the user and then check whether it is a number or a character 
#if its a character , determine whether its in uppercase or lowercase 

# i have nerver known input result is string but it has isdigit & isalpha 

#>>> a = 5
#>>> type(a)
#<class 'int'>
#>>> a = "5"
#>>> type(a)
#<class 'str'>
#>>> a.isdigit()

input_sample = input("Enter a number or character: ")
if input_sample.isdigit() ==1:
    print("you have entered a digit")
elif input_sample.isalpha() ==1:
    if input_sample.islower():
        print("You have entered lowercase")
    elif input_sample.isupper():
        print("you have entered uppercase")
else:
    print("its neither a digit nor a character")

###############################################     

#Program4.14 write  aprogram to print rank card 75 above is distinction 
#60 -75 its first class , 50 -60 is second class 40 -50 is third division , else fail

total_marks = int(input("Enter your total marks: "))

if total_marks >= 75:
    print("Congrats , you passed in distinction!")
elif 50 <= total_marks < 75:
    print("Congrats , you pass in first class!")
elif 40 <= total_marks < 50:
    print("Congrats , you passed in second class!")
else: 
    print("Fail! better luck next time!")
    
###############################################    

#Program4.15 Write a program to clalculate the roots of quadratic equation - skip too complex maths

#Program 4.16 Write a program to calculate the sum and vaerage of first 10 numbers 

n=10
sum = 0 
average = 0
while n > 0:
    sum += n
    n -=1
average = sum/10

print(f"The sum of first 10 numbers is {sum} whereas average is {average}")

###############################################    
 

#Program4.17 print 20 horizontal asterisk (*)

i = 20 
while i > 0:
    print('*',end=" ")
    i -=1
###############################################    
 
#Program4.18 Calculate the sum of numbers of m to n 

m = int(input("Enter the start of numbers: "))
n = int(input("Enter the end of numbers: "))
i = m
sum = 0

while(i <=n): 
    sum += i
    i += 1
print(f"the sum of numbers from {m} to {n} is {sum}")

###############################################    
     

#Program4.19 Write a Program to read the numbers until -1 is encountered. Also count the negative , positives & Zeroes entered by user

count_pos = count_neg = count_zer = 0
while(1):
    input_var = int(input("Enter any num +ve , -ve , zero to continue & -1 to exit: "))
    if input_var > 0: 
        count_pos += 1
    elif input_var == -1:
        break
    elif input_var == 0:
        count_zer += 1
    elif input_var < 0:
        count_neg += 1
print(f"The number positives entered is {count_pos} & number of negatives are {count_neg} & number of zeroes are {count_zer}")

###############################################    

#Program4.20 Write a Program to read the numbers until -1 is encountered. Also avg of the negative , positives  entered by user

count_pos = count_neg = sum_pos = sum_neg = 0

while(1):
    input_var = int(input("Enter any num +ve , -ve , zero to continue & -1 to exit: "))
    if input_var > 0: 
        count_pos += 1
        sum_pos += input_var
    elif input_var == -1:
        break
    elif input_var < 0:
        count_neg += 1
        sum_neg += input_var
print(f"The avg positives entered is {sum_pos/count_pos} & number of negatives are {sum_neg/count_neg}")

###############################################    
  

#Program4.21 Whether its an armstrong --> math logic to be remembered 

#1 = 1pow1 = 1 
#2 = 2pow1 = 2
#153 = 1pow3 + 5pow3 + 3 pow3 = 1 + 125 + 27 = 153 
#1634 = 1pow4 + 6pow4 + 3 pow4 + 4 pow4 = 1 + 1296 + 81 + 256 = 1634

sum = 0
input_number = input("Enter the number: ")
length = len(input_number)
for each in input_number:
    sum += int(each) ** length
if sum == int(input_number):
    print(f"The {input_number} is an armstrong number")
else:
    print(f"The {input_number} is not an armstrong number")
    
###############################################    


#Program4.22 Write a program to enter decimal . convert to binary 

# 7 --> 7/2 - reminder 1 Quotient 3 ; 3/2 - reminder 1 Quotient 1 ; one is not divisible , so write all reminders + undivisible quotient - 111
# 13 --> 13/2 -  reminder 1 Quotient 6 ; 6/2 -  reminder 0 Quotient 3 ;3/2 - reminder 1 Quotient 1 ; one is not divisible , so write all reminders + undivisible quotient - 1011
#so reminders of modulo should be taken until its greater than 2 
#verdict string is always easy 

#binary_num = ''
#input_num = int(input("Enter the decimal num: "))
#i = input_num 
#while i != 0:
#    binary_num += str(i%2)
#    i = i//2
#print(f"The binary equivalent of {input_num} is {binary_num}")

binary_num = 0
input_num = int(input("Enter the decimal num: "))
i = input_num 
j = 0
while i != 0:
    binary_num += (i%2) * (10**j)
    i = i//2
    j += 1
print(f"The binary equivalent of {input_num} is {binary_num}")

###############################################    

#Program4.23 Write a program to enter a binary number and convert into decimal

decimal_num = 0
input_num = input("Enter the binary num: ")
i = 0 
for each in input_num[::-1]:
    decimal_num += int(each) * (2 ** i)
    i +=1
    print(decimal_num)

print(f"The decimal equivalent of {input_num} is {decimal_num}")

###############################################    

#Program4.24 Write a Program to read character until a * encontered . Count upper, lower and numbers by users

count_upp = count_low = count_num = 0
while(1):
    input_var = input("Enter any alphabets or numbers to continue & * to exit: ")
    if input_var.isalpha() and input_var.isupper(): 
        count_upp += 1
    elif input_var.isalpha() and input_var.islower(): 
        count_low += 1
    elif input_var.isdigit():
        count_num += 1
    elif input_var == '*':
        break
print(f"The number uppercase entered is {count_upp} & number of lowercase are {count_low} & number of numbers are {count_num}")


###############################################    

#Program4.25 Write a program to enter number abd calculate sum of its digits

sum = 0
input_number = input("Enter the number: ")
length = len(input_number)
for each in input_number:
    sum += int(each)
print(f"The sum of  {input_number} is {sum}")

###############################################   

#Program4.26 Write a Program to calculate GCD of two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd = 1

if {num1 < num2} :
    low_num = num1
else:
    low_num = num2

for each in range(2,low_num):
    if num1%each ==0 and num2%each == 0:
        gcd = each 
    
print(f"The GCD of {num1} & {num2} is {gcd}")

###############################################  

#Program4.27 Write a program to print reverse of the number 

input_num = input("Enter the number: ")
rev_num = ''
for each in input_num:
    rev_num = each + rev_num
print(f"The reverse of {input_num} is {rev_num}")

###############################################    

#Program4.28 Write a program to print down count down that input number to Zero 

input_num = int(input("Enter the number: "))
while input_num >= 0:
    print(input_num)
    input_num -=1

###############################################    


#Program 4.29 Write a program using for to calculate avg of first n natural numbers
n = int(input("Enter number upto avg should be calc"))
sum = 0
for each in range(1,n):
    print(each)
    sum += each
print(f"The avg of first {n} numbers is {sum/n}")

###############################################    

#Program 4.30 Print multiplication table of n entered by user

n = int(input("Enter the n for which multiplication table has to be printed: "))
print(f"The multiplication table for {n} as follows")
print('*'*40)
for each in range(1,11):
    print(f"{n} x {each} = {n*each}")

###############################################    
 

#Program 4.31 print all numbers from m- n and clarify if its even or odd 
m = int(input("Enter start number of series: "))
n = int(input("Enter end number of series: "))

for each in range(m,n+1):
    print(f"The number you entered is {each} and its a {"even" if each%2 == 0 else "odd"} number")

###############################################    
    

#Program4.32 Write a program using for loop to calc factorial of num 

# n! = n(n-1)(n-2)..1
n = int(input("Enter number for factorial: "))
factorial = 1
for each in range(1,n+1):
    factorial *= each
print(f"The {n} factorial is {factorial}")

###############################################    
   
#Program4.33 Write a program to classify a given number as prime or composite

#Prime numbers are natural numbers greater than 1 with exactly two factors: 1 and themselves. Examples include 2, 3, 5, 7, 11, 13, 17, 19, 23, and 29

input = int(input("Enter a number of your choice: "))
if input <= 1:
    print(f"The number {input} is neither prime nor composite")
else:
    iscomposite = 0
    for each in range(2,input):
        if input%each == 0:
            iscomposite = 1
            break
    if iscomposite:
        print(f"The number {input} is composite number")
    else:
        print(f"The number {input} is a prime number")

###############################################    


#Program4.34 Write a Program using while loop to read the numbers until -1 is entered . count number of prime & composite 

count_prim = count_comp = 0
while(1):
    input_var = int(input("Enter a number of your choice: "))
    iscomposite = 0
    if input_var == -1:
        break
    else:
        for each in range(2,input_var):
            if input_var%each == 0:
                iscomposite = 1
                break
        if iscomposite:
            count_prim += 1
        else:
            count_comp += 1
print(f"The number prime numbers entered is {count_prim} & The number prime numbers entered is {count_comp}")
###############################################    

#Program4.35 Write a program to calculate pow(x,n)

#logic pow(2,3) == 2*2*2

x = int(input("Enter the number: "))
n = int(input("Enter the power to which to be calculated: "))

pow = 1
for each in range(1,n+1):
    pow *= x
print(f"{x} raised to the power of {n} is {pow}")
    
###############################################    

#Program 4.36 Write a program that displays all leap years from 1900-2101

print("Leap years from 1900-2101 are", end=' ')
for year in range(1900,2101):
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        print(year,end=' ')

###############################################    

#Program 4.37 Write a program to sum the series 1 + 1/2 + ... 1/n

n = int(input("Enter the numbers: "))
i = 1
sum = 0

while(i <=n): 
    sum += 1/i
    i += 1
print(f"the sum of series upto {1/n} is {sum}")

###############################################    


#Program 4.38 Write a program to sum the series 1 + 1/2^2 + ... 1/n^2

n = int(input("Enter the numbers: "))
i = 1
sum = 0

while(i <=n): 
    sum += 1/(i**2)
    i += 1
print(f"the sum of series upto {1/n} is {sum}")

###############################################    

#Program 4.39 Write a program to sum the series 1/2 + 2/3 + ... n/n+1

n = int(input("Enter the numbers: "))
i = 1
sum = 0

while(i <=n): 
    sum += i/(i+1)
    i += 1
print(f"the sum of series upto {n/n+1} is {sum}")


###############################################    

#Program 4.40 Write a program to sum the series 1/2 + 2^2/2 + 3^3/3 + ... n^n/n
n = int(input("Enter the numbers: "))
i = 1
sum = 0

while(i <=n): 
    sum += i**i/i
    i += 1
print(f"the sum of series upto {n**n/n} is {sum}")

###############################################    

#Program 4.41 Write a program to calculate the sum of cubes of numbers from 1-n
n = int(input("Enter the numbers: "))
sum = 0 

for each in range(1,n+1):
    sum += each ** 3
print(f"The sum of cubes of numbers from 1-{n} is {sum}")

###############################################    

#Program 4.42 Write a program to calculate the sum of squares of even numbers
n = int(input("Enter the number: "))
sum = 0 

for each in range(1,n+1):
    if each%2 == 0:
        sum += each ** 2
print(f"The sum of squares of even numbers upto {n} is {sum}")

###############################################    

# Program 4.43 Write a program to calculate value of investment over a time with input intial investment and annual interest for every year

val_init = int(input("Enter the initial investment value: "))
roi = int(input("Enter the rate of interest: "))
yrs = int(input("length of investment: "))
val_fut = val_init
for each_year in range(1,yrs+1):
    val_fut = val_fut + (val_fut * roi/100) 
    print(f"year {each_year} : {val_fut}")

###############################################    


# Program 4.44 Write a program to generate Monthly calender , by inputting first monday date of month & number of days 

# Revisit later using matrix

# Program 4.45 Write a program to print the following pattern

#Pass 1- 1 2 3 4 5
#Pass 2- 1 2 3 4 5
#Pass 3- 1 2 3 4 5 

#FOr nested loop , this is order , outer loop executes once , then inner loop completes . Then comes outer loop once , then full inner loop
# completes. so for printing programs , only outerloop may have new line printing , if inner loop has , it cannot go to upper line


for i in range(1,6):
    print(f"Pass {i}-",end =" ")
    for j in range (1,6):
        print(f"{j}",end = " ")
    print()
    
###############################################    
  

#Program4.47: Write a program to print following pattern 

#  **********
#  **********
#  **********
#  **********
#  **********

for i in range(1,7):
    print("*",end='')
    for j in range(1,7):
        print("*",end='')
    print()
    
###############################################    

#Program 4.48 Write a program to print following pattern.

# 1 
# 1 2 
# 1 2 3
# ...
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
    
###############################################    
 
#Program 4.49 Write a program to print following pattern.

# 1 
# 22
# 333
# 4444
# 55555

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end='')
    print()

###############################################    

#Program 4.50 Write a program to print following pattern.

# 0 
# 12
# 345
# 6789

count = 0
for i in range(0,5):
    print()
    for j in range(0,i):
        print(count,end='')
        count +=1
        
###############################################    


#Program 4.52 Write a Program to print the following pattern 

#        1  
#      1 2 1
#    1 2 3 2 1
#.........................
#1 2 3 4 5 4 3 2 1

#revisit 

###############################################    

#Program 4.53 Write a program to print the following pattern 

#        1  
#      2  2 
#    3  3  3
#.........................
#  5 5 5 5 5 5

#revisit 

###############################################    
"""

# Program 4.54 Write a program to sqare root of number 

n = int(input("Enter the number: "))
sum = 0 

for each in range(1,n+1):
    sum += each ** 2
print(f"The sum of cubes of numbers from 1-{n} is {sum}")



