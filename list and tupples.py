#first list
marks=[94,34,12,24,46]
print(marks)
print(type[list])
print(marks[0])
print(marks[3])
print(len(marks))
#student
student=["rafay",74,19,"lahore"]
print(student)
print(student[0])
student[0]="Darling"
print(student)      
#slicing
civillines=[45,46,23,87,23,56]
print(civillines[3:5])
#append
clg=[4,45,23]
clg.append(4)
print(clg)
#sort
me=[34,32,22,21,45]
me.append(3)
me.sort()
print(me)
#reverse method of list
she=[34,32,12,56,55]
she.reverse()
print(she)
#Decsending order
bilal=[34,4,32,46.9]
bilal.sort(reverse=True)
print(bilal)
#insert value
bai=[34,342,46,66]
bai.insert(0,23)
print(bai)
#insert_remove
nums=[1,2,3,4,5]
nums.insert(0,8)
print(nums)
nums.remove(3)
print(nums)
#POP index ki base per value remove or return kerwata ha 
a=[10,20,30]
x=a.pop(1)
print(a,x)
#pop second practice
b=[34,32,23]
z=b.pop(0)
print(b,z)
#extend do list ko merge krta ha means k jod deta ha 
w=[34,32,45,65]
e=[3,5,54,43]
w.extend(e)
print(w)
#practice of extend
nimra=[46,89,92,27,2]
SEA=[45,23,5,46]
nimra.extend(SEA)
print(nimra)
#count btata ha value kitni bar ha 
fet=[34,2,65,2,2,34]
fet.count(34)
print(fet.count(34))
#index
hello=[4,32,123,53]
print(hello.index(123))
#test
fruits=[]
for i in range(1,6):
  fruit=input("Enter your  fruit name that you have:")
  
  fruits.append(fruit)
  print("\n")
print(fruits)
fruits.reverse()
print(fruits)
fruits.remove(fruits[0])
print(fruits)
fruits.sort()
print(fruits)
#practice sum and average using for loop and list
num=[]
su=0
for k in range(5):
  ali=int(input("Enter number:"))
  print("\n")
  num.append(ali)
  su=su+ali
its=(len(num))
avg=su/its
print(num)
print("sum=",su)
print("average=",avg)
#maximum
smile=[]
for l in range(5):
  marks=int(input("enter number:"))
  smile.append(marks)      #append function list ma marks ma aya variable store krwata ha ager hm user se string lein gy to input wale parts se int hata dein gy 
print(marks)
big=max(smile) 
small=min(smile)
print("Maximum=",big)
print("Minimum",small)
#take 10 nmbers from users and identify odd ,even and counting
test=[]
even=0
odd=0
for d in range(10):
  book=int(input("Enter number:"))
  test.append(book)
  if book%2==0:
    even+=1
  else:
    odd+=1 
print(even)     
print(odd)
print(len(test))
