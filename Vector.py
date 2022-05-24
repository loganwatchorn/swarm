from math import degrees, radians, tan, atan, sin, cos, sqrt


class Vector:
    def __init__(self, x=0, y=0, deg=None):
        self._precision = 5
        self.x = x
        self.y = y

        if deg is not None:
            if deg != 90 and deg != 270:
                self.x = -1 if 90 < deg and deg < 270 else 1
                self.y = tan(radians(deg)) * self.x
            else:
                self.y = 1 if deg == 90 else -1

        self.normalize()


    def _simplify(self):
        x = round(self.x, self._precision)
        x_int = round(x)
        self.x = x if x != x_int else x_int

        y = round(self.y, self._precision)
        y_int = round(y)
        self.y = y if y != y_int else y_int


    def is_zero(self):
        return self.x == 0 and self.y == 0


    def get_magnitude(self):
        # L2 norm (Euclidean)
        # return sqrt(self.x ** 2 + self.y ** 2)

        # L_infty norm (Grid)
        return max(abs(self.x), abs(self.y))


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
        self._simplify()


    def add(self, v):
        self.x += v.x
        self.y += v.y
        self._simplify()


    def normalize(self):
        self.multiply(1 / self.get_magnitude())


    def rotate(self, deg):
        if self.is_zero():
            return

        magnitude = self.get_magnitude()
        new_angle = self.get_angle() + radians(deg)

        self.x = cos(new_angle)
        self.y = sin(new_angle)

        self.multiply(magnitude / self.get_magnitude())


    def output(self):
        s = f'({self.x}, {self.y})'

        if not self.is_zero():
            s += f', {self.get_magnitude()} @ {degrees(self.get_angle())} deg'

        print(s)




# for i in range(0, 8):
#     vector = Vector(deg = i * 45)
#     vector.output()
#     vector.rotate(45)
#     vector.output()
#     print()
