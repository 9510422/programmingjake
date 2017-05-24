from Game import Game

class Platform(Game):

    # member variables
    tempX = 0
    platX = 0
    platY = 0
    platW = 0
    platH = 0

    # for collision function
    topBound = False
    sideBound = False

    def __init__(self, platX, platY, platW, platH, number):
        Game.platArray.extend((0,0,0))
        self.tempX = platX
        self.platY = platY
        self.platW = platW
        self.platH = platH
        Game.platArray[3*number] = platX
        Game.platArray[3*number+1] = platY
        Game.platArray[3*number+2] = platW
        self.color = 0

    def display(self):
        stroke(self.color)
        img = loadImage("stretch.png")
        #fill(self.color)
        self.platX = self.tempX + Game.scrollDis
        image(img, self.platX, self.platY, self.platW, self.platH)

    def collision(self):
        # check for top-collision with platform using boundaries
        if Game.pX >= (self.platX - Game.pW) and Game.pX <= (self.platX + self.platW) and \
                Game.pY <= self.platY and Game.pY >= (self.platY - abs(Game.gravity) * 2.5):
            if self.topBound == False:
                Game.numCollide += 1
            self.topBound = True
        else:
            if self.topBound == True:
                Game.numCollide -= 1
            self.topBound = False

        # check for bound and jumping to activate gravity or not
        if Game.jump == 0 and self.topBound == True:
            Game.pY = self.platY

    def jump(self):
        if keyPressed:
            if key == 'w' or key == 'W':
                if Game.pY == self.platY and Game.jump == 0:
                    Game.gravity = 4
                    Game.jump = 1
                    
        # checks for whether or not character has landed
        if Game.jump == 1:
            if Game.gravity < 0 and self.topBound == True:
                Game.jump = 0
            else:
                Game.scrollDis += Game.dir*Game.scrollSpeed