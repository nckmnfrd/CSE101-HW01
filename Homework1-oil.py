#Nicholas Manfredi
#110207186
#CSE 101
#Lab Section: 8
#Homework 1


import math

flow_rate = int(input('Enter the flow rate liters per minute: '))

radius = int(input('Enter the radius of drum in inches: '))

height = int(input('Enter the height of the drum: '))

Volume = (math.pi)*(height)*(radius**2)

Volume*= 0.0163871

hours = Volume / (flow_rate*60)
minutes = (hours % 1) * 60
seconds = (minutes % 1) * 60
print("Time to fill barrel: ",int(hours),"hour(s),",int(minutes),"minute(s) and",int(seconds),"second(s)")
