import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose


class SimpleTurtlesimKinematics(Node):

    def __init__(self):
        super().__init__("simple_turtlesim_kinematics")

        # Subscribe to turtle1 pose
        self.turtle1_pose_sub_ = self.create_subscription(
            Pose,
            "/turtle1/pose",
            self.turtle1PoseCallback,
            10
        )

        # Subscribe to turtle2 pose
        self.turtle2_pose_sub_ = self.create_subscription(
            Pose,
            "/turtle2/pose",
            self.turtle2PoseCallback,
            10
        )

        # Store last poses
        self.last_turtle1_pose_ = Pose()
        self.last_turtle2_pose_ = Pose()


    def turtle1PoseCallback(self, msg):
        self.last_turtle1_pose_ = msg


    def turtle2PoseCallback(self, msg):
        self.last_turtle2_pose_ = msg

        # Translation vector calculation
        Tx = self.last_turtle2_pose_.x - self.last_turtle1_pose_.x
        Ty = self.last_turtle2_pose_.y - self.last_turtle1_pose_.y

        self.get_logger().info(
            "\nTranslation Vector turtle1 -> turtle2\nTx: %f\nTy: %f\n" % (Tx, Ty)
        )


def main(args=None):

    rclpy.init(args=args)

    simple_turtlesim_kinematics = SimpleTurtlesimKinematics()

    rclpy.spin(simple_turtlesim_kinematics)

    simple_turtlesim_kinematics.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()