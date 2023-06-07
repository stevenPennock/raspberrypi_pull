# robotica_bringup/launch/ros_control.launch.py

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    serial_input = Node(
        package='ros_control', 
        executable='serial_input'
    )

    Telemetric = Node(
        package='ros_control', 
        executable='Telemetric'
    )

    RandomData = Node(
        package='ros_control', 
        executable='RandomData'
    )

    servo_control = Node(
        package='ros_control', 
        executable='servo_control'
    )

    ld.add_action(serial_input)
    ld.add_action(servo_control)
    ld.add_action(Telemetric)
    ld.add_action(RandomData)

    return ld