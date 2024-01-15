#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""
    CSV_FIELDNAMES = ["id", "size", "x", "y"]

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square."""
        if args:
            self.update_from_args(args)
        elif kwargs:
            self.update_from_kwargs(kwargs)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {field: getattr(self, field) for field in self.CSV_FIELDNAMES}

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
