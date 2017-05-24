from Game import Game

class Projectile(Game):
    
    # member variables
    projX = 0
    projY = 0
    projW = 5
    projH = 5
    speed = 3
    fire = False
    
    def __init__(self):
        pass
        
    def display(self):
        if mousePressed == True and self.fire == False:
            self.projX = Game.pX
            self.projY = Game.pY - Game.pH
            #calculate slope
            self.fire = True
        
        if self.fire == True:
            stroke(232,54,198)
            fill(0,0,255)
            ellipse(self.projX+50,self.projY-20,10,10)
            self.projX += self.speed
            
    def collision(self):
        #test for screen bounds
        if self.projX > Game.screenW or self.projX < 0 or self.projY > Game.screenH or \
            self.projY < 0:
                self.fire = False
                self.projX = Game.screenW/2
                self.projY = Game.screenH/2