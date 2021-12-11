'''factorial program using recursive approach'''
def factorial(n):
    assert n>=0
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter the number"))
fact=factorial(n)
print("The factorial of",n,"is",fact)

