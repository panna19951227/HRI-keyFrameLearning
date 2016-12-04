#!/usr/bin/python

import rospy
import sys

from nav_msgs.msg      import Odometry
from turtlesim.msg     import Pose

########################################################################
# keyframe_gen.py 
# 
# Generate keyframes on voice command
#
# Input:  Voice command given by PhraseRecognizer
#         Topic odom given by Shpero OR topic turtle1/pos
# Output: Topic keyframe: Odometry
# 
# Chunheng Luo 
# 2016-12-04
########################################################################

# ----------------------------------------------------------------------
# Node initialization
# ----------------------------------------------------------------------
rospy.init_node('keyframe_gen') 

# ----------------------------------------------------------------------
# Subscribers and publishers
# ----------------------------------------------------------------------
# For turtlesim simulation ---------------------------------------------
rospy.Subscriber('turtle1/pose', Pose, PosCallback) 
# TODO
# For Shpero -----------------------------------------------------------
# rospy.Subscriber('odom', Odometry, PosCallback) 
rospy.Subscriber('verbalInstruction', String, CmdCallback)
Pub = rospy.Publisher('keyframe', Odometry, queue_size=2) 

# ----------------------------------------------------------------------
# Global states
# ----------------------------------------------------------------------
ReadInOdometry = Odometry() 

# ----------------------------------------------------------------------
# Callback functions 
# ----------------------------------------------------------------------
def PosCallback (msg) : 
  global ReadInOdometry 
  # For turtlesim simulation -------------------------------------------
  # Put parameters to global Odometry state
  ReadInOdometry.pose.pose.position.x = msg.x
  ReadInOdometry.pose.pose.position.y = msg.y
  ReadInOdometry.twist.twist.linear.x = msg.linear_velocity * math.cos(msg.theta)
  ReadInOdometry.twist.twist.linear.y = msg.linear_velocity * math.sin(msg.theta)
  # TODO
  # For Shpero ---------------------------------------------------------
  # ReadInOdometry = msg

def CmdCallback (msg) : 
  global Pub 
  if msg.data == 'keep the frame' : 
    print('Frame kept: \n')
    # print(str(ReadInOdometry.pose.pose.position.x) + ', ' + str(ReadInOdometry.pose.pose.y) + '\n') 
    print(ReadInOdometry) 
    print('\n') 
    Pub.publish(ReadInOdometry)

# ----------------------------------------------------------------------
# Main routine 
# ----------------------------------------------------------------------
rate = rospy.Rate(10) 
while not rospy.is_shutdown() : 
  rate.sleep() 
