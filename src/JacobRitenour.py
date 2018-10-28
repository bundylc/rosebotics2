"""
  Capstone Project.  Code written by Jacob Ritenour.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    robot.color_sensor.wait_until_intensity_is_greater_than(10)
    print(1)

main()
