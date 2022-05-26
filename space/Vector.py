from math import degrees, radians, tan, atan, sin, cos, sqrt
from collections.abc import Sequence


class Vector(Sequence):
    def __init__(self, elems=None, angles=None, magnitude=None):
        elems = elems or [0, 0]

        if angles is not None:
            angle = angles[0]
            if angle != 90 and angle != 270:
                elems[0] = -1 if 90 < angle and angle < 270 else 1
                elems[1] = tan(radians(angle)) * elems[0]
            else:
                elems[1] = 1 if angle == 90 else -1

        self.elems = elems
        super().__init__()
        self.norm = "L_infty"
        self.precision = 5

        if angles is not None:
            self.resize(magnitude or 1)
        else:
            self._simplify()


    def __getitem__(self, i):
        return self.elems[i]

    def __len__(self):
        return len(self.elems)

    def __mul__(self, other):
        c = simplify_number(c, self.precision)
        return Vector([elem * c for elem in self])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        precision = min(self.precision, other.precision)
        return Vector([self[i] + other[i] for i in range(0, len(self))])

    def __repr__(self) -> str:
        s = f'({self[0]}, {self[1]})'

        if not self.is_zero():
            s += f', {self.magnitude()} @ {self.get_angle()} deg'

        return s


    def _simplify(self):
        for i in range(0, len(self)):
            self.elems[i] = simplify_number(self.elems[i], self.precision)


    def is_zero(self):
        return not any([elem != 0 for elem in self])


    def magnitude(self):
        if self.norm == "L1": # Manhattan space
            norm = sum([abs(elem) for elem in self])
        elif self.norm == "L2": # Euclidean space
            norm = sqrt(sum([elem ** 2 for elem in self]))
        elif self.norm == "L_infty": # Grid space
            norm = max([abs(elem) for elem in self])

        return simplify_number(norm, self.precision)


    def resize(self, magnitude):
        scale_factor = magnitude / self.magnitude()
        for i in range(0, len(self)):
            self.elems[i] *= scale_factor
        self._simplify()


    def get_angle(self):
        if self.is_zero():
            return None

        if self[0] == 0:
            return 90 if self[1] > 0 else 270
        else:
            relative_angle = degrees(atan(self[1] / self[0]))

            if self[0] < 0:
                return 180 + relative_angle
            elif self[1] < 0:
                return 360 + relative_angle
            else:
                return relative_angle


    def rotate(self, angle):
        if self.is_zero():
            return

        magnitude = self.magnitude()
        new_angle = self.get_angle() + angle

        self[0] = cos(radians(new_angle))
        self[1] = sin(radians(new_angle))

        self.resize(magnitude)



def simplify_number(number, precision):
    n = round(number, precision)
    n_int = round(n)
    return n if n != n_int else n_int


class A(Sequence):
    def __init__(self, l):
        self.l = l
        super().__init__()

    def __getitem__(self, i):
        return self.l[i]

    def __len__(self):
        return len(self.l)


# a = A([1,2,3])
# try:
#     for i,_ in enumerate(a):
#         print(a[i])
#     for elem in a:
#         print(elem)
# except Exception:
#     print("Gah! No good!")
#     raise
