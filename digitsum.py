n = int(input("enter a digit: "))
sum=0
while n > 0 :
    rem = n%10
    sum += rem
    n = n//10
print("sum = ",sum)