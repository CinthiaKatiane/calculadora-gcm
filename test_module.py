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
<<<<<<< HEAD
    
    def test_potencia(self):
        calculadora = Calculadora()
        assert (calculadora.elevar(10), 100)

=======
>>>>>>> 3e3e198cd397efbd7a8845b9fa08914a9f32d3ab

if __name__ == "__main__":
    unittest.main()