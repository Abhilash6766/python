str = input("enter the string: ")
count=0
for i in str:
    if i.islower():
        count = count+1
print(count)