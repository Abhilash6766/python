num = int(input("enter a number"))
temp = num 
digits = 0
while temp != 0 :
    digits += 1
    temp = temp//10
sum=0
temp = num
while num >0 :
    rem = num % 10
    sum += rem**digits
    num = num//10
if temp == sum :
    print("IS ARMSTRONG")
else :
    print("Is Not Armstrong")
