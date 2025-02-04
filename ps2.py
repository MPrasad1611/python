year=int(input("Enter any year: "))
if (year%4==0 and year%100!=0) or year%400==0:
    print("Leap Year")
else:
    print("Not a Leap Year")
#r="Leap Year"if(year%4==0 and year%100!=0) or year%400==0 else "Not a Leap Year"