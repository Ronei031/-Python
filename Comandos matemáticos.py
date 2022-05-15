print('--------------------FATIAÇÃO--------------------')
frase = '      Curso em Video Python'

print('Descreve a 9 letra da frase contando com espaços')
print(frase[9])

print('Descreve da 9 até a que antecede a 13')
print(frase[9:13])

print('Descreve da letra numero 9 até a letra numero 21')
print(frase[9:21])

print('Descreve da letra 9 até a 21 pulando de 2 em 2.')
print(frase[9:21:2])

print('Descreve do inicio até a letra numero 5')
print(frase[:5])

print('Descreve da 15 letra até o final')
print(frase[15:])

print('descreve da 9 letra até o final de 3 em 3.')
print(frase[9::3])

print('--------------------ÁNALISE--------------------')

print('Quantos caracteres há na frase.')
print(len(frase))

print('Quantos caracteres x há na frase.')
print(frase.count('o'))

print('Contagem com fatiamento do 0 até 12')
print(frase.count('o',0,13))

print('Em que momento começou a sequencia de letras descrita.')
print(frase.find('deo'))

print('Descreve o valor -1 quando a palrava não existe dentro da frase.')
print(frase.find('Android'))

print('Existe a palavra citada dentro da frase, sim ou não?')
print('Curso'in frase)

print('--------------------TRANSFORMAÇÃO--------------------')

print('Substitui a palavra por outra')
print(frase.replace('Python','Android'))

print('Transforma todas as letras da frase em maisculas.')
print(frase.upper())

print('Transforma todas as letras em minusculas')
print(frase.lower())

print('Mantém a primeira letra maiscula e transforma o restante em minuscula.')
print(frase.capitalize())

print('Transforma todas as letras das primeiras palavras em maiscula.')
print(frase.title())

print('Retira espaçoes indevidos em frases.')
print(frase.strip())

print('Retira os espaços da direita')
print(frase.rstrip())

print('Retira os espaços da esquerda')
print(frase.lstrip())

print('--------------------DIVISÃO--------------------')
print('Separar palavras da frase')
print(frase.split())

print('Separar letras por traços')
print('-'.join(frase))

print('Para escrever o testo inteiro é só utilizar 3 ''')







