class mover():

    def __init__(self, p):
        self.photographer = p

    def move_to_the_ball(self):
        print("The photo = ", self.photographer.picture)
        print("Moving to the ball")
        print("The ball has been reached")
    
    def turn_right_to_adjust_to_the_ball(self):
        print("The robot has turned")
    
    def move_back(self):
        print("Moving back")