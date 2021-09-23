import unittest
from calculadora import Calculadora

class MultiplicacaoTeste(unittest.TestCase):
    def test_multiplicacao(self):
        calculadora = Calculadora()
        assert (calculadora.multiplicar(10,10), 100)

if __name__ == "__main__":
    unittest.main()