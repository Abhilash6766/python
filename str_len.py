str = input("enter string: ")
count = 0
while str:
    count+=1
    str = str[1:]
print(count)