def product(a,b):
    if b==0:
        return 0
    else:
        return a + product(a,b-1)
a=int(input("enter the value of a :"))
b=int(input("enter the value of b :"))
print(product(a,b))