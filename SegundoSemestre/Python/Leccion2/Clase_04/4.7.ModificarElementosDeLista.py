#Ejercicio 2: Modificar los elementos de una lista
#llenar una lista con los números del 1 al 10, luego modificarlos
#multiplicandolos por un valor ingresado por el usuario

lista = list(range(1, 11))
print('Lista original')
for i in lista:
    print(i, end= '-')
valor = int(input('\nDigite un valor a multiplicar: '))
#multiplicamos todos los elementos de la lista
for indice, i in enumerate(lista):
    lista[indice] *= valor

print(f'Lista final con los elementos multiplicados por {valor}')
for i in lista:
    print(i, end='-')