from math import sqrt, acos, pi
from decimal import getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = 'No unique parallel component'
    NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG = 'No unique orthogonal component'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([x for x in coordinates])
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
            return self.times_scalar(1/magnitude)
        
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')
    
    # Compute the dot product
    def dot(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    # Compute angle with
    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            angle_in_radians = acos(u1.dot(u2))

            if in_degrees:
                degrees_per_radian = 180. / pi 
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e
    
    # Compute whether or not our vectors are orthogonal
    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    # Computer whether or not our vectors are parallel
    def is_parallel_to(self, v):
        return (self.is_zero() or v.is_zero() or self.angle_with(v) == 0 or self.angle_with(v) == pi)

    # Is our vector a zero vector
    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    # Computing orthogonal projections
    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return self.minus(projection)

        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e

    # Computing parallel projects
    def component_parallel_to(self, basis):
        try:
            u = basis.normalized()
            weight = self.dot(u)
            return u.times_scalar(weight)
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e
    

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

# Normalization calculation
v = Vector([5.581, -2.136])
print(v.normalized())

v = Vector([1.996, 3.108, -4.554])
print(v.normalized())

# Dot Product calculation
v = Vector([7.887, 4.138])
w = Vector([-8.802, 6.776])
print(v.dot(w))

# Angle_with calculation
v = Vector([3.183, -7.627])
w = Vector([-2.668, 5.319])
print(v.angle_with(w))

v = Vector([7.35, 0.221, 5.188])
w = Vector([2.751, 8.259, 3.985])
print(v.angle_with(w, in_degrees=True))

# Parallel and Orthogonal calculations
v = Vector([-7.579, -7.88])
w = Vector([22.737,23.64])
print('is parallel: ', v.is_parallel_to(w))
print('is orthogonal: ' + v.is_orthogonal_to(w))
