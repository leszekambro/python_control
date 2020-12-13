#!/usr/bin/python

import rospy
import math
from ardrone_autonomy.msg import Navdata
from std_msgs.msg import Float32

global ax
global ay
global az


def fax(mssg):
	global ax
	global ay
	global az
	ax = mssg.ax
	ay = mssg.ay
	az = mssg.az

def main():
	global ax
	global ay
	global az
	ax = 0
	ay = 0
	az = 0
	rospy.init_node('python_ardrone')
	Sax = rospy.Subscriber('/ardrone/navdata', Navdata, fax)
	Pfi = rospy.Publisher("~fi", Float32, queue_size=30)
	Pteta = rospy.Publisher("~teta", Float32, queue_size=30)
	delay = rospy.Rate(15)
	fi = Float32()
	teta = Float32()
	while not rospy.is_shutdown():
		fi.data = math.atan2(ay, ax)
		teta.data = -0*math.atan2(ax, math.sqrt(ay*ay+az*az))
		Pfi.publish(fi)
		Pteta.publish(teta)
		delay.sleep()

if __name__=='__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
