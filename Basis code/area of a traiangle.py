n1=int(input("enter the length of the triangle"))
n2=int(input("enter the breadth of the triangle"))
n3=int(input("enter the height of the triangle"))
n4=(n1+n2+n3)/2
area=(n4*(n4-n1)*(n4-n2)*(n4-n3))**0.5
print("area of the triangle is %.2f"%area)
