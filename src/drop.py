import rospy
from std_msgs.msg import Int16

class dropper():

    def __init__(self):
        self.pub = rospy.Publisher("servo1_cmd_echo", Int16, queue_size = 10)
        self.command = Int16()

    def drop_the_mark(self):
        self.command.data = 1
        self.pub.publish(self.command)
        rospy.sleep(1)
        self.command.data = 0
        self.pub.publish(self.command)
        print("The mark has been dropped")

