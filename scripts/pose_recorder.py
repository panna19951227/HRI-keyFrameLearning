#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose

#counter = 0
f = open('testfile10', 'w+')

def callback(data):
    global counter
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data)
    #newData = str(counter) + "," + str(data.x) + "," + str(data.y) + "," + str(data.theta) + "," + str(data.linear_velocity) + "," + str(data.angular_velocity)
    newData = str(data.x) + "," + str(data.y) + "," + str(data.theta)
    f.write(newData)
    f.write("\n")
    #counter = counter + 1
    print "Write to file"

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/turtle1/pose', Pose, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    f.close()

if __name__ == '__main__':
    listener()

