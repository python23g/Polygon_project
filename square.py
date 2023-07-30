
class Square:
    def __init__(self, square_side:float):
        self.square_side = square_side
    
    def is_valid(self) -> bool:
        """
        This method checks if the circle is valid.
        Args:
            No
        Returns:
            bool: This method checks if the square is valid.
        """
        if self.square_side > 0:
            return True
        else:
            return False
        
    
    def area(self) -> float:
        """
        This method finds the area of the square.
        Args:
            No
        Returns:
            float or int: return area of the square if the square is valid, 0 otherwise
        """
        a = 0
        if self.is_valid():
            a = self.square_side **2
        return a

    def perimeter(self) -> float:
        """
        This method finds the perimeter of the square.
        Args:
            No
        Returns:
            float: return perimeter of the square if the square is valid, 0 otherwise
        """
        p = 0
        if self.is_valid():
            p = 4 * self.square_side
        return p

sq = Square(5.00)
print(sq.perimeter())