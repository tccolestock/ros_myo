#!/usr/bin/env python

"""
grasp_flex.py: Simple script to slowly open and then close the fingers, then
 thumb.

BioRobotics Lab, Florida Atlantic University, 2016
"""
__author__ = "Thomas Colestock"
__version__ = "1.0.0"


import rospy

from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from sr_robot_msgs.msg import BiotacAll, ShadowPST, UBI0All
from sr_robot_commander.sr_hand_commander import SrHandCommander
from sr_utilities.hand_finder import HandFinder


rospy.init_node("grasp_flex_video", anonymous=True)
rospy.sleep(1)  # Do not start at time zero
hand_commander = SrHandCommander()


# Shadow Hand Dictionaries:::
start = {
    'rh_FFJ1': 0.004462489564758254,    'rh_FFJ2': 0.5824300986992313,
    'rh_FFJ3': -0.06589317250962576,    'rh_FFJ4': -0.014037985768995172,
    'rh_THJ4': 0.9852128448766578,      'rh_THJ5': -0.35808646382658194,
    'rh_THJ1': 0.039838472070345236,    'rh_THJ2': 0.019881639457926235,
    'rh_THJ3': 0.01002801514898127,     'rh_LFJ2': 0.22009683045061237,
    'rh_LFJ3': 0.06263935222117027,     'rh_LFJ1': 0.017877044690381982,
    'rh_LFJ4': -0.04729200226155228,    'rh_LFJ5': 0.06588764091936142,
    'rh_RFJ4': -0.0007980082966327391,  'rh_RFJ1': 0.048010232558778176,
    'rh_RFJ2': 0.35172178621711814,     'rh_RFJ3': 0.008215032197292554,
    'rh_MFJ1': 0.0044815872376459676,   'rh_MFJ3': -0.015813316088005697,
    'rh_MFJ2': 0.34707800387039855,     'rh_MFJ4': 0.040486752405445955,
    'rh_WRJ2': -0.012987432112372568,   'rh_WRJ1': -0.3927317393175203}

close_fingers = {
    'rh_FFJ1': 0.03187492546255877,     'rh_FFJ2': 1.6070853508462637,
    'rh_FFJ3': 1.4705084117792264,      'rh_FFJ4': -0.007807417007164914,
    'rh_THJ4': 0.9850911788580581,      'rh_THJ5': -0.2025545669029515,
    'rh_THJ1': 0.2794737532860944,      'rh_THJ2': 0.24197512513982633,
    'rh_THJ3': 0.023937570085237263,    'rh_LFJ2': 1.5980013836595672,
    'rh_LFJ3': 1.098877759656638,       'rh_LFJ1': 0.22286715714009533,
    'rh_LFJ4': -0.15054968392815313,    'rh_LFJ5': 0.07262328034306434,
    'rh_RFJ4': -0.0031615450609755597,  'rh_RFJ1': 0.10094459153384133,
    'rh_RFJ2': 1.5511613727099602,      'rh_RFJ3': 1.43920535534375,
    'rh_MFJ1': 0.03529249949646168,     'rh_MFJ3': 1.4642411062133984,
    'rh_MFJ2': 1.6305900141317393,      'rh_MFJ4': -0.0011675935361636718,
    'rh_WRJ2': -4.627691793882189e-06,  'rh_WRJ1': 0.40850290603901596}

close_thumb_flex = {
    'rh_FFJ1': 0.030599928444056457,    'rh_FFJ2': 1.5798685828077383,
    'rh_FFJ3': 1.4346871380349107,      'rh_FFJ4': -0.012533730025784747,
    'rh_THJ4': 0.9313243760216793,      'rh_THJ5': -0.15941243629813273,
    'rh_THJ1': 0.8915517445998653,      'rh_THJ2': 0.57755691304697,
    'rh_THJ3': 0.10892692804782067,     'rh_LFJ2': 1.5980013836595672,
    'rh_LFJ3': 1.098877759656638,       'rh_LFJ1': 0.22286715714009533,
    'rh_LFJ4': -0.15054968392815313,    'rh_LFJ5': 0.07262328034306434,
    'rh_RFJ4': -0.0960273218183659,     'rh_RFJ1': 0.04924126416284941,
    'rh_RFJ2': 1.533396414252161,       'rh_RFJ3': 1.2786533911685845,
    'rh_MFJ1': 0.03697309471057891,     'rh_MFJ3': 1.3995185940738193,
    'rh_MFJ2': 1.6273579229243424,      'rh_MFJ4': 0.010057198073120985,
    'rh_WRJ2': -4.627691793882189e-06,  'rh_WRJ1': 0.40850290603901596}


# ------------------------------------------------------------------

if __name__ == '__main__':
    # Move to start
    joint_goals = start
    hand_commander.move_to_joint_value_target_unsafe(joint_goals, 8, True)

    # Move to close_fingers
    joint_goals = close_fingers
    hand_commander.move_to_joint_value_target_unsafe(joint_goals, 8, True)

    # Move to close_thumb_flex
    joint_goals = close_thumb_flex
    hand_commander.move_to_joint_value_target_unsafe(joint_goals, 8, True)
