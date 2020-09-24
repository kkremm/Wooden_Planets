"""moves all motors simultaniously, data from solar_system, live speed"""

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

def sort_dict(dict):
	return sorted(dict.items() , reverse=True, key=lambda x: x[1])

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

circumference_Gear = cir(1) #insert circumference of gear

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

count=1
while True:

    planets_positions_dict = {'mercury' : 0,
                        'venus' : 0,
                        'earth' : 0,
                        'mars' : 0,
                        'jupiter' : 0,
                        'saturn' : 0,
                        'uranus' : 0,
                        'neptune' : 0}

    name_to_class = {'mercury' : Mercury,
                        'venus' : Venus,
                        'earth' : Earth,
                        'mars' : Mars,
                        'jupiter' : Jupiter,
                        'saturn' : Saturn,
                        'uranus' : Uranus,
                        'neptune' : Neptune}

    planet_name_sorted = []
    planet_sleeptime_sorted = []
    planet_sleeptime_sorted_sub = []

    for Planet in planet_names:

        Planet.update_sleeptime()

        planets_positions_dict[Planet.name.lower()] = Planet.sleeptime
        Planet.last_position = Planet.current_position

    for p in range(8):
        planet_name_sorted.append( sort_dict(planets_positions_dict)[p][0] )

        planet_sleeptime_sorted.append( sort_dict(planets_positions_dict)[p][1] )

    for i in range(8):
        if i < 7:
            planet_sleeptime_sorted_sub.append( planet_sleeptime_sorted[i] - planet_sleeptime_sorted[i+1] )
        elif i ==7:
            planet_sleeptime_sorted_sub.append( planet_sleeptime_sorted[i])

    planet_sleeptime_sorted_sub.reverse()
    planet_name_sorted.reverse()
    planet_sleeptime_sorted.reverse()

    for planet_1 in planet_name_sorted:
        planet_class = name_to_class[planet_1]

        planet_class.motor.throttle = 1

    for wsh in range(8):
        time.sleep(planet_sleeptime_sorted_sub[wsh])
        name_to_class[planet_name_sorted[wsh]].motor.throttle = 0
        print(str(planet_name_sorted[wsh]))


    print(planet_name_sorted)
    print(planet_sleeptime_sorted)
    print(planet_sleeptime_sorted_sub)

    print('end of check '+ str(count))
    time.sleep(refresh)
    count+=1
