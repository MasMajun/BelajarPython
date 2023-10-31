from PKG.modul1 import *
from PKG.modul2 import *

def fungsi1():
    print('memanggil fungsi 1 yang ada di mana modul1')

def fungsi2():
    print('memanggil fungs 1 yang ada di modul2')
def main():
    #memanggil fungsi fungsi yang ada disana  modul1
    fungsi1()
    fungsi2()
    #memanggil fungsi fungsi yang ada di dalam modul2
    fungsi3()
    fungsi4()
if __name__ == '__main__':
    main()