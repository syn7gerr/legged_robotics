#!/usr/bin/python
# Software License Agreement (GPL V3 License)
# Written by: Bryan Butenhoff <syn7gerr@vt.edu>

import rospy
import dynamixel
from legged_robotics.msg import Dynamixel_Net

def refresh_net(data):
	for actuator in net.get_dynamixels():
		actuator.moving_speed = int(data.moving_speed.data)
		actuator.torque_limit = int(data.torque_limit.data)
		actuator.goal_position = int(data.goal_position.data)

	net.synchronize()

if __name__ == '__main__':
	try:
		rospy.init_node('network_node')

		# Initializing the serial port connection based on configuration file data in /config/settings.yaml and creating a network
		serial = dynamixel.SerialStream(port=rospy.get_param("~port"), baudrate=rospy.get_param("~baudRate"), timeout=1)
		net = dynamixel.DynamixelNetwork(serial)

		# Populating the created network with the servo ids found in /config/setting.
		for servoId in rospy.get_param("~servoIds"):
			newDynamixel = dynamixel.Dynamixel(servoId, net)
			net._dynamixel_map[servoId] = newDynamixel

		sub = rospy.Subscriber('cmd_pos', Dynamixel_Net, refresh_net)
		rospy.spin()

	except rospy.ROSInterruptException:
		pass
