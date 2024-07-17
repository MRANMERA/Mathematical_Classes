import math

class Fraction:
    # Initialize the fraction with numerator `n` and denominator `d`, simplifying it if possible.
    def __init__(self, n, d):
        if d == 0:
            raise ValueError("Denominator cannot be zero")  # Handle the case where the denominator is zero.
        self.n = n
        self.d = d
        self.simplify()

    # Return a string representation of the fraction in the format "n/d".
    def __str__(self):
        return f"{self.n}/{self.d}"

    # Perform addition of two fractions and return a new Fraction object as the result.
    def __add__(self, other):
        temp_num = self.n * other.d + other.n * self.d
        temp_den = self.d * other.d
        return Fraction(temp_num, temp_den)

    # Perform subtraction of two fractions and return a new Fraction object as the result.
    def __sub__(self, other):
        temp_num = self.n * other.d - other.n * self.d
        temp_den = self.d * other.d
        return Fraction(temp_num, temp_den)

    # Perform multiplication of two fractions and return a new Fraction object as the result.
    def __mul__(self, other):
        temp_num = self.n * other.n
        temp_den = self.d * other.d
        return Fraction(temp_num, temp_den)

    # Perform true division of two fractions and return a new Fraction object as the result.
    def __truediv__(self, other):
        if other.n == 0:
            raise ValueError("Cannot divide by a fraction with a numerator of zero")  # Handle division by zero error.
        temp_num = self.n * other.d
        temp_den = self.d * other.n
        return Fraction(temp_num, temp_den)

    # Simplify the fraction using the greatest common divisor (GCD).
    def simplify(self):
        gcd = math.gcd(self.n, self.d)
        self.n //= gcd
        self.d //= gcd

x = Fraction(6, 7)
y = Fraction(2, 3)
print(x + y)  # Output: 32/21

z = Fraction(1, 0)  # This will raise a ValueError due to division by zero
