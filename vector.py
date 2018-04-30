from math import sqrt

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    # Prints out the value of the Vector
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    # Determines whether two defined vectors are equal
    def __eq__(self, v):
        return self.coordinates == v.coordinates

    # Add two vectors together
    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    # Subtract two vectors
    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    # Scale a vector
    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    # Get the magnitude of two vectors
    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    # Normalize a vector
    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1./magnitude)
        
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

my_vector = Vector([1,2,3])
print(my_vector)
my_vector2 = Vector([1,2,3])
my_vector3 = Vector([-1,2,3])
print(my_vector == my_vector2)
print(my_vector2 == my_vector3)

# adding two vectors
v = Vector([8.218,-9.341])
w = Vector([-1.129,2.111])
print(v.plus(w))

# subtracting two vectors
v = Vector([7.119,8.215])
w = Vector([-8.223,0.878])
print(v.minus(w))

# scaling a vector
v = Vector([1.671,-1.012,-0.318])
c = 7.41
print(v.times_scalar(c))

# Magnitude result
v = Vector([-0.221,7.437])
print(v.magnitude())

v = Vector([8.813, -1.331, -6.247])
print(v.magnitude())

v = Vector([5.581, -2.136])
print(v.normalized())

v = Vector([1.996, 3.108, -4.554])
print(v.normalized())


