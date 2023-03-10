import rospy

from navig import *
from search import *
from photo import *
from drop import *
from move import *

rospy.init_node("robot_photo")

x,y = 0.2, 0 

n = navigator()
d = dropper()
p = photographer()
m = mover(p)
s = searcher(p, m)

n.go(x,y)
s.search_the_ball()
m.move_to_the_ball()
m.turn_right_to_adjust_to_the_ball()
d.drop_the_mark()
m.move_back()
p.take_picture()
n.go(0,0)