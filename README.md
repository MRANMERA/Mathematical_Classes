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
-> __init__(self, n, d)
- Initializes a Fraction object with a numerator n and a denominator d.
- Checks if d is zero to avoid division by zero errors.
- Calls the simplify() method to reduce the fraction to its simplest form using the greatest common divisor (GCD).

-> __str__(self)
- Returns a string representation of the fraction in the format "n/d".
- Provides a human-readable output when printing or converting the Fraction object to a string.
  
-> __add__(self, other)
- Performs addition of two fractions (self and other) and returns a new Fraction object with the result.
- Uses the formula (a/b) + (c/d) = (a*d + c*b) / (b*d) to compute the sum.

-> __sub__(self, other)
- Performs subtraction of two fractions (self and other) and returns a new Fraction object with the result.
- Uses the formula (a/b) - (c/d) = (a*d - c*b) / (b*d) to compute the difference.

-> __mul__(self, other)
- Performs multiplication of two fractions (self and other) and returns a new Fraction object with the result.
- Uses the formula (a/b) * (c/d) = (a*c) / (b*d) to compute the product.

-> __truediv__(self, other)
- Performs true division of two fractions (self divided by other) and returns a new Fraction object with the result.
- Raises a ValueError if other has a numerator of zero to prevent division by zero errors.
- Uses the formula (a/b) / (c/d) = (a*d) / (b*c) to compute the quotient.

-> simplify(self)
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
-> __init__(self, real, imag)

- Initializes a complex number with a real part real and an imaginary part imag.
- Stores these values as instance variables (self.real and self.imag).

-> Arithmetic Operations:
- __add__(self, other): Performs addition of two complex numbers and returns a new ComplexNumber object with the sum of their real and imaginary parts.
- __sub__(self, other): Performs subtraction of two complex numbers and returns a new ComplexNumber object with the difference of their real and imaginary parts.
- __mul__(self, other): Performs multiplication of two complex numbers using the formula (a + bi) * (c + di) = (ac - bd) + (ad + bc)i.
- __truediv__(self, other): Performs division of two complex numbers using the formula (a + bi) / (c + di) = ((ac + bd) / (c^2 + d^2)) + ((bc - ad) / (c^2 + d^2))i.

-> __str__(self)
- Returns a string representation of the complex number in the format "real + imagi".

# 3.) Polynomial Class

## Concept

The `Polynomial` class represents polynomials with coefficients (`coefficients`) stored in a list. It supports addition and subtraction of polynomials.

## Example

```python
p1 = Polynomial([1, 2, 3])  # x^2 + 2x + 3
p2 = Polynomial([3, 4])     # 3x + 4
print(p1 + p2)  # Output: x^2 + 5x + 7
```
-> __init__(self, coefficients)
- Initializes a Polynomial object with a list of coefficients.
- Coefficients are provided in order from the highest degree to the lowest degree.
 
-> __add__(self, other)
- Adds two Polynomial objects (self and other) and returns a new Polynomial object with the result.
- Handles cases where polynomials have different lengths by aligning coefficients appropriately.

-> __sub__(self, other)
- Subtracts one Polynomial object (other) from another (self) and returns a new Polynomial object with the result.
- Handles cases where polynomials have different lengths by aligning coefficients appropriately.

-> __str__(self)
- Returns a string representation of the Polynomial object in a human-readable format.
- Formats each term based on its coefficient and power, omitting terms with zero coefficients.

# 4.) Matrix Class

## Concept

The `Matrix` class represents matrices with operations like addition, subtraction, and multiplication.

## Example

```python
matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6], [7, 8]])
print(matrix1 + matrix2)
```
-> __init__(self, data)
- Initializes a Matrix object with a 2D list data representing matrix elements.
- Sets rows and cols attributes based on the dimensions of the matrix.

-> __add__(self, other)
- Adds two Matrix objects (self and other) and returns a new Matrix object with the result.
- Checks if matrices have the same dimensions before performing addition.
- Uses list comprehension to compute element-wise addition of matrices.

-> __sub__(self, other)
- Subtracts one Matrix object (other) from another (self) and returns a new Matrix object with the result.
- Checks if matrices have the same dimensions before performing subtraction.
- Uses list comprehension to compute element-wise subtraction of matrices.

-> __mul__(self, other)
- Multiplies two Matrix objects (self and other) and returns a new Matrix object with the result.
- Checks if matrices are compatible for multiplication (number of columns in self equals number of rows in other).
- Uses nested list comprehension to compute matrix multiplication based on the dot product formula.

-> __str__(self)
- Returns a string representation of the Matrix object.
- Converts each row of the matrix into a string representation, separated by tabs (\t), and joins them with newline characters (\n).

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
-> __init__(self, x, y)
- Initializes a Vector object with coordinates x and y.
  
