"""moves motors one by one, data from solar_system, live speed"""

"""kerem yazici"""

import time
import solar_system as ss
from adafruit_motorkit import MotorKit

refresh = 300 #seconds between checks

def rev(x):
    if x >= 360 or x < 0:
        return x%360
    elif x >= 0:
        return x

def cir(x):
    return 3.141592*2*x

kitA = MotorKit(address=0x60)
kitB = MotorKit(address=0x61)

mot_Mercury = kitA.motor1
mot_Venus = kitA.motor2
mot_Earth = kitA.motor3
mot_Mars = kitA.motor4
mot_Jupiter = kitB.motor1
mot_Saturn = kitB.motor2
mot_Uranus = kitB.motor3
mot_Neptune = kitB.motor4

circumference_Gear = cir(1) #?

def num_of_steps(last_position, current_position):
    if last_position < current_position:
        return current_position-last_position
    elif last_position > current_position:
        return 360-last_position+current_position
    elif round(last_position, 1) == round(current_position, 1):
        return 0

class Planet:

    def __init__(self, name, circumference, motor, last_position, current_position, rps, sleeptime):
        self.name = name
        self.circumference = circumference
        self.motor = motor
        self.last_position = last_position
        self.current_position = current_position
        self.rps = rps
        self.sleeptime = sleeptime

    def update_sleeptime(self):
        self.sleeptime = round( float((1/self.rps) * (self.circumference/circumference_Gear) * (num_of_steps(self.last_position, self.current_position) /360)), 3)


Mercury = Planet ("Mercury", #name
                    cir(4), #circumference
                    mot_Mercury,
                    0, #last_position
                    round(ss.Mercury.long, 1), #current_position
                    1, #rps
                    0) #sleeptime

Venus = Planet ("Venus", #name
                    cir(7), #circumference
                    mot_Venus,
                    0, #last_position
                    round(ss.Venus.long, 1), #current_position
                    1, #rps
                    0) #sleeptime

Earth = Planet ("Earth", #name
                    cir(10), #circumference
                    mot_Earth,
                    0, #last_position
                    round(ss.Earth.RA + 180, 1), #current_position
                    1, #rps
                    0) #sleeptime

Mars = Planet ("Mars", #name
                    cir(13), #circumference
                    mot_Mars,
                    0, #last_position
                    round(ss.Mars.long, 1), #current_position
                    1, #rps
                    0) #sleeptime

Jupiter = Planet ("Jupiter", #name
                    cir(16), #circumference
                    mot_Jupiter,
                    0, #last_position
                    round(ss.Jupiter.long, 1), #current_position
                    1, #rps
                    0) #sleeptime

Saturn = Planet ("Saturn", #name
                    cir(19), #circumference
                    mot_Saturn,
                    0, #last_position
                    round(ss.Saturn.long, 1), #current_position
                    1, #rps
                    0) #sleeptime

Uranus = Planet ("Uranus", #name
                    cir(22), #circumference
                    mot_Uranus,
                    0, #last_position
                    round(ss.Uranus.long, 1), #current_position
                    1, #rps
                    0) #sleeptime

Neptune = Planet ("Neptune", #name
                    cir(25), #circumference
                    mot_Neptune,
                    0, #last_position
                    round(ss.Neptune.long, 1), #current_position
                    1, #rps
                    0) #sleeptime

planet_names = [Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune]

count = 1
for i in range(3): #while True:

    for Planet in planet_names:

        Planet.update_sleeptime()
        print(Planet.sleeptime)

        Planet.motor.throttle = 1
        time.sleep(Planet.sleeptime)
        Planet.motor.throttle = 0

        Planet.last_position = Planet.current_position


    print('\n')
    print('end of check '+ str(count))
    time.sleep(refresh)
    count+=1
