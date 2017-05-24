class Game():
    
    #global variables
    
    #screen scrolling
    scrollDis = 0
    scrollSpeed = .5
    dir = 0
    screenW = 700
    screenH = 400
    
    #player
    spawnX = 200
    spawnY = 200
    pX = spawnX
    pY = spawnY
    pW = 10
    pH = 10
    pDeath = False
    
    #gravity
    gravity = 0
    jump = 0
    
    #collisions
    numCollide = 0
    
    #platform array
    platArray = []
    
    def __init__(self):
        pass
        
    def grav(self):
        if Game.jump == 0 and Game.numCollide > 0:
            Game.gravity = 0
        else:
            Game.gravity -= .1