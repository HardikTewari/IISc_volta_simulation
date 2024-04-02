#!/usr/bin/env python3

import rospy
import roslaunch
from geometry_msgs.msg import Pose

def spawn_robots(robot_name, position):
    node = roslaunch.core.Node(
        package="gazebo_ros",
        executable="spawn_model",
        name="spawn_" + robot_name,
        namespace="/",
        args="-urdf -param robot_description -model {} -x {} -y {} -z {}".format(
            robot_name, position[0], position[1], position[2]
        ),
    )
    launch = roslaunch.scriptapi.ROSLaunch()
    launch.start()

    process = launch.launch(node)
    process.spin()

if __name__ == "__main__":
    rospy.init_node("spawn_robot")

    robot_positions = rospy.get_param("~robot_positions", [])
    robot_description = rospy.get_param("~robot_description", "")

    for i, pos in enumerate(robot_positions):
        spawn_robots("robot{}".format(i + 1), pos)
