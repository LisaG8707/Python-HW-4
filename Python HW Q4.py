from graphics import *

win = GraphWin("Logistic Function", 600, 500)

# Draw x-axis and y-axis
xAxis = Line(Point(50, 450), Point(550, 450))
xAxis.draw(win)

yAxis = Line(Point(50, 450), Point(50, 50))
yAxis.draw(win)

# Starting value
x = float(input("Enter the starting value: "))
k = float(input("Enter the value of k: "))

# Plot 100 values
previousPoint = None

for i in range(100):
    x = k * x * (1 - x)

    graphX = 50 + i * 5
    graphY = 450 - x * 400

    point = Point(graphX, graphY)
    point.draw(win)

    if previousPoint != None:
        line = Line(previousPoint, point)
        line.draw(win)

    previousPoint = point

win.getMouse()
win.close()

