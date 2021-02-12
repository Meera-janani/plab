class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width
    
    def __lt__(self,second):
       if self.area < second.area:
            return True
        
a = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))
obj = Rectangle(a, b)
print("area:",obj.rectangle_area())
a2 = int(input("Enter length of the rectangle : "))
b2 = int(input("Enter width of the rectangle : "))
obj2 = Rectangle(a2,b2)
print("area2:",obj2.rectangle_area())       
while(1):
        if obj.rectangle_area() >= obj2.rectangle_area():
            if obj.rectangle_area() == obj2.rectangle_area():
                print("Rectangles area are  equal")
            else:
                print("Rectangle one is large")
        else:
           print("Rectangle Two is large")

