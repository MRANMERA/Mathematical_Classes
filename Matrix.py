class Matrix:
    def __init__(self, data):
        """
        Initializes a Matrix object with the given 2D list `data`.
        Sets attributes `rows` and `cols` based on the dimensions of the matrix.
        """
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        """
        Adds two Matrix objects and returns a new Matrix object with the result.
        Raises a ValueError if matrices have different dimensions.
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __sub__(self, other):
        """
        Subtracts one Matrix object from another and returns a new Matrix object with the result.
        Raises a ValueError if matrices have different dimensions.
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        """
        Multiplies two Matrix objects and returns a new Matrix object with the result.
        Raises a ValueError if matrices are not compatible for multiplication.
        """
        if self.cols != other.rows:
            raise ValueError("Matrices must be compatible for multiplication")
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __str__(self):
        """
        Returns a string representation of the Matrix object.
        """
        return "\n".join(["\t".join(map(str, row)) for row in self.data])

# Example usage:
matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6], [7, 8]])
print(matrix1 + matrix2)
