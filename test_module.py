import unittest
from calculadora import Calculadora

class DivisaoTeste(unittest.TestCase):
    def test_divisao(self):
        calculadora = Calculadora()
        assert (calculadora.dividir(10,10), 1)

if __name__ == "__main__":
    unittest.main()