n = int(input("enter a num: "))
count =0 
while n>0 :
    n &= n-1
    count +=1
print(count)