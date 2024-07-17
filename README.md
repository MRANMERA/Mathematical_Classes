# Mathematical Classes and Probability Distributions in Python

## Object-Oriented Programming and Classes in Python

### Introduction to OOP

Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to design applications and programs. Each object is an instance of a class, which defines a blueprint for creating objects with specific properties (attributes) and behaviors (methods). OOP promotes modularity, reusability, and efficient problem-solving by organizing code into manageable and reusable components.

#### Benefits of OOP in Python:
- **Modularity**: Encapsulation allows hiding the complexity of implementation.
- **Reusability**: Classes and objects can be reused in different parts of the program.
- **Flexibility**: Easily modify and update existing code without affecting other parts of the program.
- **Scalability**: Allows building large and complex applications more effectively.
- **Maintenance**: Simplifies maintenance by dividing the code into smaller, manageable pieces.

## Mathematical Classes Implemented

# 1.) Fraction Class

## Concept

The `Fraction` class represents fractions with a numerator (`n`) and denominator (`d`). It provides methods for arithmetic operations such as addition, subtraction, multiplication, and division of fractions.

## Example

```python
x = Fraction(6, 7)
y = Fraction(2, 3)
print(x + y)  # Output: 32/21
```
__init__(self, n, d)
- Initializes a Fraction object with a numerator n and a denominator d.
- Checks if d is zero to avoid division by zero errors.
- Calls the simplify() method to reduce the fraction to its simplest form using the greatest common divisor (GCD).

__str__(self)
- Returns a string representation of the fraction in the format "n/d".
- Provides a human-readable output when printing or converting the Fraction object to a string.
  
__add__(self, other)
- Performs addition of two fractions (self and other) and returns a new Fraction object with the result.
- Uses the formula (a/b) + (c/d) = (a*d + c*b) / (b*d) to compute the sum.

__sub__(self, other)
- Performs subtraction of two fractions (self and other) and returns a new Fraction object with the result.
- Uses the formula (a/b) - (c/d) = (a*d - c*b) / (b*d) to compute the difference.

__mul__(self, other)
- Performs multiplication of two fractions (self and other) and returns a new Fraction object with the result.
- Uses the formula (a/b) * (c/d) = (a*c) / (b*d) to compute the product.

__truediv__(self, other)
- Performs true division of two fractions (self divided by other) and returns a new Fraction object with the result.
- Raises a ValueError if other has a numerator of zero to prevent division by zero errors.
- Uses the formula (a/b) / (c/d) = (a*d) / (b*c) to compute the quotient.

simplify(self)
- Simplifies the fraction by dividing both the numerator n and the denominator d by their greatest common divisor (GCD).
- Ensures that fractions are always represented in their simplest form.

# 2.) ComplexNumber Class

## Concept

The `ComplexNumber` class models complex numbers (`a + bi`) with real (`real`) and imaginary (`imag`) parts. It supports basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Example

```python
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 4)
print(c1 + c2)  # Output: 3 + 7i
```
# 3.) Polynomial Class

## Concept

The `Polynomial` class represents polynomials with coefficients (`coefficients`) stored in a list. It supports addition and subtraction of polynomials.

## Example

```python
p1 = Polynomial([1, 2, 3])  # x^2 + 2x + 3
p2 = Polynomial([3, 4])     # 3x + 4
print(p1 + p2)  # Output: x^2 + 5x + 7
```
# 4.) Matrix Class

## Concept

The `Matrix` class represents matrices with operations like addition, subtraction, and multiplication.

## Example

```python
matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6], [7, 8]])
print(matrix1 + matrix2)
```
# 5.) Vector Class

## Concept

The `Vector` class models 2D vectors (`x` and `y` components). It supports addition, subtraction, and dot product operations.

## Example

```python
vec1 = Vector(1, 2)
vec2 = Vector(3, 4)
print(vec1 + vec2)  # Output: <4, 6>
print(vec1.dot(vec2))  # Output: 11
```
# 6.) Point2D Class

## Concept

The `Point2D` class represents points in a 2D Cartesian coordinate system (`x` and `y` coordinates). It calculates distances between points.

## Example

```python
point1 = Point2D(1, 2)
point2 = Point2D(4, 6)
print(f"Distance: {point1.distance_to(point2)}")
```
# 7.) Quaternion Class

## Concept

The `Quaternion` class models quaternions (`w + xi + yj + zk`). It supports addition, subtraction, and multiplication operations.

## Example

```python
q1 = Quaternion(1, 2, 3, 4)
q2 = Quaternion(5, 6, 7, 8)
print(q1 + q2)  # Output: 6 + 8i + 10j + 12k
```
# 8.) ProbabilityDistribution Class

## Concept

The `ProbabilityDistribution` class models discrete and continuous probability distributions. It supports sampling, expected value, variance, standard deviation, moments, and plotting.

## Example

```python
# Example usage for discrete distribution (Binomial distribution)
binom_dist = ProbabilityDistribution.binomial(n=10, p=0.5)
print(binom_dist)
print("Sample:", binom_dist.sample())
binom_dist.plot()
```


