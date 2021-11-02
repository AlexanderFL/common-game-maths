from Vector import Vector

# Class represents a single point in 3d space
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Add two points together
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    # Subtracts two points
    def __sub__(self, other) -> Vector:
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)