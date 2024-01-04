#!/usr/bin/python3
''' module for defining a rectangle '''


class Rectangle:
    ''' class that desines a rectangle '''

    def __init__(self, width=0, height=0):
        ''' initialization '''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' width method'''
        return self.__width

    @width.setter
    def width(self, value):
        ''' width setter'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' height method'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height getter'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''method to calculate area'''
        return self.__height * self.__width

    def perimeter(self):
        '''returns the perimeter of the Rectangle,
        or nothing if height/width are 0'''
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)
    
    def __str__(self):
        ''' String representation of the rectangle '''
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += '#' * self.width + '\n'
        return rectangle_str.rstrip('\n')
