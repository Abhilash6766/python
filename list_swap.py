n = int(input("Enter length of list:"))
print("Enter ",n,"numbers")
l = []
for i in range(0,n) :
    l.append(int(input()))
x = int(input("Enter number to swap:"))
y = int(input("Enter another number to swap:"))
a ,b = -1,-1
for i in range(0,n) :
    if l[i] == x :
        a = i
        break
for i in range(0,n) :
    if l[i] == y :
        b = i
        break
l[a],l[b] = y,x
print(l)