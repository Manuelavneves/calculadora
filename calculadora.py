print("Bem-vindo a Calculadora Phyton!")

operacao = input("Escolha uma operação (+, -, *, /): ")
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

if operacao == "+":
	resultado = int(num1) + int(num2)
if operacao == "-":
	resultado = int(num1) - int(num2)
if operacao == "*":
	resultado = int(num1) * int(num2)
if operacao == "/":
	resultado = int(num1) / int(num2)
    
print("O resultado da operação é: " + str(resultado))