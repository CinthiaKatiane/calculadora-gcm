import unittest
from calculadora import Calculadora

class SomaTeste(unittest.TestCase):
    def test_frete_gratis(self):
        calculadora = Calculadora()
        assert calculadora.somar(10,10), 20

if __name__ == "__main__":
    unittest.main()