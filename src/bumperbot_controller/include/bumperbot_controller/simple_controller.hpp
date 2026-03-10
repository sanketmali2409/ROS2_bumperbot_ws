#ifndef BUMPERBOT_CONTROLLER__SIMPLE_CONTROLLER_HPP_
#define BUMPERBOT_CONTROLLER__SIMPLE_CONTROLLER_HPP_

#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist_stamped.hpp"
#include "std_msgs/msg/float64_multi_array.hpp"
#include <Eigen/Dense>

class SimpleController : public rclcpp::Node
{
public:
    SimpleController(const std::string & name);

private:
    void velCallback(const geometry_msgs::msg::TwistStamped::SharedPtr msg);

    rclcpp::Publisher<std_msgs::msg::Float64MultiArray>::SharedPtr wheel_cmd_pub_;
    rclcpp::Subscription<geometry_msgs::msg::TwistStamped>::SharedPtr vel_sub_;

    double wheel_radius_;
    double wheel_separation_;

    Eigen::Matrix2d speed_conversion_;
};

#endif