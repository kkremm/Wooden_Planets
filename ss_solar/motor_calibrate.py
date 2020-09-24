"""for calibration (align on a line the right of the star)"""

"""kerem yazici"""

from adafruit_motorkit import MotorKit
from time import sleep

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

mot_Mercury.throttle = None
mot_Venus.throttle = None
mot_Earth.throttle = None
mot_Mars.throttle = None
mot_Jupiter.throttle = None
mot_Saturn.throttle = None

mot_Uranus.throttle = None
mot_Neptune.throttle = None

print('60" for calibration')
time.sleep(60)

mot_Mercury.throttle = 0
mot_Venus.throttle = 0
mot_Earth.throttle = 0
mot_Mars.throttle = 0
mot_Jupiter.throttle = 0
mot_Saturn.throttle = 0
mot_Uranus.throttle = 0
mot_Neptune.throttle = 0

print('calibration complete')
