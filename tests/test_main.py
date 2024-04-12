from app.main import fatorial
from app.main import bhaskara
from app.main import serie_taylor

def test_fat_0():
    assert fatorial(0) == 1


def test_fat_1():
    assert fatorial(1) == 1


def test_fat_5():
    assert fatorial(5) == 120


def test_bhaskara_raiz_1():
    assert bhaskara (1,-2,1) == 1

def test_bhaskara_raiz_2():
    assert bhaskara(1,-5,6) = 3, 2 
    
def test_bhaskara_complexo():
    assert bhaskara(2,3,4) == "Eita, número complexo à vista!"
    

            
    
