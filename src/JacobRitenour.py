"""
  Capstone Project.  Code written by Jacob Ritenour.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import ev3dev.ev3 as ev3
import time


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    while(robot.proximity_sensor.get_distance_to_nearest_object_in_inches()<15):
        ev3.Sound.beep().wait()
    print(1)

main()
