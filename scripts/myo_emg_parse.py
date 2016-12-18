#!/usr/bin/env python

"""
myo_emg_parse.py: Collects the MyoBand electrode data and parses it into
 flexion, extension, and diff (flextion-extension) values for publishing on
 separate rostopics.

BioRobotics Lab, Florida Atlantic University, 2016
"""
__author__ = "Thomas Colestock"
__version__ = "1.0.0"


import rospy

from std_msgs.msg import UInt8, Float32
from geometry_msgs.msg import Twist, Vector3
from ros_myo.msg import EmgArray


rospy.init_node("myo_emg_parse", anonymous=True)

flexPub = rospy.Publisher("flexion", Float32, queue_size=10)
extPub = rospy.Publisher("extension", Float32, queue_size=10)
diffPub = rospy.Publisher("emg_difference", Float32, queue_size=10)


def listen():
    rospy.Subscriber("myo_emg", EmgArray, parse)


def parse(emgArray):
    emgArr = emgArray.data
    ext = float(emgArr[3])  # electrode 4
    flex = float(emgArr[7])  # electrode 8
    emg_diff = flex - ext
    flexPub.publish(flex)
    extPub.publish(ext)
    diffPub.publish(emg_diff)
    rospy.loginfo("callback")


if __name__ == '__main__':
    listen()
    rospy.loginfo("spinning")
    rospy.spin()
