import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

class navigator():

    def go(self, x, y):
        print("Moving to ", x, " ", y)
        client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        client.wait_for_server()
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = x # Координаты в системе отсчета карты
        goal.target_pose.pose.position.y = y # (0,0) - точка включения навигации
        goal.target_pose.pose.orientation.w = 1.0

        client.send_goal(goal)
        client.wait_for_result()