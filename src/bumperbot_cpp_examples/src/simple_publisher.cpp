#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>
#include <type_traits>   // IMPORTANT: required for is_convertible_v
#include <chrono>

using namespace std::chrono_literals;

class SimplePublisher : public rclcpp::Node
{
public:
  SimplePublisher()
  : Node("simple_publisher"), counter_(0)
  {
    publisher_ = this->create_publisher<std_msgs::msg::String>("chatter", 10);

    timer_ = this->create_wall_timer(
      1s,
      std::bind(&SimplePublisher::publish_message, this)
    );

    RCLCPP_INFO(this->get_logger(), "Simple publisher started (1 Hz)");
  }

private:
  void publish_message()
  {
    std_msgs::msg::String msg;
    msg.data = "Hello ROS 2 : " + std::to_string(counter_++);

    publisher_->publish(msg);
  }

  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
  rclcpp::TimerBase::SharedPtr timer_;
  int counter_;
};

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<SimplePublisher>());
  rclcpp::shutdown();
  return 0;
}
