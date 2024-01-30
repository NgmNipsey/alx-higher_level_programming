#!/usr/bin/python3
""" Defines Rectangle. """


class Rectangle:
    """ Represent rectangle. """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes rectangle instance with given width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Returns width of the rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width of the rectangle. """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Returns height of the rectangle. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns area of the recatangle. """
        return self.width * self.height

    def perimeter(self):
        """ Returns pereimeter of the rectangle. """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """ Returns the string representation of the rectangle. """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "\n".join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """ Returns string representation of an instance. """
        return "Rectangle({}, {}".format(self.width, self.height)
    
    def __del__(self):
        """ Delete rectangle instance. """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
