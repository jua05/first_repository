class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __mul__(self, num):
        return Point(self.x*num,self.y*num)

    def __rmul__(self, num):
        return Point(self.x*num, self.y*num)

    def __str__(self):
        return f"({self.x},{self.y})"
    def ICD(self):
        a = self.x + self.y
        return a

pt1 = Point(1,2)
pt2 = Point(3,4)
pt3 = pt1*10 #x,y 각각 10을 곱함 => pt1.__mul__(10)
pt4 = -10 * pt2
pt5 = 333+111
pt6 = 2 * pt1
print(pt6)
pt7 = Point.ICD(pt1)
print(pt7)

print(pt1)
print(pt2)
print(pt3)
print(pt4)