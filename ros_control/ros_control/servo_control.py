#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from topics_services.msg import ServoData
from topics_services.msg import Telemetric
from dynamixel_sdk import *
from .submodules.Ax12 import *
import random

Ax12.DEVICENAME = '/dev/ttyUSB0'
Ax12.BAUDRATE = 1_000_000
# sets baudrate and opens com port
Ax12.connect()
# create AX12 instance with ID 10 
motor_id_1 = 10
motor_id_2 = 11
motor_id_3 = 12
motor_id_4 = 13
motor_id_5 = 14
motor_id_6 = 15
gripper = Ax12(motor_id_1)
z_axis = Ax12(motor_id_2)
wheelRF = Ax12(motor_id_3)
wheelLF = Ax12(motor_id_4)
wheelRB = Ax12(motor_id_5)
wheelLB = Ax12(motor_id_6)

max_torque1 = 0
max_torque2 = 0
max_torque3 = 0
max_torque4 = 0
max_torque5 = 0
max_torque6 = 0
set_speed1 = 0
set_speed2 = 0
set_speed3 = 0
set_speed4 = 0
set_speed5 = 0
set_speed6 = 0
set_position1 = 0
set_position2 = 0
set_position3 = 0
set_position4 = 0
set_position5 = 0
set_position6 = 0

position1 = 0
position2 = 0
position3 = 0
position4 = 0
position5 = 0
position6 = 0
temperature1 = 0
temperature2 = 0
temperature3 = 0
temperature4 = 0
temperature5 = 0
temperature6 = 0
voltage1 = 0
voltage2 = 0
voltage3 = 0
voltage4 = 0
voltage5 = 0
voltage6 = 0
load1 = 0
load2 = 0
load3 = 0
load4 = 0
load5 = 0
load6 = 0

class ServoControllerNode(Node):
    # Default settings for AX-12A servo
    PROTOCOL_VERSION = 1.0
    DEBUG = True

    def __init__(self):
        super().__init__("servo_controller")
        self.publisher_ = self.create_publisher(Telemetric, '/Telemetric', 30)
        self.subscription = self.create_subscription(ServoData, '/ServoData', self.callback, 30)
        # e.g 'COM3' windows or '/dev/ttyUSB0' for Linux 
        self.timer_ = self.create_timer(1, self.update_telemetric_data)

    def publish_telemetric_data(self):
        msg = Telemetric()
        msg.cur_pos_fr = random.randint(0,1025)
        msg.cur_pos_fl = random.randint(0,1025)
        msg.cur_pos_br = random.randint(0,1025)
        msg.cur_pos_bl = random.randint(0,1025)
        msg.cur_pos_z_as = random.randint(0,1025)
        msg.cur_pos_gripper = random.randint(0,1025)
        msg.temp_fr = float(random.randint(180,250))/10
        msg.temp_fl = float(random.randint(180,250))/10
        msg.temp_br = float(random.randint(180,250))/10
        msg.temp_bl = float(random.randint(180,250))/10
        msg.temp_z_as = float(random.randint(180,250))/10
        msg.temp_gripper = float(random.randint(180,250))/10
        msg.voltage_fr = random.randint(9,12)
        msg.voltage_fl = random.randint(9,12)
        msg.voltage_br = random.randint(9,12)
        msg.voltage_bl = random.randint(9,12)
        msg.voltage_z_as = random.randint(9,12)
        msg.voltage_gripper = random.randint(9,12)
        msg.load_fr = random.randint(0,255)
        msg.load_fl = random.randint(0,255)
        msg.load_br = random.randint(0,255)
        msg.load_bl = random.randint(0,255)
        msg.load_z_as = random.randint(0,255)
        msg.load_gripper = random.randint(0,255)
        self.publisher_.publish(msg)
        self.get_logger().info('updated telementric 2')

    def callback(self, msg):
        # Set servo position based on received data
#        self.get_logger().info('Received position1: {}'.format(msg.set_pos1))
#        self.get_logger().info('Received speed1: {}'.format(msg.set_speed1))
#        self.get_logger().info('Received max torque: {}'.format(msg.max_torque1))
        set_position1 = msg.set_pos1
        set_speed1 = msg.set_speed1
        max_torque1 = msg.max_torque1
#        gripper.set_goal_position(set_position1)
#        self.get_logger().info(gripper.get_present_position())
#        gripper.set_torque_limit(max_torque1)
#        gripper.set_moving_speed(100)
#        gripper.set_moving_speed(set_speed1)

    def update_telemetric_data(self):
        # Get servo data and publish
#        position1 = gripper.get_present_position()
#        self.get_logger().info('Received position1: {}'.format(position1))
#        temperature1 = gripper.get_temperature()
#        voltage1 = gripper.get_voltage()
#        load1 = gripper.get_load()
        self.publish_telemetric_data()
        self.get_logger().info('updated telementric')

def main(args=None):
    rclpy.init(args=args)
    servo_controller = ServoControllerNode()
    rclpy.spin(servo_controller)
    servo_controller.port_handler.closePort()
    servo_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()