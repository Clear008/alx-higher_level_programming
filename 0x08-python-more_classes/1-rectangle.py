#!/usr/bin/python3
''' module for defining a rectangle '''


class Rectangle:
    ''' class that desines a rectangle '''

    def __init__(self, width=0, heigh=0):
        ''' initialisation '''
        self.width = width
        self.heigh = heigh

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
