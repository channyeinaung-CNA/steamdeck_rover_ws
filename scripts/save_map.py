import rclpy
from rclpy.node import Node
from slam_toolbox.srv import SaveMap
from std_msgs.msg import String

class SaveMapClient(Node):
    def __init__(self):
        super().__init__('save_map_client')
        self.cli = self.create_client(SaveMap, '/slam_toolbox/save_map')
        while not self.cli.wait_for_service(timeout_sec=2.0):
            self.get_logger().info('Waiting for /slam_toolbox/save_map service...')
        self.req = SaveMap.Request()
        self.req.name = String(data='my_map')  # ✅ Correct usage for Humble
        self.send_request()

    def send_request(self):
        future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, future)
        if future.result():
            self.get_logger().info("✅ Map saved successfully!")
        else:
            self.get_logger().error("❌ Map save failed.")

rclpy.init()
client = SaveMapClient()
client.destroy_node()
rclpy.shutdown()