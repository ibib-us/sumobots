# IBiB Sumobot Design Rules

## I. General Specification

### A. Robot Classes

1. 2040b
    1. Must fit within a 10 cm by 10 cm square tube, with no height restriction.
    2. Maximum weight: 500 grams.
    3. Powered by no more than 6 volts.
    4. Must use the Maker Pi RP2040 development board as the microcontroller.
    5. Only the VL53L0X time of flight sensor and TCRT5000 reflectance sensor are allowed.
    6. Only two N20 metal gear DC motors are allowed.
    7. Must be programmed using CircuitPython.
2. 2040b+
    1. The 2040b+ class follows all the rules of the 2040b class except where specifically noted.
    2. No restrictions on the type and number of sensors.
    3. No restriction on the type and number of motors.

## B. Autonomy

1. All robots must be autonomous.
2. Any method of onboard control may be used, as long as it is fully contained within the robot and receives no external signals or directions (human, machine, or otherwise).
3. Autonomous robot operation must begin within the start procedure indicated for the event and robot class.

## C. Identification

1. Robots must have a name or number for registration purposes.
2. Robots must be clearly identifyable by their name and/or number.

## II. Restrictions

### A. Prohibited Devices and Materials

1. Jamming devices, such as IR LEDs intended to saturate the opponent's IR sensors, are not allowed.
2. Parts that could break or damage the event area are not allowed.
3. Parts intended to damage the opponent’s robot or its operator are not allowed. 
4. Parts intended to damage or alter the event area are not allowed.
5. Devices that can store liquid, powder, gas, or other substances for throwing at the opponent are not allowed.
6. Flaming devices are not allowed.
7. Devices that throw things are not allowed.
8. Sticky substances to improve traction are not allowed.
    1. Tires and other components of the robot in contact with the event area must not be able to pick up and hold a standard 3"x5" index card for more than two seconds.
    2. Devices to increase downforce, such as a vacuum pump or magnets, are not allowed.
9. All edges, including but not limited to the front scoop, must not be sharp enough to scratch or damage the ring, other robots, or players. Edges with a radius greater than 0.005", as would be obtained with an unsharpened 0.010" thick metal strip, should be acceptable. Judges or competition officials may require edges deemed too sharp to be covered with tape.

### B. Exceptions to restrictions

1. Restrictions mentioned in this section may be superceded by the event rules.
2. The judge or referee overseeing an event has final say on the interpretation of these restrictions.
