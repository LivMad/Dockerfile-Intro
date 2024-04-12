import math

from app.main import bhaskara, fatorial, serie_taylor


def test_fat_0():
    assert fatorial(0) == 1


def test_fat_1():
    assert fatorial(1) == 1


def test_fat_5():
    assert fatorial(5) == 120


def test_bhaskara_raiz_1():
    assert bhaskara(1, -2, 1) == 1


def test_bhaskara_raiz_2():
    resposta = bhaskara(1, -5, 6)
    assert resposta[0] == 3.0
    assert resposta[1] == 2.0


def test_bhaskara_complexo():
    assert bhaskara(2, 3, 4) is None


def test_taylor():
    valor_real = math.sin(math.pi / 4)
    assert str(serie_taylor(math.pi / 4, 10, 1e-4))[:6] == str(valor_real)[:6]
