nota1 = float(input('Escribe la primera nota '))
nota2 = float(input('Escribe la segunda nota '))
nota3 = float(input('Escribe la tercera nota '))

media = (nota1 + nota2 + nota3)/3

if media > 5:
    resultat = "Suspendido"
else:
    resultat = "Aprobado"

print ('La nota final es ' + str(resultat))
