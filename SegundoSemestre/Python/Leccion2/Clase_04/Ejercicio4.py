#Ejercicio 4: Sumar números pares dentro de un rango
#hacer un programa para sumar números pares dentro de un rangom por ejemplo:
#  suma de números pares del 2 al 30
#  suma = 240

a = int(input("Digite de dónde va a comenzar la suma: "))
b = int(input("Digite hasta donde quiere llegar a sumar: "))
suma = 0
for i in range(a, b+1):
    if i % 2 == 0: #esto es si el número es par
     suma += i
print(f"\nLa suma de números pares dentro del rango es: {suma}")

