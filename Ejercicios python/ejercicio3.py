print("comparador de numeros ")

numero1 = float(input('Escribe la primera nota '))
numero2 = float(input('Escribe la segunda nota '))

if numero1 > numero2:
    print('el mayor es el primero: ' + str(numero1))
elif numero1 < numero2:
    print('el mayor es el segundo ' + str(numero2))
else:
    print("los dos numeros son iguales")