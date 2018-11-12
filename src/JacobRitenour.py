"""
  Capstone Project.  Code written by Jacob Ritenour.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import ev3dev.ev3 as ev3
import time


def main():
    """ Runs YOUR specific part of the project """
    #test_color_sensor()
    #test_proximity_sensor()
    test_beacon_buttons()

def test_color_sensor():
    """Test for the robot's color sensor"""
    robot=rb.Snatch3rRobot()
    robot.drive_system.start_moving(20,20)
    robot.color_sensor.wait_until_color_is(2)
    robot.drive_system.stop_moving()


def test_proximity_sensor():
    """Test for the robot's proximity sensor"""
    robot = rb.Snatch3rRobot()
    print(1)
    while (True):
        if (robot.proximity_sensor.get_distance_to_nearest_object_in_inches() < 15):
            ev3.Sound.beep().wait()

def test_beacon_buttons():
    """Test for the robot responding to the beacon buttons"""
    robot = rb.Snatch3rRobot()
    while (True):
        if robot.beacon_button_sensor.is_top_red_button_pressed()==True:
            robot.drive_system.start_moving(50,50)

        if robot.beacon_button_sensor.is_bottom_red_button_pressed()==True:
            ev3.Sound.speak('hello')

        if robot.beacon_button_sensor.is_top_blue_button_pressed()==True:
            robot.arm.calibrate()

        if robot.beacon_button_sensor.is_bottom_blue_button_pressed()==True:
            robot.drive_system.stop_moving()
main()
