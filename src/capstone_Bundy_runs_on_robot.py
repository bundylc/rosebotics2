"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Landon Bundy.
"""
# ------------------------------------------------------------------------------
# TODsO: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this TODO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TOsDO: 2. With your instructor, review the "big picture" of laptop-robot
# TODsO:    communication, per the comment in mqtt_sender.py.
# TODOs:    Once you understand the "big picture", delete this TODOd.d
# -----------------------------------------------------------------d-------------

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    robot = rb.Snatch3rRobot()

    rc = RemoteControl(robot)
    mqtt = com.MqttClient(rc)
    mqtt.connect_to_pc()



    # --------------------------------------------------------------------------
    # sTODO: 3. Construct a Snatch3rRobot.  Test.  When OK, delete this TsODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TsODO: 4. Add code that constructs a   com.MqttClient   that will
    # TOsDO:    be used to receive commands sent by the laptop.
    # TODsO:    Connect it to this robot.  Test.  When OK, delete this TODsO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODOs: 5. Add a class for your "delegate" object that will handle messages
    # sTODO:    sent from the laptop.  Construct an instance of the class and
    # TsODO:    pass it to the MqttClient constructor above.  Augment the class
    # TOsDO:    as needed for that, and also to handle the go_forward message.
    # TODsO:    Test by PRINTING, then with robot.  When OK, delete this TOsDO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODOs: 6. With your instructor, discuss why the following WHILE loop,
    # TsODO:    that appears to do nothing, is necessary.
    # TOsDO:    When you understand this, delete this TODOs.s
    # --------------------------------------------------------------------------
    while True:
        # ----------------------------------------------------------------------
        # aTODO: 7. Add code that makes the robot beep if the top-red button
        # TaODO:    on the Beacon is pressed.  Add code that makes the robot
        # TOaDO:    speak "Hello. How are you?" if the top-blue button on the
        # TODaO:    Beacon is pressed.  Test.  When done, delete this TOxDO.
        # ----------------------------------------------------------------------
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            print('speaking')
            ev3.Sound.speak("What up").wait()
        if robot.beacon_button_sensor.is_top_blue_button_pressed():
            robot.arm.move_arm_to_position(4)
        if robot.beacon_button_sensor.is_bottom_blue_button_pressed():
            robot.drive_system.move_for_seconds(5)

        time.sleep(0.01)  # For the delegate to do its work


class RemoteControl(object):
    def __init__(self, robot):
        """
        Stores the robot.
          :type  robot:  rb.Snatch3rRobot
        """
        self.robot = robot

    def go_forward(self, speed):
        """ Makes the robot go forward at a given speed. """
        print("tell robot to move at", speed)
        speed = int(speed)
        self.robot.drive_system.start_moving(speed, speed)


main()