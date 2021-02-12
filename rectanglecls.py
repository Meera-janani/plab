class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    
a = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
obj = Rectangle(a, b)
print("area:",obj.area())
print("perimeter:",obj.perimeter())
a2 = int(input("Enter length of the rectangle : "))
b2 = int(input("Enter width of the rectangle : "))
obj2 = Rectangle(a2,b2)
while(True):        
        if obj.area() >= obj2.area():
            if obj.area() == obj2.area():
                print("Rectangles area are  equal")
            else:
                print("Rectangle one is large")
        else:
           print("Rectangle Two is large")

    
    
