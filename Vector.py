class Vector:
    def __init__(self, x, y):
        """
        Initializes a Vector object with coordinates `x` and `y`.
        """
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        Adds two Vector objects and returns a new Vector object with the result.
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Subtracts one Vector object from another and returns a new Vector object with the result.
        """
        return Vector(self.x - other.x, self.y - other.y)

    def dot(self, other):
        """
        Computes the dot product of two Vector objects.
        """
        return self.x * other.x + self.y * other.y

    def __str__(self):
        """
        Returns a string representation of the Vector object.
        """
        return f"<{self.x}, {self.y}>"

# Example usage:
vec1 = Vector(1, 2)
vec2 = Vector(3, 4)
print(vec1 + vec2)        # Output: <4, 6>
print(vec1.dot(vec2))     # Output: 11
