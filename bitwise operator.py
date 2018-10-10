a=int(input("enter the first value a:"))
b=int(input("enter the second value b:"))
print(" before swapping two number:a={0} b={1}" format (a,b))
a=a^b
b=a^b
a=a^b
print("after swapping two number a={0} and b={1}", format (a,b))
