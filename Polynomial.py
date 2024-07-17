class Polynomial:
    def __init__(self, coefficients):
        """
        Initializes a Polynomial object with coefficients provided in a list.
        Coefficients are ordered from highest degree to lowest degree.
        """
        self.coefficients = coefficients

    def __add__(self, other):
        """
        Adds two Polynomial objects and returns a new Polynomial object with the result.
        """
        # Determine the longer and shorter list of coefficients
        if len(self.coefficients) > len(other.coefficients):
            coeffs = [a + b for a, b in zip(self.coefficients, [0]*(len(self.coefficients) - len(other.coefficients)) + other.coefficients)]
        else:
            coeffs = [a + b for a, b in zip([0]*(len(other.coefficients) - len(self.coefficients)) + self.coefficients, other.coefficients)]
        return Polynomial(coeffs)

    def __sub__(self, other):
        """
        Subtracts two Polynomial objects and returns a new Polynomial object with the result.
        """
        # Determine the longer and shorter list of coefficients
        if len(self.coefficients) > len(other.coefficients):
            coeffs = [a - b for a, b in zip(self.coefficients, [0]*(len(self.coefficients) - len(other.coefficients)) + other.coefficients)]
        else:
            coeffs = [a - b for a, b in zip([0]*(len(other.coefficients) - len(self.coefficients)) + self.coefficients, other.coefficients)]
        return Polynomial(coeffs)

    def __str__(self):
        """
        Returns a string representation of the Polynomial object in a human-readable format.
        """
        terms = []
        # Iterate through coefficients in reverse order (from highest degree to lowest)
        for power, coeff in enumerate(reversed(self.coefficients)):
            if coeff:
                # Format each term based on its power
                terms.append(f"{coeff}x^{power}" if power else f"{coeff}")
        # Join terms with "+" and return the polynomial as a string
        return " + ".join(reversed(terms))

# Example usage:
p1 = Polynomial([1, 2, 3])  # Represents x^2 + 2x + 3
p2 = Polynomial([3, 4])     # Represents 3x + 4
print(p1 + p2)  # Output: x^2 + 5x + 7
