from Game import Game

class Platform(Game):
    
    #member variables
    platX = 0
    platY = 0
    platW = 0
    platH = 0
    
    #for collision function
    topBound = False
    sideBound = False
    
    def __init__(self,platX,platY,platW,platH):
        self.platX = platX
        self.platY = platY
        self.platW = platW
        self.platH = platH
        self.color = 0
        
    def display(self):
        stroke(self.color)
        fill(self.color)
        rect(self.platX,self.platY,self.platW,self.platH)
        
    def collision(self):
        #check for top-collision with platform using boundaries
        if Game.pX >= (self.platX - Game.pW) and Game.pX <= (self.platX + self.platW) and \
            Game.pY <= self.platY and Game.pY >= (self.platY - abs(Game.gravity)*2.5):
            if self.topBound == False:
                Game.numCollide += 1
            self.topBound = True
        else:
            if self.topBound == True:
                Game.numCollide -= 1
            self.topBound = False
        
        #check for bound and jumping to activate gravity or not
        if Game.jump == False and self.topBound == True:
            Game.pY = self.platY
    
    def jump(self):
        if keyPressed:
            if key == 'w' or key == 'W':
                Game.momentum = True
                if Game.pY == self.platY and Game.jump == False:
                    Game.gravity = 4
                    Game.jump = True
                    
        #checks for whether or not character has landed  
        if Game.gravity < 1 and Game.jump == True and self.topBound == True:
                Game.jump = False
                Game.momentum = False