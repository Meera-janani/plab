import module
from module import circle,rectangle
from module import module1
from module.circle import *

print("Area of a circle with radius 7 is : ",circle.area_circle(7))
print("Permeter of a circle with radius 7 is ",circle.perimeter_circle(7))

print("Area of a circle with radius 7 is : ",area_circle(7))

print("Area of a Rectangle with length and width 7 is : ",rectangle.area_rec(7,7))
print("Permeter of a Rectangle with length and width 7 is : ",rectangle.perimeter_rec(7,7))

print("Area of a  cuboid with length,width,height 7 is : ",cuboid.area_cuboid(7,7,7))
print("Permeter of a cuboid with length,width,height 7 is : ",cuboid.perimeter_cuboid(7,7,7))

print("Area of a spere with radius 7 is : ",sphere.area_sphere(7))
print("Permeter of a spere with radius 7 is ",sphere.perimeter_sphere(7))
