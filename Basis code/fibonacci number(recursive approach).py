#fibonacci number using recursive function
def fibonacci(n):
    assert n>0
    second_last=0
    last=1
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
def main():
    num=int(input("Enter the number"))
    fibo=fibonacci(num)
    print("Fibonacci number of",num,"is",fibo)
if __name__=='__main__':
    main()
    
