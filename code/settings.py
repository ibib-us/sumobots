# These settings affect the behaviors of your sumobot, such as how fast it moves and
#   how wide of an arc it searches.

MAX_SPEED = 0.8 # Ranges from 0 (doesn't move at all) to 1 (as fast as possible)
MAX_DISTANCE = 600

TURN_DURATION = 0.2 # Number of seconds that the bot spends turning. ***NOT CURRENTLY USED***

CHARGE_DURATION = 5 # Time to charge before giving up
CHARGE_TOLERANCE = 25 # Difference between TOF sensors that triggers a right/left shift

RETREAT_TIME = 1 # Time used in backing up and spinning during a retreat

AVOIDANCE_TIME = 2 # Time to spend during the edge avoidance movement. The slower the motors, the longer this needs to be.

TEST_TIME = 0.5 # Time to spend doing whatever is being done in the test state.

# NONE OF THE VALUES BELOW SHOULD BE CHANGED

WAITING_TIME = 5 # DO NOT CHANGE THIS VALUE! It is the time your bot waits to start battling and must be the same for all bots

LOG_LEVEL = 20 # Sets amount of logging. See below for values, but the way the code is currently written, must use numbers.
# Although not yet tested, setting the LOG_LEVEL to 99 should stop all logging and may speed up bot response
'''
LOG_NOTSET      =  0
LOG_DEBUG       = 10
LOG_INFO        = 20
LOG_WARNING     = 30
LOG_ERROR       = 40
LOG_CRITICAL    = 50
'''
