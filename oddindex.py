str=input("enter a string: ")
ans=""
for i in range(len(str)):
    if i % 2 == 0:
        ans += str[i]
print(ans)