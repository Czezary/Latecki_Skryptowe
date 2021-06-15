
import mojeklasy

def test():
    print(15 * '/', '\nPunkt2D ')
    p2d = mojeklasy.Punkt2D()
    p2d.__name__(20, 12)
    p2d.Drukuj()
    p2d.Zeruj()
    p2d.Drukuj()
    print("\n")
    print(15 * '/', '\nPunkt3D ')
    p3d = mojeklasy.Punkt3D()
    p3d.__name__(2, 8, 10)
    p3d.Drukuj()
    p3d.Zeruj()
    p3d.Drukuj()
    print("\n")
    print(15 * '/', '\nOdcinek 3')
    odc = mojeklasy.Odcinek()
    odc.punkt_A(6, 11)
    odc.punkt_B(2, 15)
    dlugosc = odc.dlugosc_odcinka()
    print('Długosc odcinka wynosi: ', dlugosc)