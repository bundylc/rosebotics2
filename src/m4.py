"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


"""def main2():
    root = tkinter.Tk()

    mqtt = com.MqttClient()
    mqtt.connect_to_ev3()

    setup_gui(root, mqtt)

    root.mainloop()


def setup_gui(root_window, mqtt):
 Constructs and sets up widgets on the given window.
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
    Constructs and sets up widgets on the given window.
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
    mqtt.send_message('go_forward', [speed])"""


def move_item():
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving()
    robot.color_sensor.wait_until_color_is(6)
    robot.drive_system.stop_moving()
    robot.arm.raise_arm_and_close_claw()
    robot.drive_system.spin_in_place_degrees(90)
    robot.drive_system.go_straight_inches(10)
    robot.arm.calibrate()
    robot.drive_system.go_straight_inches(-5)
    robot.drive_system.turn_degrees(180)
    robot.drive_system.start_moving()
    robot.color_sensor.wait_until_color_is(6)
    robot.drive_system.turn_degrees(90)
    robot.drive_system.start_moving()
    robot.color_sensor.wait_until_color_is(6)
    robot.drive_system.stop_moving()


def car():
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving()
    if robot.color_sensor.get_value(2):
        robot.drive_system.stop_moving()
    if robot.color_sensor.get_value(6):
        robot.drive_system.turn_degrees(90)


def calibrate():
    robot = rb.Snatch3rRobot
    robot.arm.calibrate()


def main():
    move_item()
    car()
    calibrate()


main()
