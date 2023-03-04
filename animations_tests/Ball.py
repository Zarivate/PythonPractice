# Separate class to handle all the ball adjustments, blueprint if you will
class Ball:
    # Need to pass in the canvas as well so can have something to alter
    def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coordinates = self.canvas.coords(self.image)
        # By printing out the coordinates we can see that there are 4 positions, two for the top left
        # and two for the bottom right
        print(coordinates)
        # Check to see if any corner is touched, specifically any left or right border
        if (coordinates[2] >= (self.canvas.winfo_width()) or coordinates[0] < 0):
            self.xVelocity = -self.xVelocity
        # Same idea but now for top and bottom borders
        if (coordinates[3] >= (self.canvas.winfo_height()) or coordinates[1] < 0):
            self.yVelocity = -self.yVelocity

        self.canvas.move(self.image, self.xVelocity, self.yVelocity)