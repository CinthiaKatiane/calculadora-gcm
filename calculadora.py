class Calculadora():
    def multiplicar(self, op1, op2):
        try:
            op1 = float(op1)
            op2 = float(op2)
            return op1 * op2
        except:
            return ('Resultado inválido, verifique os valores inseridos')  
