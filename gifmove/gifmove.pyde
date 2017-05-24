add_library('gifAnimation')
#import gifAnimation
#Gif myAnimation:

def setup():
    size(400,400)
    myAnimation = Gif("samurai_idle_resize.gif",4)
    #myAnimation.play()


def draw():
    image(myAnimation, 10, 10)