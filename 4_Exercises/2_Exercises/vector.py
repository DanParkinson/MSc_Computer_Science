from math import isclose

class Vector():
    """
    A class representing a mathematical vector using a list of float values
    """
    def __init__(self, data: list):
        """
        Initialize a Vector instance

        Parameters:
        data: a list of float values representing a vector
        """
        self._vector = data.copy()
    
    def __str__(self):
        """
        Print vector as string "< x, y, z >"
        """
        return "<" + ", ".join(str(value) for value in self._vector) + ">"
    
    def dim(self):
        """
        Returns the dimension of a vector
        [1.0, 2.0, 3.0] = 3
        [1.0, 2,0] = 2
        """
        return len(self._vector)
    
    def get(self, index: int):
        """
        Returns the value at a given index.

        Parameters:
        index: int value fo the desired index
        """
        return self._vector[index]
    
    def set(self, index: int, value: float):
        """
        Set the value at a specified index
        """
        self._vector[index] = value
    
    def scalar_product(self, scalar: int):
        """
        multiply a vector by a given scalar.
        
        Returns: 
        A new vector

        Parameters:
        scalar: int value
        """
        new_values = []

        for value in self._vector:
            new_values.append(value * scalar)
        
        return Vector(new_values)
    
    def add(self, other_vector: list):
        """
        Adds two vectors together

        Business Logic:
        - If other_vecotr is not a vector, return None
        - If vectors of different dimensions, return None

        Parameters:
        other_vector: another vector instance

        Returns: 
        A new vector 
        """

        if not isinstance(other_vector, Vector):
            return None
        
        if self.dim() != other_vector.dim():
            return None
        
        new_values = []

        for i in range(self.dim()):
            new_values.append(self._vector[i] + other_vector._vector[i])
        
        return Vector(new_values)

    def equals(self, other_vector):
        """
        Checks whether two vectors are equal.

        Business Logic:
        - If other_vector is not a Vector, return False.
        - If the vectors have different dimensions, return False.

        Parameters:
        other_vector: Another Vector instance.

        Returns:
        True if both vectors contain the same values, otherwise False.
        """

        if not isinstance(other_vector, Vector):
            return False

        if self.dim() != other_vector.dim():
            return False

        for i in range(self.dim()):
            if not isclose(self._vector[i], other_vector._vector[i]):
                return False

        return True

    def __eq__(self, other_vector):
        """
        Returns True if both vectors are equal.
        """
        return self.equals(other_vector)


    def __ne__(self, other_vector):
        """
        Returns True if both vectors are not equal.
        """
        return not self.equals(other_vector)


    def __add__(self, other_vector):
        """
        Adds two vectors using the + operator.

        Returns:
        A new Vector, or None if the operation is invalid.
        """
        return self.add(other_vector)


    def __mul__(self, scalar):
        """
        Prevents multiplication in the form vector * scalar.
        """
        return NotImplemented


    def __rmul__(self, scalar):
        """
        Multiplies a vector by a scalar using scalar * vector.

        Returns:
        A new Vector containing the scaled values.
        """
        return self.scalar_product(scalar)


    def __iadd__(self, other_vector):
        """
        Supports vector += other_vector.

        Equivalent to:
        vector = vector + other_vector
        """
        return self.add(other_vector)


    def __imul__(self, scalar):
        """
        Supports vector *= scalar.

        Equivalent to:
        vector = scalar * vector
        """
        return self.scalar_product(scalar)


    