-> __add__(self, other)
- Adds two Vector objects (self and other) and returns a new Vector object with the result.
- Uses the + operator overloaded method to perform element-wise addition of vectors.

-> __sub__(self, other)
- Subtracts one Vector object (other) from another (self) and returns a new Vector object with the result.
- Uses the - operator overloaded method to perform element-wise subtraction of vectors.

-> dot(self, other)
- Computes the dot product of two Vector objects (self and other).
- Calculates the sum of the products of corresponding coordinates (x and y) of the vectors.

-> __str__(self)
- Returns a string representation of the Vector object in the format <x, y>.

# 6.) Point2D Class

## Concept

The `Point2D` class represents points in a 2D Cartesian coordinate system (`x` and `y` coordinates). It calculates distances between points.

## Example

```python
point1 = Point2D(1, 2)
point2 = Point2D(4, 6)
print(f"Distance: {point1.distance_to(point2)}")
```
-> __init__(self, x, y)
- Initializes a Point2D object with coordinates x and y.
  
-> distance_to(self, other)
- Computes the Euclidean distance between the current Point2D object (self) and another Point2D object (other).
- Uses the formula  d=√((x2 – x1)² + (y2 – y1)²). to calculate the distance.

-> __str__(self)
- Returns a string representation of the Point2D object in the format (x, y).

# 7.) Quaternion Class

## Concept

The `Quaternion` class models quaternions (`w + xi + yj + zk`). It supports addition, subtraction, and multiplication operations.

## Example

```python
q1 = Quaternion(1, 2, 3, 4)
q2 = Quaternion(5, 6, 7, 8)
print(q1 + q2)  # Output: 6 + 8i + 10j + 12k
```
-> __init__(self, w, x, y, z)
- Initializes a Quaternion object with components w, x, y, and z.
  
-> __add__(self, other)
- Adds two Quaternion objects (self and other) and returns a new Quaternion object with the result.
- Uses the + operator overloaded method to perform element-wise addition of quaternions.
  
-> __sub__(self, other)
- Subtracts one Quaternion object (other) from another (self) and returns a new Quaternion object with the result.
- Uses the - operator overloaded method to perform element-wise subtraction of quaternions.

-> __mul__(self, other)
- Multiplies two Quaternion objects (self and other) and returns a new Quaternion object with the result.
- Implements quaternion multiplication using the Hamilton product formula.
  
-> __str__(self)
- Returns a string representation of the Quaternion object in the format w + xi + yj + zk.

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
-> Initialization (__init__ method):
- Initializes a ProbabilityDistribution object based on whether it's discrete or continuous. If continuous (pdf provided), it discretizes the pdf over the given support.
  
-> Discretizing PDF (_discretize_pdf method):
- Discretizes a continuous `probability density function` (pdf) over a specified support range (support) into a dictionary of probabilities.
  
-> Creating CDF (_create_cdf method):
- Computes the cumulative distribution function (CDF) from the discrete or discretized probabilities.

-> Sampling (sample method):
- Generates a random sample from the probability distribution using its CDF.
  
-> Expected Value (expected_value method):
- Computes the expected value (mean) of the distribution.
  
-> Variance (variance method):
- Computes the variance of the distribution.
  
-> Standard Deviation (std_dev method):
- Computes the standard deviation of the distribution.
  
-> Moment (moment method):
- Computes the k-th moment of the distribution.
  
-> Plotting (plot method):
- `Visualizes` the probability distribution using matplotlib. It uses a bar chart for discrete distributions and a line plot for continuous distributions.
  
-> String Representation (__str__ method):
- Returns a string representation of the ProbabilityDistribution object, showing its probabilities.
  
-> Static Methods (from_continuous, normal, uniform, binomial):
- from_continuous: Converts a `continuous probability density function` (pdf) into a ProbabilityDistribution.
- normal: Creates a ProbabilityDistribution for a `normal distribution`.
- uniform: Creates a ProbabilityDistribution for a `uniform distribution`.
- binomial: Creates a ProbabilityDistribution for a `binomial distribution`.


This repository hosts Python implementations of fundamental mathematical classes using object-oriented programming (OOP) principles, designed to enhance code clarity, modularity, and reusability across various mathematical domains. The classes include Fraction for precise handling of fractional arithmetic, ComplexNumber for computational tasks involving complex numbers, Polynomial for algebraic calculations and data fitting, Matrix for structured manipulation of matrices, Vector for geometric computations in 2D space, Point2D for spatial analysis and distance calculations, Quaternion for 3D rotations in computer graphics, and ProbabilityDistribution for modeling discrete and continuous probability distributions. Each class encapsulates specific mathematical concepts, providing methods for arithmetic operations, statistical calculations, and geometric transformations essential in fields like engineering, physics, data science, and game development. These implementations promote efficient problem-solving and serve as foundational tools for both educational exploration and practical applications.

