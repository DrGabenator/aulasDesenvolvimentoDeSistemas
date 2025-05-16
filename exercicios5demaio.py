#Peça ao usuário para digitar 5 números e mostre a soma deles ao final.
#print('Peça ao usuário para digitar 5 números e mostre a soma deles ao final.')
#numero1 = input('Digite o primeiro número: ')
#numero2 = input('Digite o segundo número: ')
#numero3 = input('Digite o terceiro número: ')
#numero4 = input('Digite o quarto número: ')
#numero5 = input('Digite o quinto número: ')

#soma = int(numero1) + int(numero2) + int(numero3) + int(numero4) + int(numero5)

#print(f'A soma dos números {numero1}, {numero2}, {numero3}, {numero4}, {numero5} é: {soma}')

#Peça ao usuário para digitar 4 números e mostre qual é o maior e qual é o menor.
#print('Peça ao usuário para digitar 4 números e mostre qual é o maior e qual é o menor.')
#numero1 = int(input('Digite o primeiro número: '))
#numero2 = int(input('Digite o segundo número: '))
#numero3 = int(input('Digite o terceiro número: '))
#numero4 = int(input('Digite o quarto número: '))

#listaDeNumeros = [numero1, numero2, numero3, numero4]

#listaDeNumeros.sort(reverse=False)

#print(f'{listaDeNumeros}')

#print(f'O maior número é: {listaDeNumeros[-1]}\nO menor número é: {listaDeNumeros[0]}')

#Peça ao usuário uma palavra e mostre quantas vogais ela tem.

#palavra = input("Digite uma palavra: ")

#vogais = ["a", "e", "i", "o", "u"]

#contador = 0

#for letra in palavra:
#    for vogal in vogais:
#        if(letra == vogal):
#            contador += 1

#print(f"A quantidade de vogais na palavra {palavra} é de: {contador}")


#print('Peça ao usuário uma palavra e mostre quantas vogais ela tem.')

#palavra = input("Digite uma palavra: ")

#contadorDeVogais = 0

#for letra in palavra:
#    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
#        contadorDeVogais += 1

#print(f'O número de vogais que a palavra {palavra} tem é de: {contadorDeVogais}')

#Peça ao usuário para digitar 6 números e mostre apenas os números pares digitados.
#print('Peça ao usuário para digitar 6 números e mostre apenas os números pares digitados.')

#numero1 = int(input('Digite o primeiro número: '))
#numero2 = int(input('Digite o segundo número: '))
#numero3 = int(input('Digite o terceiro número: '))
#numero4 = int(input('Digite o quarto número: '))
#numero5 = int(input('Digite o quinto número: '))
#numero6 = int(input('Digite o sexto número: '))

#listaDePares = []

#listaDeNumeros = [numero1, numero2, numero3, numero4, numero5, numero6]

#for numero in listaDeNumeros:
#    if numero % 2 == 0:
#        listaDePares.append(numero)

#if len(listaDePares) != 0:
#    print(f"Os números pares digitados foram: {listaDePares}")
#else:
#    print("A lista não tem nenhum número par!")

#Solicite as notas de 4 provas e mostre a média.
#nota1 = float(input('Digite a primeira nota: '))
#nota2 = float(input('Digite a segunda nota: '))
#nota3 = float(input('Digite a terceira nota: '))
#nota4 = float(input('Digite a quarta nota: '))

#media = (nota1 + nota2 + nota3 + nota4) / 4

#print(f'A média das notas {nota1}, {nota2}, {nota3}, {nota4} é: {media}')

#Peça ao usuário um número e mostre a tabuada desse número de 1 a 10.

numeroDigitado = int(input("Digite um número para visualizar a tabuada desse número de 1 a 10: "))

for numero in range(1, 11):
    print(f"{numeroDigitado} X {numero} = {numeroDigitado * numero}")

#Peça um número N ao usuário e mostre todos os números de 1 até N.
#Peça ao usuário uma palavra e mostre ela ao contrário.
#Peça um número ao usuário e diga se ele é múltiplo de 3.
#Peça ao usuário para digitar 3 nomes e mostre todos eles em ordem alfabética.
