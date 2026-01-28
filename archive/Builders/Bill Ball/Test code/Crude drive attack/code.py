# basic code for sumo bots, can be used to test your build
# reverse not working as of 2/14/2024
# pin assignments are at the end of this file
# Bill Ball bill@tinkerfarm.net

# import modules
# adafruit_vl53l0x.mpy must be on the board
import busio, time, pwmio
from board import *
import digitalio
from adafruit_vl53l0x import VL53L0X
from adafruit_motor import motor

#create motor objects and assign pins
# Initialize DC motors
m1a = pwmio.PWMOut(GP8, frequency=50)
m1b = pwmio.PWMOut(GP9, frequency=50)
motor1 = motor.DCMotor(m1a, m1b)
m2a = pwmio.PWMOut(GP10, frequency=50)
m2b = pwmio.PWMOut(GP11, frequency=50)
motor2 = motor.DCMotor(m2a, m2b)
# stop motors. throttle can be -1 to 1
motor1.throttle = 0  
motor2.throttle = 0

# create objects for edge detection and assign pins.
edgeL = digitalio.DigitalInOut(GP5)
edgeL.direction = digitalio.Direction.INPUT
edgeR = digitalio.DigitalInOut(GP26)
edgeR.direction = digitalio.Direction.INPUT

# setup the ToF sensors, one has to have address changed
# use pins on robot to create I2C
i2c1 = busio.I2C(GP3, GP2)
i2c2 = busio.I2C(GP17, GP16)
# shut down the I2C devices, low is off
xshutL = digitalio.DigitalInOut(GP4)
xshutL.direction = digitalio.Direction.OUTPUT
xshutL.value = False
xshutR = digitalio.DigitalInOut(GP6)
xshutR.direction = digitalio.Direction.OUTPUT
xshutR.value = False
# bring up the Right I2C its default value should be 41 (29 hex)
xshutR.value = True
#create ToF sensor using default address and then change it to 62 (3E hex)
ToFR = VL53L0X(i2c1, address=0x29)
ToFR.set_address(0x3E)
ToFR = VL53L0X(i2c1, address=0x3E)
# bring up the Left I2C
xshutL.value = True
# assign its default address to the other ToF sensor
ToFL = VL53L0X(i2c2, address=0x29)

# give yourself time to get your hands away
time.sleep(2)

# main driving loop
while True:
    #if the robot is at the white edge stop the motors
    # and back away -- except the back away part is not working
    if (edgeL.value == False) or (edgeR.value == False):
        motor1.throttle = 0  
        motor2.throttle = 0
        t_end = time.time() + 0.5
        while time.time() < t_end:
            motor1.throttle = -1  
            motor2.throttle = -1
        motor1.throttle = 0  
        motor2.throttle = 0
    
    # sample ToF sensors 2X and take highest reading to reduce spurious detects
    Right = max(ToFR.range, ToFR.range)
    Left = max(ToFL.range, ToFL.range)
    
    #target ahead -- go for it
    if Right < 770 and Left < 770:
        motor1.throttle = 1
        motor2.throttle = 1
    
    #target to left -- turn that way
    elif Right > 669 and Left < 770:
        motor1.throttle = .5
        motor2.throttle = 1
    
    #target to right  -- turn that way
    elif Right < 770 and Left > 669:
        motor1.throttle = 1
        motor2.throttle = .5   
    
    #no target so just spin in place looking for one
    elif Right > 769 and Left > 769:
        motor1.throttle = .5
        motor2.throttle = -.5    
    
    #otherwise just sit there like a dumb robot
    else:
        motor1.throttle = 0
        motor2.throttle = 0   


i2c1.unlock()
i2c1.deinit()
i2c2.unlock()
i2c2.deinit()

""" pin assignments for this code

Motor 1 is the left motor
Motor 2 is the right motor
If your robot does move in the direction you expect just
switch the wires going to MA and MB for that motor on the MakerPi board.

MakerPi connections to sensors (ToF is VL53L0X sensor):

Grove 2 
GND -> Right ToF GND
3V3 -> Right ToF VIN
GP2 -> Right ToF SDA
GP3 -> Right ToF SCL

Grove 3
GND -> Left edge detection GND
3V3 -> Left edge detection VIN
GP4 -> Left ToF XSHUT
GP5 -> Left IR DO

Grove 4
GND -> Left ToF GND 
3V3 -> Left ToF VCC
GP16 -> Left ToF SDA
GP17 -> Left ToF SCL

Grove 5
GND -> Right edge detection GND
3V3 -> Right edge detection VCC
GP6 -> Right ToF XSHUT 
GP26 -> Right IR DO

"""
