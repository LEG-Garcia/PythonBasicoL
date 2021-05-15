'''
Hoja de trabajo dos
Nombre: Lucía García

'''
# ejercicio uno
print("-------------------------------------------------------------")
print("----------------------- Ejercicio uno -----------------------")
print("-------------------------------------------------------------")

numeroEntero  = input("Ingrese la altura del triangulo : ")
altura=int(numeroEntero)

for i in range(0,altura):
    i +=1
    print(i*'*')

print("-------------------------------------------------------------")

# ejercicio dos

print("----------------------- Ejercicio dos -----------------------")
print("-------------------------------------------------------------")

numeroEntero = input(" Ingrese un número entero: ")

valorEntero  = int(numeroEntero)

for i in range (0,valorEntero+1):
    ordenarNumero=valorEntero-i
    print(ordenarNumero ,end=',')
print("")

print("-------------------------------------------------------------")

# ejercicio tres

print("----------------------- Ejercicio tres ----------------------")
print("-------------------------------------------------------------")

numeroEntero = input("Ingrese un número entero: ")
valorEntero = int(numeroEntero)

for i in range(2,valorEntero):
    if valorEntero % i != 0:
        print(valorEntero,"es un número primo")
        break
    else:
        print(numeroEntero, "no es un número primo")
        break
print("-------------------------------------------------------------")