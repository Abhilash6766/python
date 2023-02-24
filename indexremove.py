str = input("enter a string: ")
n = int(input("enter nth index: "))
first = str[:n]
last = str[n+1:]
print(first+last)