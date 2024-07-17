class ComplexNumber:
    def __init__(self, real, imag):
        """
        Initializes a complex number with a real part `real` and an imaginary part `imag`.
        """
        self.real = real
        self.imag = imag

    def __add__(self, other):
        """
        Adds two complex numbers and returns a new ComplexNumber object with the sum.
        """
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        """
        Subtracts two complex numbers and returns a new ComplexNumber object with the difference.
        """
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        """
        Multiplies two complex numbers using the formula (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        and returns a new ComplexNumber object with the product.
        """
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        """
        Divides two complex numbers using the formula (a + bi) / (c + di) = ((ac + bd) / (c^2 + d^2))
        + ((bc - ad) / (c^2 + d^2))i and returns a new ComplexNumber object with the quotient.
        """
        denom = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real, imag)

    def __str__(self):
        """
        Returns a string representation of the complex number in the format "real + imagi".
        """
        return f"{self.real} + {self.imag}i"

# Example usage:
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 4)
print(c1 + c2)  # Output: 3 + 7i
