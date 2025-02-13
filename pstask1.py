a=float(input("Enter Any Number:"))
#output: Positive, Negative, Zero      
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")

#output: Odd or Even
if a%2==0:
    print("Even")
else:
    print("Odd")


age=int(input("Enter your age: "))
#output: Eligible for voting or not
if age>=18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")

#output: Greater number among two numbers
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
if num1>num2:
    print("First number is greater than second number")
else:
    print("Second number is greater than first number")

#output: Pass or Fail
marks=int(input("Enter your marks: "))
if marks>40:
    print("You are pass")
else:
    print("You are fail")


#days of week
number=int(input("Enter number from 1 to 7: "))
if number>7:
    print("please enter number from 1 to 7 only")
elif number==1:
     print("Monday")
elif number==2:
     print("Tuesday")
elif number==3:
     print("Wednesday")
elif number==4:
     print("Thursday")
elif number==5:
     print("Friday")
elif number==6:
     print("Saturday")
else:
    print("Sunday")

#calculator
str=input("Enter Arithmetic Operation:").lower()
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if str=="add":
    print(a+b)
elif str=="sub":
    print(a-b)
elif str=="mul":
    print(a*b)
elif str=="div":
     st="Division by zero is not possible"if b==0 else a/b
     print(st)
else:
    print("Invalid Operation")

#month of year
number2=int(input("Enter any number from 1 to 12: "))
if number2>12:
    print("Please enter number from 1 to 12 only")
elif number2==1:
    print("January")
elif number2==2:
    print("February")
elif number2==3:
    print("March")
elif number2==4:
    print("April")
elif number2==5:
    print("May")
elif number2==6:
    print("June")
elif number2==7:
    print("July")
elif number2==8:
    print("August")
elif number2==9:
    print("September")
elif number2==10:
    print("October")
elif number2==11:
    print("November")
else:
    print("December")
     
#greates of three numbers
fnum=int(input("Enter the first number: "))
snum=int(input("Enter the second number: "))
tnum=int(input("Enter the third number: "))
if fnum>snum and fnum>tnum:
    print(f"{fnum} is greatest")
elif snum>fnum and snum>tnum:
    print(f"{snum} is greatest")
else:
    print(f"{tnum} is greatest")

#vowel or consonant
char=input("Enter any single character: ").lower()
if char.isalpha()==False:
    print("Not a character")
elif char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
    print("Vowel")
else:
    print("Consonant")

#leap year
year=int(input("Enter any year: "))
if year%4==0 and year%100!=0 or year%400==0:
    print("Leap Year")
else:
    print("Not a Leap Year")

#grades
score=int(input("Enter your score: "))
if score>=90:
    print("Grade A")
elif score>=80:
    print("Grade B")
elif score>=70:
    print("Grade C")
else:
    print("Fail")

#valid triangle or not
side1=int(input("Enter the first side of triangle: "))
side2=int(input("Enter the second side of triangle: "))
side3=int(input("Enter the third side of triangle: "))
if side1+side2>side3 and side2+side3>side1 and side1+side3>side2:
    print("Triangle is valid")
else:
    print("Triangle is not valid")