# Python3 Program to
# Write a menu driven program for the following:
#  Area of a circle
#  Area of a rectangle
#  Area of a square
#  Area of trapezium

def area_circle(r):
    area_circle = 3.14 * r * r
    return area_circle


def area_rectangle(l, b):
    area_rectangle = l * b
    return area_rectangle


def area_square(s):
    area_square = s * s
    return area_square


def area_trapezium(a, b, h):
    area_trapezium = (a + b / 2) * h
    return area_trapezium


# area circle
print("AREA OF CIRCLE")
r = int(input("Enter radius of a circle:"))
num1 = 3.14 * r * r
print("Area of circle=", num1)

# area rectangle
print("AREA OF RECTANGLE")
l = int(input("Enter the length: "))
b = int(input("Enter the bredth: "))
num2 = l * b
print("area of rectangle=", num2)

# area square
print("AREA OF SQUARE")
s = int(input("Enter the side of the square: "))
num3 = s * s
print("Area of square= ", num3)

# area trapezium
print("AREA OF TRAPEZIUM")
a = int(input("Enter the 1st side: "))
b = int(input("Enter the 2nd side: "))
h = int(input("Enter the height: "))
num4 = (a + b / 2) * h
print("Area of Trapezium= ", num4)
