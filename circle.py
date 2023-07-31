from math import pi, sqrt


class Circle:
    def __init__(self, radius:float):
        self.radius = radius
        
    def is_valid(self) -> bool:
        if self.radius > 0:
            return True
        
        else:

            return False
    
    def diameter(self) -> float:
        '''
        This method finds the diameter of the circle.
        Args:
            no
        Returns:
            float: return diameter of the circle if the circle is valid, 0 otherwise
        '''
        if self.is_valid():
            return self.radius * 2
        else:
            return 0
    
    def circumference(self) -> float:
        '''
        This method finds the circumference of the circle.
        Args:
            no
        Returns:
            float: return circumference of the circle if the circle is valid, 0 otherwise
        '''
        C = 0
        if self.is_valid:
            C = self.diameter() * pi
        return  C
    
    def area(self) -> float:
        '''
        This method finds the area of the circle.
        Args:
            no
        Returns:
            float: return area of the circle if the circle is valid, 0 otherwise
        '''
        a = 0
        if self.is_valid():
            a = pi * self.radius**2
        return a

ccl = Circle(radius=2.00)
