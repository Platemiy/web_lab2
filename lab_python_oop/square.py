# -*- coding: utf-8 -*-
from rectangle import Rectangle
from colour import Colour
class Square(Rectangle):
    name='квадрат'
    def __init__(self, length):
        self.length=length
        self.height=length
        colour=Colour()
        self.colour=colour
    def __repr__(self):
        return 'Квадрат со сторной {}, цвета {}, и с площадью {}'.format(self.length, self.colour.name, self.area())