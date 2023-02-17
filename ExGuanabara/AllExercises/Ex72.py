tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
         'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um número de 0 a 20: '))
while numero >20 or numero < 20:
    numero = int(input('Você digitou um número incorreto. por favor, tente novamente: '))
    if numero >=0 and numero <=20:
        break

print(f'O número {numero}, por extenso ficará {tupla[numero]}')