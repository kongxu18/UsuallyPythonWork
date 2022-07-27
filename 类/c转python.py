import math


class Line(object):
    def __init__(self, Ax=None, Ay=None, Az=None, Bx=None, By=None, Bz=None):
        self.__tolerance = 1E-14
        self.Ax = Ax
        self.Ay = Ay
        self.Az = Az
        self.Bx = Bx
        self.By = By
        self.Bz = Bz

    def line3(self, **kwargs):
        if len(kwargs) == 1:
            other = kwargs.get('other')
            if getattr(other, 'set'):
                other.set()
        elif len(kwargs) == 2:
            Node3_nA = kwargs.get('Node3nA')
            Node3_nB = kwargs.get('Node3nB')
            self.Ay = Node3_nA.y
            self.Az = Node3_nA.z
            self.Bx = Node3_nB.x
            self.By = Node3_nB.y
            self.Bz = Node3_nB.z
        elif len(kwargs) == 6:
            nAx = kwargs.get('nAx')
            nAy = kwargs.get('nAy')
            nAz = kwargs.get('nAz')
            nBx = kwargs.get('nBx')
            nBy = kwargs.get('nBy')
            nBz = kwargs.get('nBz')

    def closestPoint(self, **kwargs):
        if len(kwargs) == 1:
            Node3_pt = kwargs.get('Node3pt')
            self.closestPoint(x=Node3_pt.x, y=Node3_pt.y, z=Node3_pt.z)

        if len(kwargs) == 3:
            x = kwargs.get('x')
            y = kwargs.get('y')
            z = kwargs.get('z')
            num2 = self.lengthSquared()
            if num2 < 1E-32:
                return 0.5
            return (((self.Ay - y) * (self.Ay - self.By)) - ((self.Ax - x) * (self.Bx - self.Ax))) / num2

    def distanceTo(self, **kwargs):
        if len(kwargs) == 1:
            Node3_pt = kwargs.get('Node3pt')
            self.distanceTo(x=Node3_pt.x, y=Node3_pt.y, z=Node3_pt.z)
        if len(kwargs) == 3:
            x = kwargs.get('x')
            y = kwargs.get('y')
            z = kwargs.get('z')
            math.sqrt(self.distanceToSquared(x=x, y=y, z=z))

    def distanceToSquared(self, **kwargs):
        if len(kwargs) == 1:
            Node3_pt = kwargs.get('Node3pt')
            self.distanceToSquared(x=Node3_pt.x, y=Node3_pt.y, z=Node3_pt.z)
        if len(kwargs) == 3:
            x = kwargs.get('x')
            y = kwargs.get('y')
            z = kwargs.get('z')

            t = self.closestPoint(x=x, y=y, z=z)
            return self.PointAt(t).DistanceSquared(x, y, z)

    @classmethod
    def duplicate(cls):
        return Line3(cls)

    def intersect(self, *args, **kwargs):
        if len(kwargs) == 3:
            A = kwargs.get('Line3A')
            B = kwargs.get('Line3B')
            t = kwargs.get('t')
            self.intersect(A.Ax, A.Ay, A.Az, A.Bx, A.By, A.Bz, B.Ax, B.Ay, B.Az, B.Bx, B.By, B.Bz, t)

        if len(kwargs) == 4:
            A = kwargs.get('Line3A')
            B = kwargs.get('Line3B')
            t0 = kwargs.get('t0')
            t1 = kwargs.get('t1')
            self.intersect(A.Ax, A.Ay, A.Az, A.Bx, A.By, A.Bz, B.Ax, B.Ay, B.Az, B.Bx, B.By, B.Bz, t0, t1)

        if args:
            Ax = args[0]
            Ay = args[1]
            Az = args[2]
            Bx = args[3]
            By = args[4]
            Bz = args[5]
            Cx = args[6]
            Cy = args[7]
            Cz = args[8]
            Dx = args[9]
            Dy = args[10]
            Dz = args[11]
            num = ((Dy - Cy) * (Bx - Ax)) - ((Dx - Cx) * (By - Ay))
            num2 = ((Dx - Cx) * (Ay - Cy)) - ((Dy - Cy) * (Ax - Cx))
            if len(args) == 13:
                t = args[12]
                if abs(num) < self.__tolerance:
                    num3 = ((Bx - Ax) * (Ay - Cy)) - ((By - Ay) * (Ax - Cx))
                    if ((abs(num2) < self.__tolerance) and (abs(num3) < self.__tolerance)):
                        return LineX.Coincident
                    return LineX.Parallel
                t = num2 / num
                return LineX.Point

            if len(args) == 14:
                t0 = args[12]
                t1 = args[13]
                num3 = ((Bx - Ax) * (Ay - Cy)) - ((By - Ay) * (Ax - Cx))
                if abs(num) < self.__tolerance:
                    if ((abs(num2) < self.__tolerance) and (abs(num3) < self.__tolerance)):
                        return LineX.Coincident
                    return LineX.Parallel
                t0 = num2 / num
                t1 = num3 / num
                return LineX.Point
    @property
    def length(self):
        return math.sqrt(self.lengthSquared())

    def lengthSquared(self):
        return (((self.Ax - self.Bx) * (self.Ax - self.Bx)) + ((self.Ay - self.By) * (self.Ay - self.By))) \
               + ((self.Az - self.Bz) * (self.Az - self.Bz))

    def PointAt(self,t):
        nX = self.Ax + (t * (self.Bx - self.Ax))
        nY = self.Ay + (t * (self.By - self.Ay))
        return Node3(nX, nY, self.Az + (t * (self.Bz - self.Az)), -1)


    def set(self,**kwargs):
        if len(kwargs) == 1:
            other = kwargs.get('other')
            self.Ax = other.Ax
            self.Ay = other.Ay
            self.Az = other.Az
            self.Bx = other.Bx
            self.By = other.By
            self.Bz = other.Bz
        elif len(kwargs) ==2:
            A = kwargs.get('Node3A')
            B = kwargs.get('Node3B')
            self.Ax = A.x
            self.Ay = A.y
            self.Az = A.z
            self.Bx = B.x
            self.By = B.y
            self.Bz = B.z

if __name__ == '__main__':
    line = Line(100,100,100,500,500,500)
    print(line.length)