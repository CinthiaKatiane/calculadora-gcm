# Trabalho de reposição de GCM
# Aluna: Cinthia Katiane 

from calculadora import Calculadora

play_in_proccess = True

while play_in_proccess:
    calc = Calculadora()
    print ("Escolha a operação que deseja realizar: ")
    print ("1 - Multiplicacao")
    print ("2 - Sair da calculadora")

    menuop = input("> ")

    if (menuop == '2') :
      play_in_proccess = False
        

    elif (menuop == '1') :
        print ("Digite o primeiro número que será multiplicado: ")
        num1 = input("> ")
        print ("Digite o segundo número que será multiplicado: ")
        num2 = input("> ")

        print ("O resultado da multiplicação é:", calc.multiplicar(num1, num2))

   
print ("Finalizando...")