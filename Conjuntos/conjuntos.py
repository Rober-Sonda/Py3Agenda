'''Los conjuntos tienen la particularidad de guardar los ingresos de manera
desordenada y no pueden ser modificados por el usuario'''
#obtener los sets del usuario, llamados UNO y DOS
#Crear una funcion de union
#Crear una funcion de intersección
#Crear una funcion de diferencia
#Crear una funcion de diferencia simétrica
opciones = [
  'Unión de conjuntos', 
  'Función de intersección',
  'Función de diferencias',
  'Función de diferencias simétricas',
  'Salir',
]

def Uniones():
  return Conjunto_UNO.union(Conjunto_DOS)

def Interseccion():
  return Conjunto_UNO.intersection(Conjunto_DOS)

def Diferencias():
  return Conjunto_UNO.difference(Conjunto_DOS)

def DiferenciasSimetricas():
  return Conjunto_UNO.symmetric_difference(Conjunto_DOS)

def menu():
  for i in opciones:
      print("{} - {}".format(opciones.index(i) + 1, i))
  opcion = int(input("Elije una opcion para realizar con los conjuntos -> "))
  return opcion


print("Ingresa los elementos de los conjuntos separando por espacio \
cada elemento por ejemplo: 1 2 4 4 6")
Conjunto_UNO = set(input("Ingresa los elementos del conjunto UNO: ").split())
Conjunto_DOS = set(input("Ingresa los elementos del conjunto DOS: ").split())

def inicio():
  try:
    opcion = menu()
  except ValueError:
    print("Esa opcion no es correcta")
  else:
    while True:
      if opcion == 1:
        resultado = Uniones()
        print(resultado)
      elif opcion == 2:
        resultado = Interseccion()
        print(resultado)
      elif opcion == 3:
        resultado = Diferencias()
        print(resultado)
      elif opcion == 4:
        resultado = DiferenciasSimetricas()
        print(resultado)
      elif opcion == 5:
        print("Gracias por usar nuestro código, un cordial saludo")
        break
      else:
        print("Esa opción no existe")
      opcion = menu()

inicio()
 