import random
import time
from time import sleep

from base_bot import SumoBotBase
from settings import *


class SimpleSumoBot(SumoBotBase):
    """
    An implementation of the sumo bot fighting routine.
    Other botmasters may define their own SumoBot classes which extend SumoBotBase,
    and add their own fight() method with their own personal fighting strategy.
    """

    def fight(self):
        """
        Robot fighting routine.
        """
        # *************************************
        # 1. Back away from the edge if needed
        # *************************************

        # If both sensors are over the edge, drive straight backwards.
        if self.left_edge_detected() and self.right_edge_detected():
            print("Backing straight up and turning around")
            self.drive(left_speed=-1, right_speed=-1, duration=0.3)
            self.drive(left_speed=-1, right_speed=1, duration=0.4)

        # If only the left sensor is over the edge, turn to the right,
        # then drive straight backwards.
        elif self.left_edge_detected():
            print("Backing to right and turning around")
            self.drive(left_speed=-0.5, right_speed=0.5, duration=0.25)
            self.drive(left_speed=-1, right_speed=-1, duration=0.3)
            self.drive(left_speed=-1, right_speed=1, duration=0.4)

        # If only the right sensor is over the edge, turn to the left,
        # then drive straight backwards.
        elif self.right_edge_detected():
            print("Backing to left and turning around")
            self.drive(left_speed=0.5, right_speed=-0.5, duration=0.25)
            self.drive(left_speed=-1, right_speed=-1, duration=0.3)
            self.drive(left_speed=1, right_speed=-1, duration=0.4)

        # ******************************
        # 2. Scan for opponent and charge it!
        # ******************************

        # Check for opponent straight ahead
        charge_time = 0
        if self.opponent_in_range_right() and self.opponent_in_range_left():
            # Charge!
            print("Charging boldly forward")
            charge_start_time = time.monotonic()
            self.drive(right_speed=MAX_SPEED, left_speed=MAX_SPEED)
            while (
                    self.opponent_in_range_right()
                    and self.opponent_in_range_left()
                    and not (self.right_edge_detected() or self.left_edge_detected())
                    and time.monotonic() - charge_start_time < MAX_CHARGE_TIME
            ):
                sleep(CHARGE_INTERVAL)
                charge_time += CHARGE_INTERVAL
            self.stop()
            if time.monotonic() - charge_start_time >= MAX_CHARGE_TIME:
                print("Backing up and turning away from opponent")
                if random.randint(0, 1):
                    self.drive(left_speed=-0.7, right_speed=-0.3, duration=BACK_AWAY_TIME)
                else:
                    self.drive(left_speed=-0.3, right_speed=-0.7, duration=BACK_AWAY_TIME)
        # Check for opponent to right
        else:
            right_distance = self.right_distance()
            left_distance = self.left_distance()
            if right_distance < MAX_DISTANCE:
                print("Looking right")
                # Turn to the right - set turn duration inversely proportional to opponent distance
                self.drive(left_speed=TURN_SPEED, right_speed=-TURN_SPEED, duration=0.2*((MAX_DISTANCE-right_distance)/MAX_DISTANCE))

            # Check for opponent to left
            elif left_distance < MAX_DISTANCE:
                print("Looking left")
                # Turn to the left - set turn duration inversely proportional to opponent distance
                self.drive(left_speed=-TURN_SPEED, right_speed=TURN_SPEED, duration=0.2*((MAX_DISTANCE-left_distance)/MAX_DISTANCE))

            # Spin and look for opponent
            else:
                # Turn to the left or right randomly
                print("Spinning")
                if random.randint(0,1):
                    self.drive(left_speed=-TURN_SPEED, right_speed=TURN_SPEED, duration=TURN_DURATION)
                else:
                    self.drive(left_speed=TURN_SPEED, right_speed=-TURN_SPEED, duration=TURN_DURATION)

if __name__ == "__main__":
    SimpleSumoBot().run()
