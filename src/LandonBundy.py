"""
  Capstone Project.  Code written by Landon Bundy.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def test_raise_arm():
    robot = rb.Snatch3rRobot()
    robot.arm.raise_arm_and_close_claw()
    print('raised')


def test_calibrate():
    robot = rb.Snatch3rRobot()
    robot.arm.calibrate()
    print('calibrated')


def test_move_arm():
    robot = rb.Snatch3rRobot()
    robot.arm.move_arm_to_position(4)
    print('moved')


def test_ellipse():
    robot = rb.Snatch3rRobot()
    while True:
        if robot.color_sensor.get_reflected_intensity() <= 5:
            robot.drive_system.start_moving(50, 50)
            robot.drive_system.right_wheel.reset_degrees_spun(0)
        elif robot.color_sensor.get_reflected_intensity() > 5:
            robot.drive_system.turn_degrees(2, 100)
            robot.drive_system.start_moving(10, 10)
            robot.drive_system.right_wheel.reset_degrees_spun(0)


def main():
    #test_raise_arm()
    test_calibrate()
    #test_ellipse()


main()


def move_item():
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving()
    robot.color_sensor.wait_until_color_is(1)
    robot.drive_system.stop_moving()
    robot.arm.raise_arm_and_close_claw()
    robot.drive_system.turn_degrees(90)
    robot.arm.calibrate()
    robot.drive_system.turn_degrees(-90)
    robot.drive_system.start_moving()
    robot.color_sensor.wait_until_color_is(6)
    robot.drive_system.stop_moving()


def drive_to_green():
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving()
    robot.touch_sensor.wait_until_pressed()
    while True:
        robot.drive_system.spin_in_place_degrees(360)
        robot.color_sensor.wait_until_color_is(1)
        while True:
            robot.drive_system.stop_moving()
            robot.arm.raise_arm_and_close_claw()
            robot.arm.calibrate()
            print('Stopped for the color green')
            break
        break
