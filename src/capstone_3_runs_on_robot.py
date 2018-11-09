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
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()
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
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            print('speaking')
            ev3.Sound.speak("How are you?").wait()
        if robot.beacon_button_sensor.is_bottom_red_button_pressed():
            while True:
                if robot.camera.get_biggest_blob().get_area() >= 600:

                    if robot.camera.get_biggest_blob().center.x > 190:
                        robot.drive_system.turn_degrees(-4, 70)
                        robot.drive_system.right_wheel.reset_degrees_spun()
                        robot.drive_system.stop_moving()
                    elif robot.camera.get_biggest_blob().center.x < 130:
                        robot.drive_system.turn_degrees(4, 70)
                        robot.drive_system.right_wheel.reset_degrees_spun()
                        robot.drive_system.stop_moving()
                    else:
                        robot.drive_system.stop_moving()

                elif robot.camera.get_biggest_blob().get_area() < 600:
                    robot.drive_system.spin_in_place_degrees(6, 40)
                    robot.drive_system.right_wheel.reset_degrees_spun()
                    robot.drive_system.left_wheel.reset_degrees_spun()
                    ev3.Sound.speak("I lost it").wait()

                if robot.beacon_button_sensor.is_top_blue_button_pressed():
                    print("break")
                    break

        if robot.beacon_button_sensor.is_bottom_blue_button_pressed():
            ev3.Sound.speak("I lost it").wait()
        if robot.beacon_button_sensor.is_top_blue_button_pressed():
            print("break")
            break
        time.sleep(0.01)  # For the delegate to do its work


class RemoteControlEtc(object):
    def __init__(self, robot):
        """
        Stores the robot.
            :type robot:  rb.Snatch3rRobot
        """
        self.robot = robot

    def go_forward(self, speed_string):
        """makes the robot go forward at the given speed """
        print("Telling the robot to go forward", speed_string)
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)

    def go_left(self, speed_string):
        self.robot.drive_system.right_wheel.reset_degrees_spun()
        self.robot.drive_system.left_wheel.reset_degrees_spun()
        print("Telling the robot to go left", speed_string)
        speed = int(speed_string)
        self.robot.drive_system.turn_degrees(90, speed)

    def go_right(self, speed_string):
        self.robot.drive_system.right_wheel.reset_degrees_spun()
        self.robot.drive_system.left_wheel.reset_degrees_spun()
        print("Telling the robot to go right", speed_string)
        speed = int(speed_string)
        self.robot.drive_system.turn_degrees(-90, speed)

    def stop(self):
        print("Telling the robot to stop")
        self.robot.drive_system.stop_moving()
        self.robot.drive_system.right_wheel.reset_degrees_spun()
        self.robot.drive_system.left_wheel.reset_degrees_spun()

    def go_back(self, speed_string):
        print("Telling the robot to go back", speed_string)
        speed = int(speed_string)
        self.robot.drive_system.start_moving(-speed, -speed)

    def arm_up(self):
        print("Telling the robot to arm up")
        self.robot.arm.move_arm_to_position(12)

    def arm_down(self):
        print("Telling the robot to arm down")
        self.robot.arm.move_arm_to_position(0)




main()