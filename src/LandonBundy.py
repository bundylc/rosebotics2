"""
  Capstone Project.  Code written by Landon Bundy.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


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


def main2():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()
    setup_gui(root, mqtt_client)
    set_remote_control_gui(root, mqtt_client)
    root.mainloop()


def setup_gui(root_window, mqtt):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=10)
    frame.grid()

    distance_entry_box = ttk.Entry(frame)
    go_forward_button = ttk.Button(frame, text="Go forward")

    distance_entry_box.grid()
    go_forward_button.grid()

    go_forward_button['command'] = \
        lambda: handle_go_forward(distance_entry_box, mqtt)


def handle_go_forward(distance_entry_box, mqtt):
    distance = distance_entry_box.get()
    print("Send message with distance in inches", distance)
    mqtt.send_message('go_forward', [distance])


def setup_gui2(root_window, mqtt):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=10)
    frame.grid()

    speed_entry_box = ttk.Entry(frame)
    go_forward_button = ttk.Button(frame, text="Go forward")

    speed_entry_box.grid()
    go_forward_button.grid()

    go_forward_button['command'] = \
        lambda: handle_go_forward(speed_entry_box, mqtt)


def handle_go_forward2(speed_entry_box, mqtt):
    speed = speed_entry_box.get()
    print("Send message with speed", speed)
    mqtt.send_message('go_forward', [speed])


def move_item(distance_entry_box):
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving()
    robot.color_sensor.wait_until_color_is(1)
    robot.drive_system.stop_moving()
    robot.arm.raise_arm_and_close_claw()
    robot.drive_system.turn_degrees(90)
    robot.drive_system.go_straight_inches(distance_entry_box.get())
    robot.arm.calibrate()
    robot.drive_system.go_straight_inches(-5)
    robot.drive_system.turn_degrees(180)
    robot.drive_system.start_moving()
    robot.color_sensor.wait_until_color_is(1)
    robot.drive_system.turn_degrees(90)
    robot.drive_system.start_moving()
    robot.color_sensor.wait_until_color_is(6)
    robot.drive_system.stop_moving()


"""def car():
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving()
    --- speed = mqtt box ---
    if robot.color_sensor.get_value(5):
        robot.drive_system.stop_moving()
    if robot.color_sensor.get_value(4):
        robot.drive_system speed = 1/2 speed"""


def main():
    #move_item()
    #test_raise_arm()
    test_calibrate()
    #test_ellipse()
    #car()


main()
