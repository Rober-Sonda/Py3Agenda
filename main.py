import os
def ejecutarScripts():
  print()
  print()
  print("Programas disponibles")
  print("A - Agenda")
  print("B - Adivina un número")
  print("C - Agenda")
  print("S- Salir")
  opcion = input("Elige un programa")
  if opcion == "A":
    os.system('python Agenda/agenda.py')
  elif opcion == "B":
    os.system('python Adivina-el-numero/AdivinaElNum.py')
  elif opcion == "S":
    print("Gracias por usar esta porción de código")
    raise SystemExit #quit() o #Ctrl-D
  else:
    print("Opción no disponible")

while True:
  ejecutarScripts()