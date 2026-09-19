from graphics import *
import math

n = int(input("Enter the number of sides: "))
radius = float(input("Enter the radius: "))

win = GraphWin("Regular Polygon", 500, 500, autoflush=True)
win.setBackground("white")

centerX = 250
centerY = 250

angle = 360 / n
vertices = []
for i in range(n):
    theta = math.radians(i * angle)
    x = centerX + radius * math.cos(theta)
    y = centerY + radius * math.sin(theta)
    vertices.append(Point(x, y))

polygon = Polygon(vertices)
polygon.setOutline("black")
polygon.setWidth(3)
polygon.draw(win)

win.getMouse()
win.close()
