def setup():
    size(200,200)
def draw():
    img = loadImage("texture.png")
    image(img*2,50,50)