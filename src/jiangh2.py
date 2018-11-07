"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time
import ev3dev.ev3 as ev3


def main():
    """ Runs YOUR specific part of the project """
    #run_test_drive_system()
    #run_test_polygon(10)
    #run_test_ellipse()
    #run_and_stop(2)
    #camera_sense()
    #test_touch_sensor()
    #test_infrared()
    test_arm()
    #follow_object()
    #right_camera()
def test_touch_sensor():
    robot = rb.Snatch3rRobot()
    robot.touch_sensor.wait_until_pressed()
    print('yes')


def run_test_drive_system():
    robot = rb.Snatch3rRobot()
    robot.drive_system.spin_in_place_degrees(90, 50)
    robot.drive_system.turn_degrees(-90, 50)


def run_test_polygon(n):
    robot = rb.Snatch3rRobot()
    for k in range(n):
        print(k)
        robot.drive_system.go_straight_inches(24, 100)
        robot.drive_system.left_wheel.reset_degrees_spun()
        robot.drive_system.stop_moving()
        time.sleep(1)
        robot.drive_system.spin_in_place_degrees(round(360/n), 100)
        robot.drive_system.right_wheel.reset_degrees_spun()
        robot.drive_system.left_wheel.reset_degrees_spun()
        robot.drive_system.stop_moving()
        time.sleep(1)


def run_test_ellipse():
    robot = rb.Snatch3rRobot()
    while True:
        if robot.color_sensor.get_reflected_intensity() <= 5:
            robot.drive_system.start_moving(50, 50)
            robot.drive_system.right_wheel.reset_degrees_spun(0)
        elif robot.color_sensor.get_reflected_intensity() > 5:
            robot.drive_system.turn_degrees(2, 100)
            robot.drive_system.start_moving(10, 10)
            robot.drive_system.right_wheel.reset_degrees_spun(0)


def run_and_stop(color):
    robot = rb.Snatch3rRobot()
    while True:
        robot.drive_system.start_moving(20, 20)
        if robot.color_sensor.get_color() == color:
            break
    robot.drive_system.stop_moving()


def camera_sense():
    robot = rb.Snatch3rRobot()

    while True:
        print(robot.camera.get_biggest_blob().get_area())
        if robot.camera.get_biggest_blob().get_area() > 600:
            print("Beeping:")
            ev3.Sound.beep().wait()
        else:
            pass


def test_infrared():
    robot = rb.Snatch3rRobot()
    while True:
        print(robot.proximity_sensor.get_distance_to_nearest_object_in_inches())
        if robot.proximity_sensor.get_distance_to_nearest_object_in_inches() <= 10:
            ev3.Sound.beep().wait()


def test_arm():
    robot = rb.Snatch3rRobot()
    #robot.arm.calibrate()
    #robot.arm.move_arm_to_position(4)

def follow_object():
    robot = rb.Snatch3rRobot()
    while True:
        print(robot.camera.get_biggest_blob().get_area())
        if robot.camera.get_biggest_blob().get_area() > 600:
            print(robot.camera.get_biggest_blob().is_against_left_edge())
            if robot.camera.get_biggest_blob().is_against_left_edge():
                robot.drive_system.turn_degrees(10, 100)
                robot.drive_system.right_wheel.reset_degrees_spun()

def right_camera():
    robot = rb.Snatch3rRobot()
    while True:
        if robot.camera.get_biggest_blob().get_area() > 600:
            if robot.camera.get_biggest_blob().is_against_right_edge():
                print(robot.camera.get_biggest_blob().is_against_right_edge())


main()
