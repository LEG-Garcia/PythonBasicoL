'''
Hoja de trabajo uno
Nombre: Lucía García

'''
peso_kg   = input("Ingrese su peso en kilogramo : ")
altura_mt = input("ingrese su estatura en metro: ")

# IMC =  peso / altura^2 

IMC = ((float(peso_kg)) / pow((float(altura_mt)),2))

print("Tu indice de masa es {0:.2f}".format(IMC))