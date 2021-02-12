x=int(input("Enter the values:"))
y=int(input("Enter the values:"))
z=int(input("Enter the values:")) 
a_square_numbers=lambda x:x*x
a_rectangle_numbers=lambda x,y:x*y
a_tringle_numbers=lambda s,x,y,z:(s*(s-x)*(s-y)*(s-z))**0.5
s=(x+y+z)/2
print(a_square_numbers(x))
print(a_rectangle_numbers(x,y))
print(a_tringle_numbers(s,x,y,z))
