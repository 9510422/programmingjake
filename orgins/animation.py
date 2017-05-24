#import gifAnimation.*:
class animation():
    images = []
    imageCount = 0
    frame = 0
  
    def __init__(self,imagePrefix,count):
        self.imageCount = count
        self.images = [int]*self.imageCount

        i = 0
        while i < self.imageCount:
            # Use nf() to number format 'i' into four digits
            filename = str(imagePrefix + str(nf(i, 4)) + ".gif")
            self.images[i] = loadImage(filename)
            i += 1

    def display(self,xpos, ypos):
        self.frame = (self.frame+1) % self.imageCount
        image(self.images[self.frame], xpos, ypos)
  
  
    def getWidth(self) :
        return self.images(0).width
  