#Exercício 3 da Lista 2 Programa que verifica o Gênero.

letra = input("Informe  uma letra sendo F ou M: ")

if (letra == "M" ) or (letra == "m"):
    print("O gênero é masculino")
elif (letra == "F") or (letra == "f"):
    print("O gênero é feminino") 

else:
    print("Os dados não foram informados corretamente, favor validar os dados")   



# Exercício 5 da Lista 2 alcule de média de uma aluno onde informa se ele passou ou reprovou


nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2)/2

if media == 10:
    print("Aluno aprovado com Distinção")
elif media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado, estude para recuperação")
    

# Exercício 7 da Lista 2 validação para ver qual número digitado pelo usuário é maior

N1 =  int (input("Informe o primeiro número: "))
N2 =  int (input("Informe o segundo número: "))
N3 = int (input("Informe o terceiro número: "))

if (N1 > N2) or (N1 > N3):

    print("O primeiro número é o maior")

elif (N2 > N1) or (N2 > N3):

    print("O segundo número é o maior")

else:
    ("O terceiro número é o maior")    



# Exercício 1 da Lista 3 Programa que verifica um valor entre 0 e 10 e caso seja inválido informe valor inválido


while True:

    n = float(input("Digite um número entre 0 e 10: "))

    if n >= 0 and n <= 10:
        print("Número válido ")
        break
    else:
        print("Número inválido! ")



# Exercício 9 da Lista 3 faça um programa que imprima os números ímpares entre 1 a 50

n = -1

while n < 49:

    n+= 2

    print(n)
