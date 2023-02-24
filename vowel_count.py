str = input("enter the string: ")
str = str.lower()
count = 0
for i in str:
    if i=='a' or i=='e' or i=='o' or i=='u' or i=='i':
        count = count+1
print(count)