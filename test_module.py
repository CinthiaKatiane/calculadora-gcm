import unittest
from calculadora import Calculadora

class SubtracaoTeste(unittest.TestCase):
    def test_subtracao(self):
        calculadora = Calculadora()
        assert(calculadora.subtrair(10,10), 0)

if __name__ == "__main__":
    unittest.main()