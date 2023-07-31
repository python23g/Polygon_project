from math import pi


class Circle:
    def __init__(self, radius:float):
        self.radius = radius
        
    def is_valid(self) -> bool:
        """
        This method checks if the circle is valid.
        
        Args:
            No
        Returns:
            bool: True if the circle is valid, False otherwise
        """
        return self.radius > 0 
    
    def diameter(self) -> float:
        '''
        This method finds the diameter of the circle.
        Args:
            no
        Returns:
            float: return diameter of the circle if the circle is valid, 0 otherwise
        '''
        if self.is_valid():
            return 2 * self.radius
        return 0
    
    def circumference(self) -> float:
        '''
        This method finds the circumference of the circle.
        Args:
            no
        Returns:
            float: return circumference of the circle if the circle is valid, 0 otherwise
        '''
        f = 0
        if self.is_valid():
            f = self.diameter() * pi 
        return f
    
    def area(self) -> float:
        '''
        This method finds the area of the circle.
        Args:
            no
        Returns:
            float: return area of the circle if the circle is valid, 0 otherwise
        '''
        f = 0 
        if self.is_valid():
            f = pi * self.radius ** 2 
        return f

circle = Circle(9)
is_valid_circle = circle.is_valid()
circle_diameter = circle.diameter()
circle_circumference = circle.circumference()
circle_area = circle.area()

print(is_valid_circle)
print(circle.diameter)
print(circle_circumference)
print(circle_area)