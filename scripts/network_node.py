#!/usr/bin/python
# Software License Agreement (GPL V3 License)
# Written by: Bryan Butenhoff <syn7gerr@vt.edu>

import rospy
import dynamixel
from sensor_msgs.msg import JointState

def refresh_net(data):
	for i in xrange(len(net.get_dynamixels())):
		actId = int(data.name[i])
		net[actId].moving_speed = int(data.velocity[i])
		net[actId].torque_limit = int(data.effort[i])
		net[actId].goal_position = int(data.position[i])
	net.synchronize()

if __name__ == '__main__':
	try:
		rospy.init_node('network_node')

		# Initializing the serial port connection
		serial = dynamixel.SerialStream(port=rospy.get_param("~port"), baudrate=rospy.get_param("~baudRate"), timeout=1)
		# Initializing the dynamixel network
		net = dynamixel.DynamixelNetwork(serial)
		# Populating the created network with specified servo ids
		for servoId in rospy.get_param("~servoIds"):
			newDynamixel = dynamixel.Dynamixel(servoId, net)
			net._dynamixel_map[servoId] = newDynamixel

		sub = rospy.Subscriber('cmd_pos', JointState, refresh_net)
		rospy.spin()

	except rospy.ROSInterruptException:
		pass
