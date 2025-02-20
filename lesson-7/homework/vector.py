import math
class Vector():

    def check_dimensions(self, other):
        """Checks whether vectors are in the same dimensions or not"""
        if isinstance(other, Vector):
            return 
        if len(self.vector_components) != len(other.vector_components): 
                raise ValueError("Vectors must have the same number of dimensions")
        else:
            raise TypeError("Unsupported operation between Vector and non-numeric/non-Vector type")

    def __init__(self, *vector_components):
        self.vector_components = tuple(vector_components) 
        


    def __add__(self, other):
        """Addition of the vectors"""
        self.check_dimensions(other)
        new_components = [x + y for x, y in zip(self.vector_components, other.vector_components)] 
        return Vector(*new_components)
    
    
    def __sub__(self, other):
        """Substractions of the vectors"""
        self.check_dimensions(other)
        new_components = [x - y for x, y in zip(self.vector_components, other.vector_components)] 
        return Vector(*new_components)
    
    def __mul__(self, other):
        """Handle scalar multiplication and dot product"""
        if isinstance(other, (int, float)): 
            return Vector(*[x * other for x in self.vector_components]) 
        self.check_dimensions(other)
        return sum(x * y for x, y in zip(self.vector_components, other.vector_components)) 
    
    def __rmul__ (self, other):
        """Now it can work as int * vector also"""
        return self.__mul__(other)
        
    
    def magnitude(self): 
        """Computes the magnitude (length) of the vector"""
        return math.sqrt(sum(x ** 2 for x in self.vector_components )) 

        
    def normalization(self):
        """Normalizes a vector"""
        magnitude = self.magnitude() 

        if magnitude == 0: # If magnitude is 0 it raises the error
            raise ValueError("Can't normalize a zero vector")
        
        return Vector(*[round(x / magnitude, 3) for x in self.vector_components]) 
    
    
    def __repr__(self):
        """Printing a vector shows its content clearly"""
        return f"Vector{self.vector_components}" 
    
    

vector1 = Vector(4, 5, 7)
vector2 = Vector(7, 8, 2)

add_vectors = vector1 + vector2 
sub_vectors = vector1 - vector2 
dot_product = vector1 * vector2 
scalar_multiplication = 4 * vector1  
vector_unit = vector1.normalization() 
print(f"Vector2 {vector2}")
print(f"Addition of vectors: {add_vectors}") 
print(f"Substraction of vectors: {sub_vectors}") 
print(f"Dot product of vectors: {dot_product}")
print(f"Scalar multiplication of vectors: {scalar_multiplication}")
print(f"Magnitude of Vector1: {vector1.magnitude():.3f}") 
print(f"Normalization of Vector1: {vector_unit}")

