from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction

def generate_launch_description():
    slam_node = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        parameters=[
            '/home/steam/steamdeck_rover_ws/config/mapper_params_online_async.yaml',
            {'use_sim_time': False}
        ],
        output='screen'
    )

    return LaunchDescription([
        TimerAction(period=5.0, actions=[slam_node])  # Delay SLAM launch 5 seconds
    ])
