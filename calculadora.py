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
            
    def dividir(self, op1, op2):
        try:
            op1 = float(op1)
            op2 = float(op2)
            if (op2 == 0):
                return ('Resultado inválido, verifique os valores inseridos')  
            else: 
                return op1 / op2
        except:
            return ('Resultado inválido, verifique os valores inseridos')  

    def elevar(self, op1):
        try:
            op1 = float(op1)
            return op1 ** 2
        except:
            return ('Resultado inválido, verifique os valores inseridos')  
