def fibonacci(n):
    assert n>=1 
    a=0
    b=1
    
    if n==1:
        return a
    elif n==2:
        return b
    for i in range (3,n+1):
        result=a+b
        a=b
        b=result
    return result
def main():
    num= int(input("Enter the number"))
    number=fibonacci(num)
    print("The fibonacci number","is",number)
if __name__=='__main__':
    main()
