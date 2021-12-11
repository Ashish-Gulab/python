import cmath
a=int(input("Enter the number"))
b=int(input("Enter the number"))
c=int(input("Enter the number"))
d=b*b-4*a*c
solution1=(-b-cmath.sqrt(d))/2*a
solution2=(+b-cmath.sqrt(d))/2*a
print("The solutions are".format(solution1,solution2))
