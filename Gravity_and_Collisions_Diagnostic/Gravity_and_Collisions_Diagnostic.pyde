#Gravity and Collisions Diagnostic
#Written by Dylan Webb

#setup

from Game import Game
from Player import Player
from Platform import Platform
from Projectile import Projectile
from Enemy import Enemy

def setup():
    size(Game.screenW,Game.screenH)
    img = loadImage("work-01.png")
    background(img)
    frameRate(120)
    
#create objects

p1 = Player()

proj1 = Projectile()

game = Game()

plat1 = Platform(50,250,250,20,0)
plat2 = Platform(350,350,100,20,1)
plat3 = Platform(550,300,100,20,2)
plat4 = Platform(400,250,100,20,3)
plat5 = Platform(600,250,100,20,3)
plats = [plat1,plat2,plat3,plat4,plat5]

en1 = Enemy('tall',1)
en2 = Enemy('wide',2)
ens = [en1,en2]

def draw():
    img = loadImage("work-01.png")
    background(img)
    for i in plats:
        i.jump()
    p1.display()
    p1.movement()
    p1.death()
    for i in plats:
        i.collision()
        i.display()
    for i in ens:
        i.display()
        i.collision()
    proj1.display()
    proj1.collision()
    game.grav()
        