from math import degrees, radians, tan, atan, sin, cos, sqrt


class Vector:
    def __init__(self, x=0, y=0, deg=None, magnitude=None):
        self._precision = 5
        self.x = x
        self.y = y

        self._simplify()

        if deg is not None:
            if deg != 90 and deg != 270:
                self.x = -1 if 90 < deg and deg < 270 else 1
                self.y = tan(radians(deg)) * self.x
            else:
                self.y = 1 if deg == 90 else -1

            self.normalize()

        if magnitude:
            self *= magnitude


    def _simplify_number(self, number):
        n = round(number, self._precision)
        n_int = round(n)
        return n if n != n_int else n_int


    def _simplify(self):
        self.x = self._simplify_number(self.x)
        self.y = self._simplify_number(self.y)


    def is_zero(self):
        return self.x == 0 and self.y == 0


    def get_magnitude(self):
        # L2 norm (Euclidean)
        # return sqrt(self.x ** 2 + self.y ** 2)

        # L_infty norm (Grid)
        return self._simplify_number(max(abs(self.x), abs(self.y)))


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

    def __mul__(self, other):
        c = round(other, self._precision)
        x = self.x * c
        y = self.y * c
        return Vector(x, y)

    def __rmul__(self, other):
        return self.__mul__(other)


    def add(self, v, debug=False):
        if debug:
            print(f'self: {self}')
            print(f'v: {v}')
            print("add")
        self.x += v.x
        self.y += v.y
        if debug:
            print(f'self: {self}')
            print("simplify")
        self._simplify()
        if debug:
            print(f'self: {self}')

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)


    def normalize(self):
        self *= 1 / self.get_magnitude()


    def rotate(self, deg):
        if self.is_zero():
            return

        magnitude = self.get_magnitude()
        new_angle = self.get_angle() + radians(deg)

        self.x = cos(new_angle)
        self.y = sin(new_angle)

        self *= magnitude / self.get_magnitude()


    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'


    def debug(self):
        s = f'({self.x}, {self.y})'

        if not self.is_zero():
            s += f', {self.get_magnitude()} @ {degrees(self.get_angle())} deg'

        print(s)




# for i in range(0, 8):
#     vector = Vector(deg = i * 45)
#     vector.debug()
#     vector.rotate(45)
#     vector.debug()
#     print()
