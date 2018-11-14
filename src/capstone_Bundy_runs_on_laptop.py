"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Landon Bundy.
"""
# ------------------------------------------------------------------------------
# TOsDO: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this TODsO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# aTODO: 2. With your instructor, discuss the "big picture" of laptop-robot
# TOaDO:    communication:
# TODOa:      - One program runs on your LAPTOP.  It displays a GUI.  When the
# TODOa:        user presses a button intended to make something happen on the
# TODOa:        ROBOT, the LAPTOP program sends a message to its MQTT client
# TODOa:        indicating what it wants the ROBOT to do, and the MQTT client
# TODOa:        SENDS that message TO a program running on the ROBOT.
# TODOa:
# TODOa:      - Another program runs on the ROBOT. It stays in a loop, responding
# TODOa:        to events on the ROBOT (like pressing buttons on the IR Beacon).
# TODOa:        It also, in the background, listens for messages TO the ROBOT
# TODOa:        FROM the program running on the LAPTOP.  When it hears such a
# TODOa:        message, it calls the method in the DELAGATE object's class
# TODOa:        that the message indicates, sending arguments per the message.
# TODOa:
# TODOa:  Once you understand the "big picture", delete this TaODO (if you wish).
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# aTODO: 3. One team member: change the following in mqtt_remote_method_calls.py:
#  a              LEGO_NUMBER = 99
# TOaDO:    to use YOUR robot's number instead of 99.
# TODaO:    Commit and push the change, then other team members Update Project.
# TODOa:    Then delete this TOaDO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TaODO: 4. Run this module.
# TOaDO:    Study its code until you understand how the GUI is set up.
# TODaO:    Then delete this TOaDO.
# ------------------------------------------------------------------------------

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()
    set_remote_control_gui(root, mqtt_client)
    root.mainloop()


def setup_gui(root_window, mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=20)
    frame.grid()

    speed_entry_box = ttk.Entry(frame)
    go_forward_button = ttk.Button(frame, text="Go forward")

    speed_entry_box.grid()
    go_forward_button.grid()

    go_forward_button['command'] = \
        lambda: handle_forward(speed_entry_box, mqtt_client)


def set_remote_control_gui(root_window, mqtt_client):
    main_frame = ttk.Frame(root_window, padding=10)
    main_frame.grid()

    speed_entry_box = ttk.Entry(main_frame)
    speed_entry_box.insert(0, "60")
    forward_button = ttk.Button(main_frame, text="Go forward")
    left_button = ttk.Button(main_frame, text="Go left")
    right_button = ttk.Button(main_frame, text="Go right")
    stop_button = ttk.Button(main_frame, text="Stop")
    back_button = ttk.Button(main_frame, text="Go back")
    exit_button = ttk.Button(main_frame, text="Exit")
    raise_arm_button = ttk.Button(main_frame, text="Raise Arm")
    lower_arm_button = ttk.Button(main_frame, text="Lower Arm")
    speak_button = ttk.Button(main_frame, text="Speak")
    color_sensor_button = ttk.Button(main_frame, text="Color Sensor")

    speed_entry_box.grid(row=1, column=2)
    forward_button.grid(row=2, column=2)
    left_button.grid(row=2, column=1)
    right_button.grid(row=2, column=3)
    stop_button.grid(row=3, column=1)
    back_button.grid(row=3, column=2)
    exit_button.grid(row=3, column=3)
    raise_arm_button.grid(row=4, column=1)
    lower_arm_button.grid(row=4, column=3)
    speak_button.grid(row=4, column=2)
    color_sensor_button.grid(row=5, column=1)

    forward_button['command'] = \
        lambda: handle_forward(speed_entry_box, mqtt_client)
    left_button['command'] = \
        lambda: handle_left(speed_entry_box, mqtt_client)
    right_button['command'] = \
        lambda: handle_right(speed_entry_box, mqtt_client)
    stop_button['command'] = \
        lambda: handle_stop(mqtt_client)
    back_button['command'] = \
        lambda: handle_back(speed_entry_box, mqtt_client)
    exit_button['command'] = lambda: exit()
    raise_arm_button['command'] = \
        lambda: handle_raise_arm(mqtt_client)
    lower_arm_button['command'] = \
        lambda: handle_lower_arm(mqtt_client)
    speak_button['command'] = \
        lambda: handle_speak(mqtt_client)
    color_sensor_button['command'] = \
        lambda: handle_color_sensor(mqtt_client)


def handle_forward(entry_box, mqtt_client):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    speed_string = entry_box.get()
    print('Sending the go_forward message with speed')
    mqtt_client.send_message('forward', [speed_string])


def handle_left(entry_box, mqtt_client):
    speed_string = entry_box.get()
    print('Sending the go_left message with speed')
    mqtt_client.send_message('left', [speed_string])


def handle_right(entry_box, mqtt_client):
    speed_string = entry_box.get()
    print('Sending the go_right message with speed')
    mqtt_client.send_message('right', [speed_string])


def handle_stop(mqtt_client):
    print('Sending the stop message')
    mqtt_client.send_message('stop')


def handle_back(entry_box, mqtt_client):
    speed_string = entry_box.get()
    print('Sending the go_back message with speed')
    mqtt_client.send_message('back', [speed_string])


def handle_raise_arm(mqtt_client):
    print('Sending the arm_up message')
    mqtt_client.send_message('raise_arm')


def handle_lower_arm(mqtt_client):
    print('Sending the arm_down message')
    mqtt_client.send_message('lower_arm')


def handle_speak(mqtt_client):
    print('Sending the speak message')
    mqtt_client.send_message('speak')


def handle_color_sensor(mqtt_client):
    print('Sending the color_sensor message')
    mqtt_client.send_message('color_sensor')


main()

