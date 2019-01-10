# -*- coding: utf-8 -*-
from figure import Figure
from colour import Colour
from math import pi
class Circle(Figure):
    name='круг'
    def __init__(self, radius):
        self.radius=radius
        colour=Colour()
        self.colour=colour
    def area(self):
        return pi*self.radius**2
    def __repr__(self):
        return 'Круг с радиусом {}, цвета {}, и с площадью {}'.format(self.radius, self.colour.name, self.area())