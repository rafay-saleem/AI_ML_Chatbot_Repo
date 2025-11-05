#first if code
Num=int(input("Enter number:"))
if Num<=10:
  print("you are right")
else:
  print("Enter right number")
# even/odd
rafay=int(input("nter your digit"))
if rafay%2==0:
  print("it is even")
else:
  print("it is odd")

#Grades
marks=int(input("Enter your marks"))
if marks>=90:
  print("Your Grade is A+")
elif marks >=80:
  print("Your Grade is A")
elif marks >=70:
  print("Your grade is B")
else:
  print("SORRY YOU ARE FAIL ")

#Checker
ber=int(input("Enter number of checking"))
if ber<0:
  print("it is negative")
elif ber>0:
  print("Number is positive")
else:
  print("it is zero:")

#Age
age=int(input("Enter your age"))
if age<13:
  print("You are child")
elif age>=13 and age<=19:
  print("teenage")
else:
  print("adult")

#Number comparison
firstnum=int(input("Enter   first   no"))
secondnum=int(input("Enter second number"))
thirdnum=int(input("Enter third number"))
if firstnum>secondnum and firstnum>thirdnum:
  print("First number is greate")
elif secondnum>firstnum and secondnum>thirdnum:
  print("Second number is greater than all")
elif thirdnum>firstnum and thirdnum>secondnum:
  print("Third number is greater than all")
else:
    print("The comparison is not possible because all the enter numbers are equals")

#Student Marks Grading with Distinction
mark=int(input("Enter marks : you got"))
if mark>90 and marks==100:
  print("A+_Excellent! Dstinction")
elif mark<=75 and marks<=89:
  print("Grade A Very Good")
elif mark<=60 and marks<=74:
  print("Grade is B Nice")
elif mark<=50 and marks<=59:
  print("Grade is C Good work")
elif mark >49:
  print("Grade F")
else:
  print("Invalid mark enter")

#practice of if temperature
temp=int(input("Enter temperature"))
if temp<0:
  print("Freezing Weather:")
elif temp<=20:
  print("Cold Weather:")
elif temp<=31:
  print("Normal Weather:")
elif temp<=40:
  print("Hot  weather:")
else:
  print("Weather is very  hot")      
#loop practice
for ra in range(2,21,2):
 print(ra)
         
#factorial 
y=int(input("Enter which number of factorial do you want:"))
saban=1
if y==0:
  print("1")
else:
  for  wt in range(2,saban,-1):
    saban=saban*wt
  print("Factorial",saban)
#sum for all dear
sail=int(input("Enter number till you want sum")) 
sum=0
for she in range(1,sail+1):
  sum=sum+she
print("sum=",sum)   
#sum even input
ze=int(input("enter number"))

total=0
for des in range(0,ze+1,2):
  total=total+des
print("total=",total)  