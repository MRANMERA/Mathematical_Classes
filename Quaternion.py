class Quaternion:
    def __init__(self, w, x, y, z):
        """
        Initializes a Quaternion object with components `w`, `x`, `y`, and `z`.
        """
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        """
        Adds two Quaternion objects and returns a new Quaternion object with the result.
        """
        return Quaternion(self.w + other.w, self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """
        Subtracts one Quaternion object from another and returns a new Quaternion object with the result.
        """
        return Quaternion(self.w - other.w, self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        """
        Multiplies two Quaternion objects and returns a new Quaternion object with the result.
        """
        w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
        x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
        y = self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x
        z = self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w
        return Quaternion(w, x, y, z)

    def __str__(self):
        """
        Returns a string representation of the Quaternion object.
        """
        return f"{self.w} + {self.x}i + {self.y}j + {self.z}k"

# Example usage:
q1 = Quaternion(1, 2, 3, 4)
q2 = Quaternion(5, 6, 7, 8)
print(q1 + q2)  # Output: 6 + 8i + 10j + 12k
