#Calculadora simples em python
       
print("************** Calculadora em python feita por Gabriel Damasio ************** \n \n \n")
print("Digite o número da operação desejada: \n \n 1. Soma \n 2. Subtração \n 3. Multiplicação \n 4. Divisão \n \n ")

seletorDeOperacao=int(input("Digite sua opção: "))

if seletorDeOperacao == 1:
   
   num1=float(input("Digite o primeiro numero: "))
   num2=float(input("Digite o segundo numero: "))
   print("O resultado da soma é: " , num1+num2)
   
elif seletorDeOperacao == 2:
   
   num1=float(input("Digite o primeiro numero: "))
   num2=float(input("Digite o segundo numero: "))
   print("O resultado da subtração é: " , num1-num2)
   
elif seletorDeOperacao == 3:

   num1=float(input("Digite o primeiro numero: "))
   num2=float(input("Digite o segundo numero: "))
   print("O resultado da multiplicação é: " , num1*num2)
   
elif seletorDeOperacao == 4:
   
   num1=float(input("Digite o primeiro numero: "))
   num2=float(input("Digite o segundo numero (diferente de zero): "))   
   print("O resultado da divisão é: " , num1/num2)
   
else: 
   print("Numero de seleção inválido. Tente novamente. ")