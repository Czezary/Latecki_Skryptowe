# -*- coding: utf-8 -*-

import math

import math


class Punkt2D():
    x = 10
    y = 11
    def __name__(self, a, b):
        self.x = a
        self.y = b
    def Drukuj(self):
        print('wartosc x: ', self.x);
        print('wartosc y ', self.y);
    def Zeruj(self):
        self.x = 0
        self.y = 0
    print('\nwyzerowane wspolrzedne');
class Punkt3D(Punkt2D):
    z = 12
    def __name__(self, a, b, c):
        super().__name__(a, b)
        self.z = c
    def Drukuj(self):
        super().Drukuj()
        print('wartosc z: ', self.z);
    def Zeruj(self):
        super().Zeruj()
        self.z = 0

class Odcinek():
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    def punkt_A(self, a, b):
        obj1 = Punkt2D()

        obj1.__name__(a, b)
        self.x1 = obj1.x
        self.y1 = obj1.y

    def punkt_B(self, a, b):
        obj2 = Punkt2D()

        obj2.__name__(a, b)
        self.x2 = obj2.x
        self.y2 = obj2.y

    def dlugosc_odcinka(self):
        print('z punktu o wspolrzednych:', self.x1, ",", self.y1)

        print('do punktu o wspolrzednych:', self.x2, ",", self.y2)
        odcinek = math.sqrt((pow((self.x2 - self.x1), 2)) + (pow((self.y2 - self.y1), 2)))
        return odcinek


def test():
    print(15 * '/', '\nPunkt2D ')
    p2d = Punkt2D()
    p2d.__name__(20, 12)
    p2d.Drukuj()
    p2d.Zeruj()
    p2d.Drukuj()
    print("\n")
    print(15 * '/', '\nPunkt3D ')
    p3d = Punkt3D()
    p3d.__name__(2, 8, 10)
    p3d.Drukuj()
    p3d.Zeruj()
    p3d.Drukuj()
    print("\n")
    print(15 * '/', '\nOdcinek 3')
    odc = Odcinek()
    odc.punkt_A(6, 11)
    odc.punkt_B(2, 15)
    dlugosc = odc.dlugosc_odcinka()
    print('Długosc odcinka wynosi: ', dlugosc)


if __name__ == "__main__":
    test()