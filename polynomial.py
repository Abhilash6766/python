import math
print("enter coefficents of ax^3+bx^2+cx+d : ")
lst = []
for i in range(0,4) :
    a=int(input())
    lst.append(a)
x = int(input("enter x: "))
j=3
sum=0
for i in range(0,4):
    sum = sum+(lst[i]*math.pow(x,j))
    j=j-1
print(sum)
