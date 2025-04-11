a=10
b=5
c=3

#if simple
if a>b:
    print("a es mayor que b")

#if doble
if a >b:
    print(a, "a es mayor que b", b)
else:
    print(a, "a no es mayor que b", b)

#elif
if a>b:
    print(a, "a es mayor que b", b)
elif a==b:
    print(a,"a es igual que b",b)
else:
    print(a,"a no es mayor que b",b)

#if compuesto
if a>b:
    print("a es mayor que b")
    if a>c:
        print("a es maor que c")
    else:
        print("a no es mayor que c")
else:
    print("a no es mayor que b")
    if a>c:
        print("a es mayor que c")
    else:
        print("a no es mayor que c")