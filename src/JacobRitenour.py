"""
  Capstone Project.  Code written by Jacob Ritenour.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import ev3dev.ev3 as ev3
import time


def main():
    """ Runs YOUR specific part of the project """
    test_color_sensor()
    test_proximity_sensor()

def test_color_sensor():
    """Test for the robot's color sensor"""
    robot=rb.Snatch3rRobot()
    robot.drive_system.start_moving(20,20)
    if(robot.color_sensor.get_color()=='red'):
        robot.drive_system.stop_moving()

def test_proximity_sensor():
    """Test for the robot's proximity sensor"""
    robot = rb.Snatch3rRobot()
    print(1)
    while (True):
        if (robot.proximity_sensor.get_distance_to_nearest_object_in_inches() < 10):
            ev3.Sound.beep().wait()


main()
