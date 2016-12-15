#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt8, Float32
from geometry_msgs.msg import Twist,Vector3
from ros_myo.msg import EmgArray

if __name__ == '__main__':

    rospy.init_node("myo_emg_parse", anonymous=True)

    flexPub = rospy.Publisher("flexion", Float32, queue_size=10)
    extPub = rospy.Publisher("extension", Float32, queue_size=10)
    diffPub = rospy.Publisher("emg_difference", Float32, queue_size=10)

    def parse(emgArray):
        emgArr=emgArray.data
        ext = float(emgArr[3]) # electrode 4
        flex = float(emgArr[7]) # electrode 8
        emg_diff = flex-ext
        flexPub.publish(flex)
        extPub.publish(ext)
        diffPub.publish(emg_diff)
        # rospy.loginfo(flex)
        rospy.loginfo("callback")

    rospy.Subscriber("myo_emg", EmgArray, parse)
    rospy.loginfo("spinning")
    rospy.spin()
