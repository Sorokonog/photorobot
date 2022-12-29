class searcher():

    def __init__(self, p, m):
        self.photographer = p
        self.mover = m
        self.ball_has_been_found = False
        print("init done")

    def search_the_ball(self):
        while (not self.ball_has_been_found):
            x, area = self.photographer.process()
            if not area:
                print("Searching the ball")
                self.mover.rotate()
            else:
                self.ball_has_been_found = True
                print("The ball has been found at ", x, " with area = ", area)
        
        