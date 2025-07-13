import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class JoyReaderNode(Node):
    def __init__(self):
        super().__init__('joy_direction_reader')
        self.subscription = self.create_subscription(
            Joy,
            'joy',
            self.joy_callback,
            10)
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)

    def joy_callback(self, msg):
        direction = 'Stop'
        linear = 0.0
        angular = 0.0

        # axes[7] → left/right, axes[8] → up/down
        axis_h = msg.axes[6] if len(msg.axes) > 6 else 0.0  # Left/Right
        axis_v = msg.axes[7] if len(msg.axes) > 7 else 0.0  # Up/Down

        if axis_v == 1.0:
            direction = 'Forward'
            linear = 0.5
        elif axis_v == -1.0:
            direction = 'Reverse'
            linear = -0.5
        elif axis_h == 1.0:
            direction = 'Left'
            angular = 1.0
        elif axis_h == -1.0:
            direction = 'Right'
            angular = -1.0

        self.get_logger().info(f'Direction: {direction}')

        twist = Twist()
        twist.linear.x = linear
        twist.angular.z = angular
        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = JoyReaderNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()