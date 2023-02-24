def count(str,ch):
    if not str:
        return 0
    elif str[0]==ch:
        return 1+count(str[1:],ch)
    else:
        return count(str[1:],ch)        
str = input("enter a string: ")
ch = input("enter a char: ")
print(count(str,ch))