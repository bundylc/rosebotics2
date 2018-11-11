"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Hao Jiang.
"""
# ------------------------------------------------------------------------------
# TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this TODO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 2. With your instructor, discuss the "big picture" of laptop-robot
# TODO:    communication:
# TODO:      - One program runs on your LAPTOP.  It displays a GUI.  When the
# TODO:        user presses a button intended to make something happen on the
# TODO:        ROBOT, the LAPTOP program sends a message to its MQTT client
# TODO:        indicating what it wants the ROBOT to do, and the MQTT client
# TODO:        SENDS that message TO a program running on the ROBOT.
# TODO:
# TODO:      - Another program runs on the ROBOT. It stays in a loop, responding
# TODO:        to events on the ROBOT (like pressing buttons on the IR Beacon).
# TODO:        It also, in the background, listens for messages TO the ROBOT
# TODO:        FROM the program running on the LAPTOP.  When it hears such a
# TODO:        message, it calls the method in the DELAGATE object's class
# TODO:        that the message indicates, sending arguments per the message.
# TODO:
# TODO:  Once you understand the "big picture", delete this TODO (if you wish).
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 3. One team member: change the following in mqtt_remote_method_calls.py:
#                LEGO_NUMBER = 99
# TODO:    to use YOUR robot's number instead of 99.
# TODO:    Commit and push the change, then other team members Update Project.
# TODO:    Then delete this TODO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 4. Run this module.
# TODO:    Study its code until you understand how the GUI is set up.
# TODO:    Then delete this TODO.
# ------------------------------------------------------------------------------

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()
    #setup_gui(root, mqtt_client)
    set_remote_control_gui(root, mqtt_client)
    root.mainloop()
    # --------------------------------------------------------------------------
    # TODO: 5. Add code above that constructs a   com.MqttClient   that will
    # TODO:    be used to send commands to the robot.  Connect it to this pc.
    # TODO:    Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------


def setup_gui(root_window, mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=20)
    frame.grid()

    speed_entry_box = ttk.Entry(frame)
    go_forward_button = ttk.Button(frame, text="Go forward")

    speed_entry_box.grid()
    go_forward_button.grid()

    go_forward_button['command'] = \
        lambda: handle_go_forward(speed_entry_box, mqtt_client)


def set_remote_control_gui(root_window, mqtt_client):
    main_frame = ttk.Frame(root_window, padding=10)
    main_frame.grid()

    speed_entry_box = ttk.Entry(main_frame)
    speed_entry_box.insert(0, "60")
    go_forward_button = ttk.Button(main_frame, text="Go forward")
    go_left_button = ttk.Button(main_frame, text="Go left")
    go_right_button = ttk.Button(main_frame, text="Go right")
    stop_button = ttk.Button(main_frame, text="Stop")
    back_button = ttk.Button(main_frame, text="Go back")
    exit_button = ttk.Button(main_frame, text="Exit")
    arm_up_button = ttk.Button(main_frame, text="Arm_up")
    arm_down_button = ttk.Button(main_frame, text="Arm_down")
    chase_mode_button = ttk.Button(main_frame, text="chase_mode")

    speed_entry_box.grid(row=1, column=2)
    go_forward_button.grid(row=3, column=2)
    go_left_button.grid(row=4, column=1)
    go_right_button.grid(row=4, column=3)
    stop_button.grid(row=4, column=2)
    back_button.grid(row=5, column=2)
    exit_button.grid(row=6, column=2)
    arm_up_button.grid(row=2, column=1)
    arm_down_button.grid(row=2, column=3)
    chase_mode_button.grid(row=2, column=2)

    go_forward_button['command'] = \
        lambda: handle_go_forward(speed_entry_box, mqtt_client)
    go_left_button['command'] = \
        lambda: handle_go_left(speed_entry_box, mqtt_client)
    go_right_button['command'] = \
        lambda: handle_go_right(speed_entry_box, mqtt_client)
    stop_button['command'] = \
        lambda: handle_stop(mqtt_client)
    back_button['command'] = \
        lambda: handle_go_back(speed_entry_box, mqtt_client)
    exit_button['command'] = lambda: exit()
    arm_up_button['command'] = \
        lambda: handle_arm_up(mqtt_client)
    arm_down_button['command'] = \
        lambda: handle_arm_down(mqtt_client)
    chase_mode_button['command'] = \
        lambda: handle_chase_mode(mqtt_client)


def handle_go_forward(entry_box, mqtt_client):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    speed_string = entry_box.get()
    print('Sending the go_forward message with speed')
    mqtt_client.send_message('go_forward', [speed_string])


def handle_go_left(entry_box, mqtt_client):
    speed_string = entry_box.get()
    print('Sending the go_left message with speed')
    mqtt_client.send_message('go_left', [speed_string])


def handle_go_right(entry_box, mqtt_client):
    speed_string = entry_box.get()
    print('Sending the go_right message with speed')
    mqtt_client.send_message('go_right', [speed_string])


def handle_stop(mqtt_client):
    print('Sending the stop message')
    mqtt_client.send_message('stop')


def handle_go_back(entry_box, mqtt_client):
    speed_string = entry_box.get()
    print('Sending the go_back message with speed')
    mqtt_client.send_message('go_back', [speed_string])


def handle_arm_up(mqtt_client):
    print('Sending the arm_up message')
    mqtt_client.send_message('arm_up')


def handle_arm_down(mqtt_client):
    print('Sending the arm_down message')
    mqtt_client.send_message('arm_down')


def handle_chase_mode(mqtt_client):
    print('Sending the chase_mode message')
    mqtt_client.send_message('chase_mode')


    # --------------------------------------------------------------------------
    # TODO: 6. This function needs the entry box in which the user enters
    # TODO:    the speed at which the robot should move.  Make the 2 changes
    # TODO:    necessary for the entry_box constructed in  setup_gui
    # TODO:    to make its way to this function.  When done, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 7. For this function to tell the robot what to do, it needs
    # TODO:    the MQTT client constructed in main.  Make the 4 changes
    # TODO:    necessary for that object to make its way to this function.
    # TODO:    When done, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 8. Add the single line of code needed to get the string that is
    # TODO:    currently in the entry box.
    # TODO:
    # TODO:    Then add the single line of code needed to "call" a method on the
    # TODO:    LISTENER that runs on the ROBOT, where that LISTENER is the
    # TODO:    "delegate" object that is constructed when the ROBOT's code
    # TODO:    runs on the ROBOT.  Send to the delegate the speed to use
    # TODO:    plus a method name that you will implement in the DELEGATE's
    # TODO:    class in the module that runs on the ROBOT.
    # TODO:
    # TODO:    Test by using a PRINT statement.  When done, delete this TODO.
    # --------------------------------------------------------------------------


main()
