import math as m
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = (b*b)-(4*a*c)
if d==0 :
    r1 = (-b+m.sqrt(d))/2*a
    r2 = (-b-m.sqrt(d))/2*a
    print("real and equal\n")
    print(r1,"\n",r2)
elif d>0 :
    r1 = (-b+m.sqrt(d))/2*a
    r2 = (-b-m.sqrt(d))/2*a
    print("\nreal and distinct\n")
    print(r1,"\n",r2)
else:
    print("\nimaginary roots")
