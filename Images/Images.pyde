def setup():
    size(Game.screenW,Game.screenH)
    img = loadImage("work-01.png")
    background(img)
    
def display(self):
        stroke(255,0,0)
        img = loadImage("jerry2.png")
        image(img, Game.pX,Game.pY-Game.pH-63)