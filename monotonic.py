def mono(a):
    x,y=[],[]
    x.extend(a)
    y.extend(a)
    x.sort()
    y.sort(reverse=True)
    if a==x or a==y :
        print("monotonic")
    else:
        print("not monotonic")
a = [6,5,4,4]
mono(a)