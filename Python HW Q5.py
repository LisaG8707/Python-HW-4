from graphics import *

win = GraphWin("Logistic Function", 600, 500)

# Draw x-axis and y-axis
xAxis = Line(Point(50, 450), Point(550, 450))
xAxis.draw(win)

yAxis = Line(Point(50, 450), Point(50, 50))
yAxis.draw(win)

# Starting value
Text(Point(150, 50), "Starting value:").draw(win)
xEntry = Entry(Point(250, 50), 10)
xEntry.draw(win)

Text(Point(150, 80), "Value of k:").draw(win)
kEntry = Entry(Point(250, 80), 10)
kEntry.draw(win)

button = Rectangle(Point(275, 100), Point(375, 140))
button.draw(win)

buttonLabel = Text(Point(325, 120), "Graph")
buttonLabel.draw(win)

win.getMouse()

x = float(xEntry.getText())
k = float(kEntry.getText())

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

buttonLabel.setText("Exit")

win.getMouse()
win.close()



