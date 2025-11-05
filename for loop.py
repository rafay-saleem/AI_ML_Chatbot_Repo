for i in range(5):
    print("Rafay")

#print counting 
for j in range(0,6):
    print(j)
#loop for table
table=int(input("Enter number of which table do you want"))
for me in range(1,11):
    print(table,"x",me,"=",table*me)    
#Reverse Table lOOP 
resv=int(input("Enter which number of table do you want"))
for you in range(10,0,-1):
    print(resv,"x",you,"=",resv*you)
#Factorial
fact = int(input("Enter which number of factorial you want: "))
factorial = 1

if fact == 0:
    print("Factorial of this number is 1")
else:
    for she in range(fact, 1, -1):
        factorial = factorial * she   # multiplication logic same
    print("Factorial of the number is:", factorial)  # print loop ke bahar
#staric
for m in range(1,6):
    print("*" *m)