# -*- coding: utf-8 -*-
def main():
    rect=Rectangle(3,20)
    rect.colour.name='синий'
    cir=Circle(5)
    cir.colour.name='зелёный'
    sq=Square(5)
    sq.colour.name='красный'
    print rect, '\n', cir, '\n', sq

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

if __name__=="__main__": main()