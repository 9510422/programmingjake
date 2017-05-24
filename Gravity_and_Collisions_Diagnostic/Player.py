from Game import Game

class Player(Game):
    
    #member variables
    
    def __init__(self):
        pass
        
    def display(self):
        stroke(255,0,0)
        img = loadImage("jerry2.png")
        #fill(255,0,0)
        Game.pY -= Game.gravity
        image(img, Game.pX,Game.pY-Game.pH-63)
        if Game.jump == 0:
            Game.dir = 0
                
    def movement(self):
        if keyPressed and Game.jump == 0:
            if key == 'a' or key == 'A':
                Game.dir = 1
                Game.scrollDis += Game.dir*Game.scrollSpeed*4
                fill(255)
                #img = loadImage("apple.png")
                #image(img, Game.pX,Game.pY-Game.pH-63)
                
            if key == 'd' or key == 'D':
                Game.dir = -1
                Game.scrollDis += Game.dir*Game.scrollSpeed*4
                
    def death(self):
        #catches player and respawns
        if Game.pDeath == True or Game.pY > 500:
            Game.scrollDis = 0
            Game.pX = Game.spawnX
            Game.pY = Game.spawnY
            Game.jump = 0
            Game.pDeath = False