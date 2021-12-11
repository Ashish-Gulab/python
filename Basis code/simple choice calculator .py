def sum(x,y):
    return x+y
def difference(x,y):
    return x-y
def product(x,y):
    return x*y
def division(x,y):
    return x/y
print("1-> Addition")
print("2-> Subtraction")
print("3-> Multiplication")
print("4-> Division")
choice=input("enter your choice(1/2/3/4):")
if  choice in ('1','2','3','4'):
    num1=eval(input("enter the first number:"))
    num2=eval(input("enter the second number:"))
    if choice=='1':
        print("sum of",num1,"+",num2 ,"=",sum(num1,num2))
    if choice=='2':
        print("difference of",num1,"-",num2,"=",difference(num1,num2))
    if choice=='3':
        print("product of",num1,"*",num2,"=",product(num1,num2))
    if choice=='4':
        print("division of",num1,"/",num2,"=",division(num1,num2))
    
else:
    print("enter the correct choice")
