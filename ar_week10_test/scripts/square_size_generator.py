#!/usr/bin/env python
import rospy
import random
from ar_week10_test.msg import *


pub = rospy.Publisher('size', square, queue_size= 0)
rospy.init_node('square_size_generator', anonymous=True)

rate = rospy.Rate(0.05) # Set the rate to 20 seconds - 0.05Hz = 20 seconds
msg = square()

while not rospy.is_shutdown():
    try:
        msg.size = random.uniform(0.05, 0.20) #Random real number between 0.05 and 0.20
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()
    except rospy.ROSInterruptException:
        break
