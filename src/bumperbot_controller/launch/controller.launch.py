from launch import LaunchDescription
from launch.actions import TimerAction
from launch_ros.actions import Node


def generate_launch_description():

    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager",
            "/controller_manager"
        ]
    )

    simple_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "simple_controller",
            "--controller-manager",
            "/controller_manager"
        ]
    )

    return LaunchDescription([
        TimerAction(period=3.0, actions=[joint_state_broadcaster_spawner]),
        TimerAction(period=5.0, actions=[simple_controller]),
    ])