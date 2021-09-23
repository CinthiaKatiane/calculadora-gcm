# Trabalho de reposição de GCM
# Aluna: Cinthia Katiane 

from calculadora import Calculadora

play_in_proccess = True

while play_in_proccess:
    calc = Calculadora()
    print ("Calculadora Reposição GCM")
    print ("Escolha a operação que deseja realizar: ")
    print ("1 - Soma")
    print ("2 - Subtracao")
    print ("3 - Multiplicacao")
    print ("4 - Divisao")
    print ("5 - Sair da calculadora")

    menuop = input("> ")

    if (menuop == '5') :
        play_in_proccess = False
        

    elif (menuop == '1') :
        print ("Digite o primeiro número que será somado: ")
        num1 = input("> ")
        print ("Digite o segundo número que será somado: ")
        num2 = input("> ")

        print ("O resultado da soma é:", calc.somar(num1, num2))
        
    elif (menuop == '2') :
        print ("Digite o primeiro número que será subtrair: ")
        num1 = input("> ")
        print ("Digite o segundo número que será somsubtrairado: ")
        num2 = input("> ")
        print ("O resultado da subtração é:", calc.subtrair(num1, num2))

    elif (menuop == '3') :
        print ("Digite o primeiro número que será multiplicado: ")
        num1 = input("> ")
        print ("Digite o segundo número que será multiplicado: ")
        num2 = input("> ")
        print ("O resultado da multiplicação é:", calc.multiplicar(num1, num2))
        
    elif (menuop == '4') :
        print ("Digite o primeiro número que será dividir: ")
        num1 = input("> ")
        print ("Digite o segundo número que será dividir: ")
        num2 = input("> ")

        print ("O resultado da divisão é:", calc.dividir(num1, num2))

print ("Finalizando...")