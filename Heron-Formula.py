import math
def area_triangle(x0, y0, x1, y1, x2, y2):

    a = math.sqrt((x1 - x0)**2 + (y1 - y0)**2)
    b = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    c = math.sqrt((x2 - x0)**2 + (y2 - y0)**2)

    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

x0 = int(input("x0 = "))
y0 = int(input("y0 = "))
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

result = area_triangle(x0, y0, x1, y1, x2, y2)
print(f"A triangle with vertices ({x0},{y0}), ({x1},{y1}), and ({x2},{y2}) has an area of {result:.1f}.")