# Trabalho de reposição de GCM
# Aluna: Cinthia Katiane 

from calculadora import Calculadora

play_in_proccess = True

while play_in_proccess:
    calc = Calculadora()
    print ("Escolha a operação que deseja realizar: ")
    print ("1 - Subtracao")
    print ("2 - Sair da calculadora")

    menuop = input("> ")

    if (menuop == '2') :
      play_in_proccess = False
        

    elif (menuop == '1') :
        print ("Digite o primeiro número que será subtrair: ")
        num1 = input("> ")
        print ("Digite o segundo número que será somsubtrairado: ")
        num2 = input("> ")

        print ("O resultado da subtração é:", calc.subtrair(num1, num2))

   
print ("Finalizando...")