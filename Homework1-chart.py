#Nicholas Manfredi
#110207186
#CSE 101
#Lab Section 8
#Homework1-chart


from turtle import *
jack = Turtle()
screen = jack.getscreen()

#Get values from the user
rent = screen.numinput("How much for rent?",  "How much will you spend on rent? ")
utilities = screen.numinput("How much for utilities?", "How much will you spend on utilites?")
food = screen.numinput("How much for food?", "How much will you spend on food?")
fun = screen.numinput("How much for fun?", "How much will you spend on fun?")
largest = max(rent, utilities, food, fun)

#Set colors and decide what bar should be red (the largest)
rentColor = "blue"
foodColor = "blue"
funColor = "blue"
utilitiesColor = "blue"

if largest == rent:
    rentColor = "red"
elif largest == food:
    foodColor = "red"
elif largest == fun:
    funColor = "red"
else:
    utilitiesColor = "red"

#Rent
#Label the bar as "Rent"
jack.penup()
jack.goto(0, -20)
jack.write("Rent")
jack.goto(0,0)
#Set the pen back down and set the fill color to rentColor
jack.pendown()
jack.fillcolor(rentColor)
#Begin filling
jack.begin_fill()
#***Making the Rectangle***#
jack.forward(50) #Width is 50
jack.left(90)
jack.forward(rent) #Height is going to be based on the height the user entered
jack.left(90)
jack.forward(50)
jack.left(90)
jack.forward(rent)
jack.left(90)
jack.forward(50)
#***End making the Rectangle***#
#Pick the pen up and end filling
jack.up()
jack.end_fill()
jack.goto(0, rent+20)
jack.write("$"+str(rent))
jack.goto(50,0)

#Move to the right by 20 to begin the next bar
jack.forward(20)

#Food

#Label the bar as "Food"
jack.penup()
jack.goto(100, -20)
jack.write("Food")
jack.goto(100,0)
#Set the pen back down and set the fill color to rentColor
jack.pendown()
jack.fillcolor(foodColor)
#Begin filling
jack.begin_fill()
#***Making the Rectangle***#
jack.forward(50) #Width is 50
jack.left(90)
jack.forward(food) #Height is going to be based on the height the user entered
jack.left(90)
jack.forward(50)
jack.left(90)
jack.forward(food)
jack.left(90)
jack.forward(50)
#***End making the Rectangle***#
#Pick the pen up and end filling
jack.up()
jack.end_fill()
jack.goto(100, food+20)
jack.write("$"+str(food))
jack.goto(100,0)

#Move to the right by 20 to begin the next bar
jack.forward(20)

#Label the bar as "Rent"
jack.penup()
jack.goto(200, -20)
jack.write("Utilities")
jack.goto(200,0)
#Set the pen back down and set the fill color to rentColor
jack.pendown()
jack.fillcolor(utilitiesColor)
#Begin filling
jack.begin_fill()
#***Making the Rectangle***#
jack.forward(50) #Width is 50
jack.left(90)
jack.forward(utilities) #Height is going to be based on the height the user entered
jack.left(90)
jack.forward(50)
jack.left(90)
jack.forward(utilities)
jack.left(90)
jack.forward(50)
#***End making the Rectangle***#
#Pick the pen up and end filling
jack.up()
jack.end_fill()
jack.goto(200, utilities+20)
jack.write("$"+str(utilities))
jack.goto(200,0)

#Move to the right by 20 to begin the next bar
jack.forward(20)

#Label the bar as "Rent"
jack.penup()
jack.goto(-100, -20)
jack.write("Fun")
jack.goto(-100,0)
#Set the pen back down and set the fill color to rentColor
jack.pendown()
jack.fillcolor(funColor)
#Begin filling
jack.begin_fill()
#***Making the Rectangle***#
jack.forward(50) #Width is 50
jack.left(90)
jack.forward(fun) #Height is going to be based on the height the user entered
jack.left(90)
jack.forward(50)
jack.left(90)
jack.forward(fun)
jack.left(90)
jack.forward(50)
#***End making the Rectangle***#
#Pick the pen up and end filling
jack.up()
jack.end_fill()
jack.goto(-100, fun+20)
jack.write("$"+str(fun))
jack.goto(-100,0)


jack.penup()
jack.goto(60,200)
jack.write("Monthly Expenses")

