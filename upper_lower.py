lam = input("Enter a string:")
lower,upper = 0,0 
for i in lam :
    if i.islower() :
        lower += 1
    elif i.isupper() :
        upper += 1
print("Lower case :",lower,"Upper case:",upper)
