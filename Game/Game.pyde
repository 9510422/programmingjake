class Game():
    
    #global variables
    
    #player dimensions
    pX = 200
    pY = 200
    pW = 10
    pH = 10
    
    #gravity
    gravity = 0
    momentum = False
    jump = False
    
    #collisions
    numCollide = 0
    
    def __init__(self):
        pass
        
    def grav(self):
        if Game.jump == False and Game.numCollide > 0:
            Game.gravity = 0
        else:
            Game.gravity -= .1
            
        #catches player and respawns
        if Game.pY > 500:
            Game.pX = 200
            Game.pY = 200