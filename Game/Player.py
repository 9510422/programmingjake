from Game import Game

class Player(Game):
    
    #member variables
    speed = 2
    right = 0
    left = 0
    
    def __init__(self):
        pass
        
    def display(self):
        stroke(255,0,0)
        fill(255,0,0)
        Game.pX += (self.right-self.left)*self.speed
        Game.pY -= Game.gravity
        rect(Game.pX,Game.pY-Game.pH,Game.pW,Game.pH)
        if Game.momentum == False:
            self.left = 0
            self.right = 0
        
    def movement(self):
        if keyPressed:
            
            if key == 'a' or key == 'A':
                self.left = 1
                
            if key == 'd' or key == 'D':
                self.right = 1