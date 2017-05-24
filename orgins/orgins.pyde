#add_library('gifAnimation')
#import gifAnimation
from animation import animation

def setup():
    size(700,400)
    frameRate(20)
    animation1 = animation("samurai_idle_resize", 6)
    
def draw():
     img = loadImage("work.png")
     background(img)
     #animation1.display(30,30)
     ima = loadImage("samurai_idle_dude.gif")
     imageMode(CENTER)
     image(ima, mouseX, mouseY)