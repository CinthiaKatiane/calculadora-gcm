class Calculadora():

    def somar(self, op1, op2):
        try:
            op1 = float(op1)
            op2 = float(op2)
            return op1 + op2
        except:
            return ('Resultado inválido, verifique os valores inseridos')  
    
    def subtrair(self, op1, op2):
        try:
            op1 = float(op1)
            op2 = float(op2)
            return op1 - op2
        except:
            return ('Resultado inválido, verifique os valores inseridos')  

    def multiplicar(self, op1, op2):
        try:
            op1 = float(op1)
            op2 = float(op2)
            return op1 * op2
        except:
            return ('Resultado inválido, verifique os valores inseridos')  
