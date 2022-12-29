import rospy
from geometry_msgs.msg import Twist

class mover():

    def __init__(self, p):
        self.photographer = p
        self.pub = rospy.Publisher("cmd_vel", Twist, queue_size = 10)
        self.vel = Twist()
        self.ball_has_been_reached = False
        self.area_size = 11000
        self.Kp = 1 / 400

    def move_to_the_ball(self):
        print("Moving to the ball")
        while not self.ball_has_been_reached:
            x, area = self.photographer.process()
            if area > self.area_size:
                self.ball_has_been_reached = True
                self.vel = Twist()
                print("The ball has been reached with area size= ", area)
            else:
                self.vel.linear.x = 0.05
                self.vel.angular.z = (320 - x) * self.Kp
                print(area)
            self.pub.publish(self.vel)
            rospy.sleep(0.05)
    
    def turn_right_to_adjust_to_the_ball(self):
        print("The robot has turned")
    
    def move_back(self):
        print("Moving back")

    def rotate(self):
        self.vel.angular.z = 0.1
        self.pub.publish(self.vel)