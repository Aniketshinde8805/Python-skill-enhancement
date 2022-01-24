class Square:
    def area(self,side):
        self.side=side
        print(self.side*self.side)

class Cricle(Square):
    def area(self,radius):
        self.radius=radius
        print(3.142*self.radius**2)

cc=Cricle()
cc.area(4)

ss=Square()
ss.area(4)
