"""http://stjarnhimlen.se/comp/tutorial.html"""

"""position of the planets and how they will evolve, its gets its data from solar_system_live"""

"""kerem yazici"""

import turtle
import math
import solar_system_live as ssl
import time

def orbit(radius, angle):
    x = math.cos(math.radians(angle))*radius
    y = math.sin(math.radians(angle))*radius
    return (x, y)

amp = 35
speed = 0

wn = turtle.Screen()
wn.title("solar system live")
wn.bgcolor('midnight blue')

sun = turtle.Turtle()
sun.shape("circle")
sun.color("black")
sun.goto(x=0, y=0 )

#orbits
circle_mercury = turtle.Turtle()
circle_mercury.speed(speed)
circle_mercury.color("grey")
circle_mercury.hideturtle()
circle_mercury.penup()
circle_mercury.goto(0, -1*amp)
circle_mercury.pendown()
circle_mercury.circle(1*amp)

circle_venus = turtle.Turtle()
circle_venus.speed(speed)
circle_venus.color("orange")
circle_venus.hideturtle()
circle_venus.penup()
circle_venus.goto(0, -2*amp)
circle_venus.pendown()
circle_venus.circle(2*amp)

circle_earth = turtle.Turtle()
circle_earth.speed(speed)
circle_earth.color("deep sky blue")
circle_earth.hideturtle()
circle_earth.penup()
circle_earth.goto(0, -3*amp)
circle_earth.pendown()
circle_earth.circle(3*amp)

circle_mars = turtle.Turtle()
circle_mars.speed(speed)
circle_mars.color("red")
circle_mars.hideturtle()
circle_mars.penup()
circle_mars.goto(0, -4*amp)
circle_mars.pendown()
circle_mars.circle(4*amp)

#--asteroids

circle_jupiter = turtle.Turtle()
circle_jupiter.speed(speed)
circle_jupiter.color("pink")
circle_jupiter.hideturtle()
circle_jupiter.penup()
circle_jupiter.goto(0, -6*amp)
circle_jupiter.pendown()
circle_jupiter.circle(6*amp)

circle_saturn = turtle.Turtle()
circle_saturn.speed(speed)
circle_saturn.color("yellow")
circle_saturn.hideturtle()
circle_saturn.penup()
circle_saturn.goto(0, -7*amp)
circle_saturn.pendown()
circle_saturn.circle(7*amp)

circle_uranus = turtle.Turtle()
circle_uranus.speed(speed)
circle_uranus.color("cyan")
circle_uranus.hideturtle()
circle_uranus.penup()
circle_uranus.goto(0, -8*amp)
circle_uranus.pendown()
circle_uranus.circle(8*amp)

circle_neptune = turtle.Turtle()
circle_neptune.speed(speed)
circle_neptune.color("blue")
circle_neptune.hideturtle()
circle_neptune.penup()
circle_neptune.goto(0, -9*amp)
circle_neptune.pendown()
circle_neptune.circle(9*amp)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("light grey")
pen.penup()
pen.hideturtle()
pen.goto(0, 210)

#planets
mercury = turtle.Turtle()
mercury.shape("circle")
mercury.color("grey")
mercury.speed(speed)
mercury.penup()

venus = turtle.Turtle()
venus.speed(speed)
venus.shape("circle")
venus.color("orange")
venus.penup()

earth = turtle.Turtle()
earth.shape("circle")
earth.color("deep sky blue")
earth.speed(speed)
earth.penup()

mars = turtle.Turtle()
mars.speed(speed)
mars.shape("circle")
mars.color("red")
mars.penup()

#--asteroids

jupiter = turtle.Turtle()
jupiter.speed(speed)
jupiter.shape("circle")
jupiter.color("pink")
jupiter.penup()

saturn = turtle.Turtle()
saturn.speed(speed)
saturn.shape("circle")
saturn.color("yellow")
saturn.penup()

uranus = turtle.Turtle()
uranus.speed(speed)
uranus.shape("circle")
uranus.color("cyan")
uranus.penup()

neptune = turtle.Turtle()
neptune.speed(speed)
neptune.shape("circle")
neptune.color("blue")
neptune.penup()

while True:

    wn.update()

    pen.clear()
    pen.write("date: {}   timepass: {} days /{} sec".format(ssl.day.date_count, ssl.time_pass, ssl.delay), align="center", font=("Avenir", 24, "normal"))

    mercury.goto(orbit(1*amp, ssl.day.Mercury_long))
    venus.goto(orbit(2*amp, ssl.day.Venus_long))
    earth.goto(orbit(3*amp, ssl.day.Earth_RA +180))
    mars.goto(orbit(4*amp, ssl.day.Mars_long))
    jupiter.goto(orbit(6*amp, ssl.day.Jupiter_long))
    saturn.goto(orbit(7*amp, ssl.day.Saturn_long))
    uranus.goto(orbit(8*amp, ssl.day.Uranus_long))
    neptune.goto(orbit(9*amp, ssl.day.Neptune_long))

    time.sleep(0.25)


turtle.done()
