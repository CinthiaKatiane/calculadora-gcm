import unittest
from calculadora import Calculadora

class CalculadoraTeste(unittest.TestCase):
    def test_soma(self):
        calculadora = Calculadora()
        assert calculadora.somar(10,10), 20
        
    def test_subtracao(self):
        calculadora = Calculadora()
        assert(calculadora.subtrair(10,10), 0)

    def test_multiplicacao(self):
        calculadora = Calculadora()
        assert (calculadora.multiplicar(10,10), 100)

    def test_divisao(self):
        calculadora = Calculadora()
        assert (calculadora.dividir(10,10), 1)

if __name__ == "__main__":
    unittest.main()