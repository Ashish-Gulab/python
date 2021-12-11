# Factorial using iterative approach
def factorial(n):
    fact=1
    assert n>=0
    for i in range (1,n+1):
        fact=fact*i
    return fact

n=int(input("Enter the number"))
fact=factorial(n)
print("Factorial of",n,"is",fact)
