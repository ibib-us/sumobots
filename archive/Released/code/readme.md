# Sumo Bot

# Software
There are four files that are needed for your sumobot to run:

- `base_bot.py` contains the startup, searching, turning, and charging routines, along with some utility functions
- `code.py` is the main program that includes the fight sequence and the routine to start fighting
- `settings.py` contains parameters you can change to customize the fighting style of your sumobot
- `adafruit_vl5310x.mpy` is a special library to allow the time of flight (distance) sensor to operate properly

# Downloading the correct driver for the distance sensor

The sensor library you download depends on the version of CircuitPython you are running. The version can be found by looking at the `boot_out.txt` file on your sumobot. It will look something like this:

>Adafruit CircuitPython 7.1.0 on 2021-12-28; Cytron Maker Pi RP2040 with rp2040
>Board ID:cytron_maker_pi_rp2040

Since this sumobot is running version 7, it requires the version 7 library. However, Adafruit no longer supports this version, and it is recommended we upgrade to the latest (which is 9 at the moment). Here are the steps:

- Head to CircuitPython.org and download the `.UF2` file for the microcontroller. The direct link is [here](https://circuitpython.org/board/cytron_maker_pi_rp2040/).
- Find the `RST` button on your MakerPi2040 and double click it. You will now see that the CIRCUITPY drive on your computer disappears and is replaced by RPI-RP2.
- Copy the `.UF2` file that you downloaded onto this drive. Once completed, the RPI-RP2 drive will disappear
- Head over to the [Libraries](https://circuitpython.org/libraries) section and download the appropriate bundle, which is currently version 9.

## Initial setup
Open `settings.py` and review the "Robot hardware settings" section. Change any pin values if your hardware is connected differently than the default settings.


## Installation instructions
Make a backup copy of the code.py file that cam on your MakerPi board.
Copy the files `base-bot.py`, `code.py`, `adafruit_vl53l0x.mpy`, and `settings.py` to your MakerPi to get a working sumo bot.

## How to use
Turn on your MakerPi. To start a bout hold down the GP20 button until the light turns yellow. Your bot is now armed. Release the button to start the bout after a 5 second delay.
See the rules document for more detail on how Sumo bot matches operate.
Turn on your Maker Pi and press buttons until you find the one that turns the lights from red to yellow. Your bot is now armed. Release the button to enter FIGHT MODE!


## How to customize
Change values in the "Settings that control fight mode parameters" section of `settings.py` to make adjustments to your robot's fighting strategy.

## Advanced customization
Modify the `fight()` method in code.py to change your robot's fighting strategy.

## File descriptions 
* `settings.py` contains hardware pin assignments and basic behavior settings
* `code.py` defines the `fight()` method which determines the robot's logic while in fight mode.
* `base_bot.py` contains the main class which defines the fundamental methods for robot control such as moving and detecting enemies.
* `adafruit_Vl530x.mpy` is the driver for the time of flight sensors. The robot code won't work without it installed on the MakerPi.
* `original_code.py` is the default demo program that shipped with the MakerPI RP2040. It's not needed for the robot to work.
