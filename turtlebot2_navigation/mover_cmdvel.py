#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Mover(Node):
    def __init__(self):
        super().__init__('mover_robot')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.mover)

    def mover(self):
        vel = Twist()
        vel.linear.x = 0.2
        self.pub.publish(vel)

def main(args=None):
    rclpy.init(args=args)
    node = Mover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

