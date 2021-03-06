"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and PUT_YOUR_NAME_HERE.
"""
# ------------------------------------------------------------------------------
# TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this TODO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 2. With your instructor, review the "big picture" of laptop-robot
# TODO:    communication, per the comment in mqtt_sender.py.
# TODO:    Once you understand the "big picture", delete this TODO.
# ------------------------------------------------------------------------------

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    # --------------------------------------------------------------------------
    # TODO: 3. Construct a Snatch3rRobot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------
    robot = rb.Snatch3rRobot()

    # --------------------------------------------------------------------------
    # TODO: 4. Add code that constructs a   com.MqttClient   that will
    # TODO:    be used to receive commands sent by the laptop.
    # TODO:    Connect it to this robot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------
    rc = RemoteControlEtc(robot)

    comms = com.MqttClient(rc)
    comms.connect_to_pc()

    # --------------------------------------------------------------------------
    # TODO: 5. Add a class for your "delegate" object that will handle messages
    # TODO:    sent from the laptop.  Construct an instance of the class and
    # TODO:    pass it to the MqttClient constructor above.  Augment the class
    # TODO:    as needed for that, and also to handle the go_forward message.
    # TODO:    Test by PRINTING, then with robot.  When OK, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 6. With your instructor, discuss why the following WHILE loop,
    # TODO:    that appears to do nothing, is necessary.
    # TODO:    When you understand this, delete this TODO.
    # --------------------------------------------------------------------------
    while True:
        # ----------------------------------------------------------------------
        # TODO: 7. Add code that makes the robot beep if the top-red button
        # TODO:    on the Beacon is pressed.  Add code that makes the robot
        # TODO:    speak "Hello. How are you?" if the top-blue button on the
        # TODO:    Beacon is pressed.  Test.  When done, delete this TODO.
        # ----------------------------------------------------------------------
        time.sleep(0.01)  # For the delegate to do its work

class RemoteControlEtc(object):
    def __init__(self, robot):
        '''
        Stores the robot
        :type robot: rb.Snatch3rRobot
        '''
        self.robot = robot

    def left_autonomous(self, speed_string):
        '''makes the robot go forward at a given speed'''
        print('telling the robot to start moving at', speed_string)
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed,speed)
        self.move_to_left_switch()

    def right_autonomous(self, speed_string):
        '''makes the robot go forward at a given speed'''
        print('telling the robot to start moving at', speed_string)
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)
        self.move_to_right_switch()


    def move_to_left_switch(self):
        while True:
            if self.robot.proximity_sensor.get_distance_to_nearest_object_in_inches()<=4:
                self.robot.drive_system.go_straight_inches(20)
                self.robot.arm.raise_arm_and_close_claw()
                self.robot.drive_system.start_moving(-50,50)
                time.sleep(1)
                self.robot.drive_system.stop_moving()
                self.robot.drive_system.go_straight_inches(42)
                self.robot.arm.motor.reset_degrees_spun()
                self.robot.arm.motor.start_spinning(-100)
                while True:
                    if self.robot.arm.motor.get_degrees_spun() <= (-14.2 * 360):
                        self.robot.arm.motor.stop_spinning()
                        self.robot.arm.motor.reset_degrees_spun()
                        break
                break

    def move_to_right_switch(self):
        while True:
            if self.robot.proximity_sensor.get_distance_to_nearest_object_in_inches()<=4:
                self.robot.drive_system.go_straight_inches(20)
                self.robot.arm.raise_arm_and_close_claw()
                self.robot.drive_system.start_moving(50,-50)
                time.sleep(1)
                self.robot.drive_system.stop_moving()
                self.robot.drive_system.go_straight_inches(42)
                self.robot.arm.motor.reset_degrees_spun()
                self.robot.arm.motor.start_spinning(-100)
                while True:
                    if self.robot.arm.motor.get_degrees_spun() <= (-14.2 * 360):
                        self.robot.arm.motor.stop_spinning()
                        self.robot.arm.motor.reset_degrees_spun()
                        break
                break
main()