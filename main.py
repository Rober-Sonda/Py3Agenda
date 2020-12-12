agendatelefonica = dict()
#Agregar Contacto
def AgregarContacto(nombre, numero):
  agendatelefonica[nombre]=numero

#Ver Contacto
def verContacto(nombre):
  print(nombre + agendatelefonica[nombre])

#Editar número de Contacto
def EditarContacto(nombre,numero):
  agendatelefonica[nombre]=numero

#Ver todos los contactos
def VerTodoslosContactos(agenda):
  for contacs in agenda:
    print(str(contacs + '  -  ' +agenda[contacs]))
    

def EliminarContacto(nombre):
  del agendatelefonica[nombre]
  print("Contacto borrado")


def MenuOpcional():
    print()
    print()
    print("Presiona el número dependiendo la operacón que deseas realizar")
    print("1 - Agregar Contacto")
    print("2 - Editar número de contacto")
    print("3 - Ver todos los contactos")
    print("4 - Ver contacto")
    print("5 - Eliminar contacto")
    print("6 - Salir")
    print()

MenuOpcional()
numero = int(input("Elija una opción: "))
while numero != 6:
  if numero == 1:
      print("1 - Agregar Contacto")
      nombre = input("ingresa un nombre: ")
      numero = input("ingresa un numero: ")
      AgregarContacto(nombre,numero)  
  elif numero == 2:
      print("2 - Editar número de contacto")
      nombre = input("ingresa un nombre: ")
      numero = input("ingresa un numero: ")
      EditarContacto(nombre,numero)  
  elif numero == 3:
      print("3 - Ver todos los contactos")
      VerTodoslosContactos(agendatelefonica)
  elif numero == 4:
      print("4 - Ver contacto")
      nombre = input("ingresa un nombre: ")
      verContacto(nombre)
  elif numero == 5:
      print("5 - Eliminar contacto")
      nombre = input("ingresa un nombre: ")
      EliminarContacto(nombre)
  elif numero == 6:
      print("5 - Salir del programa")
      break
  MenuOpcional()
  numero = int(input("Elija una opción: "))


