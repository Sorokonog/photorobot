import rospy
import cv2
import numpy as np
import math
from sensor_msgs.msg import CompressedImage

class photographer():

    picture = [1]
    yellowLower = (100, 180, 80) # dark
    yellowUpper = (120, 255, 255) # light

    def __init__(self):
        rospy.Subscriber("/front_camera/image_raw/compressed", CompressedImage, self.cb_video_capture)

    def take_picture(self):
        cv2.imwrite("/home/pi/photorobot/photo/sharik.jpg", self.picture)
        print("The picture taken")

    def cb_video_capture(self, image_msg):
        np_arr = np.frombuffer(image_msg.data, np.uint8)
        self.picture = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    def process(self):
        hsv = cv2.cvtColor(self.picture, cv2.COLOR_RGB2HSV)
        self.mask = cv2.inRange(hsv, self.yellowLower, self.yellowUpper)
        Moments = cv2.moments(self.mask)
        if Moments["m00"]:
            x = int(Moments["m10"] / Moments["m00"])
            return x, Moments["m00"] / 256
        else:
            return  0, 0
