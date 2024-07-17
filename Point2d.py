import math

class Point2D:
    def __init__(self, x, y):
        """
        Initializes a Point2D object with coordinates `x` and `y`.
        """
        self.x = x
        self.y = y

    def distance_to(self, other):
        """
        Computes the Euclidean distance between two Point2D objects.
        """
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __str__(self):
        """
        Returns a string representation of the Point2D object.
        """
        return f"({self.x}, {self.y})"

# Example usage:
point1 = Point2D(1, 2)
point2 = Point2D(4, 6)
print(f"Distance: {point1.distance_to(point2)}")
