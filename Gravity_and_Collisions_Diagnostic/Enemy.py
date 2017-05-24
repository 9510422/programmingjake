from Game import Game

class Enemy(Game):
    
    #member variables
    eX = 0
    eY = 0
    eW = 0
    eH = 0
    type = str
    #colors
    c1 = 0
    c2 = 0
    c3 = 0
    def __init__(self,enemyType,number):
        self.type = enemyType
        if self.type == 'tall':
            self.c1 = 0
            self.c2 = 255
            self.c3 = 255
            self.eH = 30
            self.eW = 10
        elif self.type == 'wide':
            self.c1 = 255
            self.c2 = 0
            self.c3 = 255
            self.eH = 10
            self.eW = 30
        self.eX = Game.platArray[3*number] + Game.platArray[3*number+2] - self.eW - 10
        self.eY = Game.platArray[3*number+1] - self.eH - 1
        
    def display(self):
        stroke(self.c1,self.c2,self.c3)
        fill(self.c1,self.c2,self.c3)
        rect(self.eX+Game.scrollDis,self.eY,self.eW,self.eH)
        
    def collision(self):
        if (Game.pX + Game.pW) >= self.eX+Game.scrollDis and Game.pX <= (self.eX+Game.scrollDis + self.eW) \
        and (Game.pY + Game.pH) >= self.eY and Game.pY <= (self.eY + self.eH):
            Game.pDeath = True