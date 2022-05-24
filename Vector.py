from math import degrees, radians, tan, atan, sin, cos, sqrt


class Vector:
    def __init__(self, x=0, y=0, deg=None):
        self.x = x
        self.y = y

        if deg is not None:
            if deg != 90 and deg != 270:
                self.x = 1
                self.y = tan(radians(deg))
            else:
                self.y = 1 if deg == 90 else -1


    def is_zero(self):
        return self.x == 0 and self.y == 0


    def get_magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2)


    def get_angle(self):
        if self.is_zero():
            return None

        if self.x == 0:
            return radians(90 if self.y > 0 else 270)
        else:
            relative_angle = atan(self.y / self.x)

            if self.x < 0:
                return radians(180) + relative_angle
            elif self.y < 0:
                return radians(360) + relative_angle
            else:
                return relative_angle


    def multiply(self, c):
        self.x *= c
        self.y *= c


    def add(self, v):
        self.x += v.x
        self.y += v.y


    def rotate(self, deg):
        if self.is_zero():
            return

        magnitude = self.get_magnitude()
        new_angle = self.get_angle() + radians(deg)

        self.x = magnitude * cos(new_angle)
        self.y = magnitude * sin(new_angle)


    def baseify(self):
        self.x = round(self.x)
        self.y = round(self.y)



    def output(self):
        s = f'({self.x}, {self.y})'

        if not self.is_zero():
            s += f', {self.get_magnitude()} @ {degrees(self.get_angle())} deg'

        print(s)


# for x in range(-1, 2):
#     for y in range(-1, 2):
#         vector = Vector(x, y)
#         vector.output()
#         vector.rotate(45)
#         vector.output()
#         vector.baseify()
#         vector.output()
#         print()
