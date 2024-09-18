print('hola mundo mi nombre es "Victor"')
print ('saludos')

from Funciones import nuevo_tema,nuevo_subtema


nuevo_tema("variables")
numero = 5
print("numero")

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)
numero = 500
print ("factorial de ", numero, " es ", factorial(numero))            

edad = 20
print('edad:', edad)

altura = 1.65
print("altura:", altura)

nombre = "Victor"
print("nombre",nombre)

nuevo_tema("Listas")

frutas = ['manzanas', 'peras', 'naranjas', 'guayabas', 'papayas']
print('frutas: ', frutas)

varias_cosas = ['escuela', 23, True, frutas]
print('varias_cosas', varias_cosas)

"""
   Seleccionando un elemento
   Comentario de multiples lineas
"""   
print('frutas[4]: ', frutas[4])

print('frutas[-1]: ', frutas[-1])
print('frutas[-2]: ', frutas[-2])

print('frutas[1:4]: ', frutas[1:4]) #Del 1 al 4 consecutivo
print('frutas[1:5:2]: ', frutas[1:5:2]) #Del 1 al 5 de 2 en 2

#Agregando un elemento al final
frutas.append('fresas')
print("frutas:", frutas)

frutas.remove('naranjas') #esta funcion es para remover naranjas
print("frutas:", frutas)

frutas.insert(4, 'kiwi') #Para inserta kiwi en la posicion 4
print("frutas:", frutas)

#Creando una lista vacia
calificaciones = []
libros = list()
print("calificaciones: ", calificaciones)
print("libros: ",libros)

frutas.reverse() # reserve es para ordenar la lista alreves
print("frutas: ", frutas)
frutas.sort() #sort es para ordenar alfabeticamente
print("frutas: ", frutas)

nuevo_tema("diccionario")


persona ={"nombre": "pedro", "Apellido":"Perez", "edad":48, "estatura": 170, "hijos": ["Casimira", "Brayan", "Eliud"]}

print('personas:', persona)

print("persona.keys(): ", persona.keys())
print("persona.values(): ", persona.values())

print('persona.get("nombre"):' , persona.get("nombre"))
print('persona.get("estatura"):' , persona.get("estatura"))

print("persona.items(): ",persona.items())

nuevo_tema("Ciclos")
nuevo_tema("for")

print("########")
for i in range(10):
    print(i)

print("########")
for i in range(3,10):
    print(i)

print("########")
for i in range(3,10,2):
    print(i)

print ("len(frutas):", len(frutas))

for fruta in frutas:
    print(fruta)

for indice in range(len(frutas)):
    print("indice", indice , frutas[indice])

print("########")
for indice, frutas in enumerate(frutas):
    print(indice, fruta) 

print("########")
for keys, value in persona.items():
    print(keys, value)


   






