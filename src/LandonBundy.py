"""
  Capstone Project.  Code written by Landon Bundy.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    drive_to_green()
    move_item()


main()


def move_item():
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving()
    robot.color_sensor.wait_until_color_is(5)
    robot.drive_system.stop_moving()
    robot.arm.raise_arm_and_close_claw()
    robot.drive_system.turn_degrees(90)
    robot.arm.calibrate()
    robot.drive_system.turn_degrees(-90)
    robot.drive_system.start_moving()
    robot.color_sensor.wait_until_color_is(3)
    robot.drive_system.stop_moving()


def drive_to_green():
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving()
    robot.touch_sensor.wait_until_pressed()
    while True:
        robot.drive_system.spin_in_place_degrees(360)
        robot.color_sensor.wait_until_color_is(3)
        while True:
            robot.drive_system.stop_moving()
            robot.arm.raise_arm_and_close_claw()
            robot.arm.calibrate()
            print('Stopped for the color green')
            break
        break
