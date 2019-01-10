# -*- coding: utf-8 -*-

from figure import Figure
from colour import Colour
class Rectangle(Figure):
    name='прямоугольник'
    def __init__(self, length, height):
        self.length=length
        self.height=height
        colour=Colour()
        self.colour=colour
    def area(self):
        return self.height*self.length
    def __repr__(self):
        return 'Прямоугольник с длиной {}, с шириной {}, цвета {}, и с площадью {}'.format(self.length, self.height, self.colour.name, self.area())