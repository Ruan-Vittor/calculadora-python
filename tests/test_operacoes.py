import pytest
from calculadora.operacoes import somar, subtrair, multiplicar, dividir

class TestSomar:
    def test_somar_positivos(self):
        assert somar(10, 5) == 15

    def test_somar_negativos(self):
        assert somar(-3, -2) == -5

    def test_somar_zero(self):
        assert somar(0, 5) == 5

class TestSubtrair:
    def test_subtrair_positivos(self):
        assert subtrair(10, 5) == 5

    def test_subtrair_negativos(self):
        assert subtrair(-3, -2) == -1

class TestMultiplicar:
    def test_multiplicar_positivos(self):
        assert multiplicar(3, 4) == 12

    def test_multiplicar_por_zero(self):
        assert multiplicar(5, 0) == 0

class TestDividir:
    def test_dividir_positivos(self):
        assert dividir(10, 2) == 5

    def test_dividir_por_zero(self):
        with pytest.raises(ValueError):
            dividir(10, 0)
