from Game import Game
from Player import Player
from Platform import Platform

def setup():
    size(500,500)
    background(255)
    frameRate(120)
    
#create objects

p1 = Player()

game = Game()

plat1 = Platform(50,400,250,20)
plat2 = Platform(350,350,100,20)
plat3 = Platform(350,300,100,20)
plat4 = Platform(350,250,100,20)
plats = [plat1,plat2,plat3,plat4]

def draw():
    background(255)
    for i in plats:
        i.jump()
    p1.display()
    p1.movement()
    for i in plats:
        i.collision()
        i.display()
    game.grav()