"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    robot.touch_sensor.wait_until_released()
    print('yes')

robot = rb.Snatch3rRobot()
robot.raise_arm_and_close_claw()
