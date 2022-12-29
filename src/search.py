class searcher():

    def __init__(self, p):
        self.photographer = p
        print("init done")

    def search_the_ball(self):
        print("The photo = ", self.photographer.picture)
        print("Searching the ball")
        print("The ball has been found")