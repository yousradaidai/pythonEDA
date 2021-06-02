class Point:
    def __init__(self, x, y, z =0):
        self.x = x
        self.y = y
        self.z = z

    def ToString(self):
        if self.z:
            print('P({:.2f} , {:.2f} , {:.2f})'.format(self.x, self.y, self.z))
        else:
            print('P({:.2f} , {:.2f})'.format(self.x, self.y))

P1=Point(2,3)
P1.ToString()
# P(2.00 , 3.00)
P2=Point(1,-5,6)
P2.ToString()
# P(1.00 , -5.00 , 6.00)