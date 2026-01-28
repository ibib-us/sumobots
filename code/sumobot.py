from settings import * # Gets the custom settings
import board # pin identification information
import digitalio # for various digital IO operations
import analogio # for the battery monitor
from adafruit_vl53l0x import VL53L0X # for the TOF sensors
import busio # for I2C communication with TOF sensor
from time import sleep, monotonic
import keypad # To handle keypresses nicely
from adafruit_motor.motor import DCMotor # for DC motors
import pwmio # To adjust speeds
import neopixel
import simpleio

##################################################
# Robot hardware settings
# Change these if your robot is wired differently
# than the instructions.
##################################################


# Pin connected to piezo buzzer
PIEZO_PIN = board.GP22

# Pins connected to DC motors (swap variable names if your motors are connected differently)
RIGHT_MOTOR_PIN_B = board.GP11
RIGHT_MOTOR_PIN_A = board.GP10
LEFT_MOTOR_PIN_A = board.GP8
LEFT_MOTOR_PIN_B = board.GP9

# Pin connected to NeoPixels
NEO_PIXEL_PIN = board.GP18

# Pins connected to buttons
BUTTON_1_PIN = board.GP20
BUTTON_2_PIN = board.GP21

# Pins connected to TOF sensors
LEFT_EDGE_SENSOR_PIN = board.GP5
RIGHT_EDGE_SENSOR_PIN = board.GP26
TOF_LEFT_I2C_PINS = (board.GP17, board.GP16)
TOF_RIGHT_I2C_PINS = (board.GP3, board.GP2)
I2C_RIGHT_TOGGLE_PIN = board.GP4
I2C_LEFT_TOGGLE_PIN = board.GP6

# Pin for battery voltage reference path NOT IMPLEMENTED YET
BATTERY_VOLTAGE_PIN = board.A3
# Low battery threshold voltage
BATTERY_VOLTAGE_THRESHOLD = 52500

# Initialize battery
battery = analogio.AnalogIn(BATTERY_VOLTAGE_PIN)

# Initialize the motors operating the two wheels
motor_right = DCMotor(
    pwmio.PWMOut(RIGHT_MOTOR_PIN_A, frequency=50),
    pwmio.PWMOut(RIGHT_MOTOR_PIN_B, frequency=50),
)
motor_left = DCMotor(
    pwmio.PWMOut(LEFT_MOTOR_PIN_A, frequency=50),
    pwmio.PWMOut(LEFT_MOTOR_PIN_B, frequency=50),
)


# Utility to log events to the serial monitor

# Define logging levels - based on the logging library
LOG_NOTSET      =  0
LOG_DEBUG       = 10
LOG_INFO        = 20
LOG_WARNING     = 30
LOG_ERROR       = 40
LOG_CRITICAL    = 50

# User sets LOG_LEVEL in settings.py

def log(message, level = LOG_NOTSET):
    '''
    message: the message to log
    mlevel : the level of the message (integer)
    '''
    if level >= LOG_LEVEL:
        print(f'({level}-{monotonic()}): {message}')


# Sumobot movements
# Tuples are assigned based upon looking in the same direction as the bot, so (1, -1) drives the
# left wheel forward and the right wheel backwards. Note this will cause confusion on which wheel is
# actually on the right or left side. Either update wiring or generalize motor naming.

FORWARD = (1, 1)
BACKWARD = (-1,-1)
HARD_RIGHT = (-1,1)
HARD_LEFT = (1,-1)
RIGHT = (0,1)
LEFT = (1,0)
BACK_LEFT = (-1, 0)
BACK_RIGHT = (0, -1)
STOP = (0, 0)

def move(direction):
    '''
    Sets the motor throttles for the given direction. Naming convention needs to be reviewed.
    Should consider a second argument to provide fine control of wheel speed (for turning)
    '''
    motor_right.throttle = direction[0] * MAX_SPEED

    motor_left.throttle = direction[1] * MAX_SPEED
    log(f'Motors activated ({motor_left.throttle},{motor_right.throttle})', LOG_DEBUG)

def buzz():
    '''
    Creates the starting sound
    '''
    simpleio.tone(pin=PIEZO_PIN, frequency=523.25, duration=0.3)

# We create a class for the TOF sensor because we need to incorporate signal averaging and an offset.
class TOF():
    '''
    Initializes a TOF sensor, allows for some corrections such as an offset, and allows for some signal averaging
    '''
    def __init__(self, address, pins, toggle, offset = 0):
        self.address = address
        self.offset = offset
        self.i2c = busio.I2C(*pins)
        self.toggle = digitalio.DigitalInOut(toggle)
        self.toggle.direction = digitalio.Direction.OUTPUT
        self.toggle.value = False
        self.tof = None
        self.number_measurements = 1


    def initialize(self):
        '''
        Cannot initialize until all of the other sensor i2c addresses have been set up. Not sure why
        '''
        self.toggle.value = True
        self.tof = VL53L0X(self.i2c)
        self.tof.set_address(self.address)


    def distance(self):
        sum = 0
        for i in range(self.number_measurements):
            sum = sum + self.tof.range + self.offset
        return int(sum / (self.number_measurements))

tof_left = TOF(address = 0x3E, pins = TOF_LEFT_I2C_PINS, toggle = I2C_LEFT_TOGGLE_PIN)
tof_right = TOF(address = 0x29, pins = TOF_RIGHT_I2C_PINS, toggle = I2C_RIGHT_TOGGLE_PIN )
# This is stupid, but it looks like we have to try and fail once.
try:
    tof_left.initialize()
except ValueError:
    log('odd ValueError ... working around it.', LOG_DEBUG)
finally:
    tof_right.initialize()
    tof_left.initialize()

# Set up edge detectors
edge_left = digitalio.DigitalInOut(LEFT_EDGE_SENSOR_PIN)
edge_left.direction = digitalio.Direction.INPUT
edge_right = digitalio.DigitalInOut(RIGHT_EDGE_SENSOR_PIN)
edge_right.direction = digitalio.Direction.INPUT

# Set up keypad (two keys at the moment)
keypad = keypad.Keys(
    (BUTTON_1_PIN, BUTTON_2_PIN), value_when_pressed=False, pull=True
)

# Utility function to grab all of the conditions (edge detector, distances, buttons)
def get_conditions():
    '''
    Returns a dictionary of conditions
    '''
    condition_dict = {
        "edge_left": not edge_left.value,
        "edge_right": not edge_right.value,
        "tof_left": tof_left.distance(),
        "tof_right": tof_right.distance(),
        "key_events": keypad.events.get(),
        }
    condition_dict["tof_diff"] = condition_dict["tof_left"] - condition_dict["tof_right"]

    return condition_dict

# Utility function to send messages as beeps
def dit(num):
    '''
    Creates a dit
    '''
    for i in range(num):
        simpleio.tone(pin=PIEZO_PIN, frequency=523.25, duration=0.01)
        sleep(0.01)


# Initialize pixels
pixels = neopixel.NeoPixel(NEO_PIXEL_PIN, 2, brightness=0.1)
pixels.fill(0)
