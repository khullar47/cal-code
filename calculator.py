# Write a program to calculate Pow(x,n), Add(x,n), Sub(x,n), Mul(x,n), Div(x,n)? Get the input and choice from the user.

def pow(x,n):
    return x**n
def add(x,n):
    return x+n
def sub(x,n):
    return x-n
def mul(x,n):
    return x*n
def div(x,n):
    return x/n
def calc(i):
        switcher={
                '^':pow(x,n),
                '+':add(x,n),
                '-':sub(x,n),
                '*':mul(x,n),
                '/':div(x,n)
             }
        return switcher.get(i,"Invalid input")
# print("Enter the values of x and n")
# x=int(input("Enter x "))
# n=int(input("Enter n "))
# i=(input("ENTER CHOICE "))
print("ENTER EXPRESSION WITH EACH OPERATOR SEPERATED BY ENTER")
# x=int(input())
# i=(input())
# n=int(input())
x,i,n=int(input()),input(),int(input())
print("Answer is : ", end="")
print(calc(i))
