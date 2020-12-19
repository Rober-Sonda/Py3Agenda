import os
def ejecutarScripts():
  print()
  print()
  print("Programas disponibles")
  print("A - Agenda")
  print("B - Adivina un número")
  print("C - Conjuntos")
  print("D - Writing")
  print("S - Salir")
  opcion = input("Elige un programa -> ").upper()
  if opcion == "A":
    os.system('python Agenda/agenda.py')
  elif opcion == "B":
    os.system('python Adivina-el-numero/AdivinaElNum.py')
  elif opcion == "C":
    os.system('python Conjuntos/conjuntos.py')
  elif opcion == "D":
    os.system('python write/write.py')
  elif opcion == "S":
    print("Gracias por usar esta porción de código")
    raise SystemExit #quit() o #Ctrl-D
  else:
    print("Opción no disponible")

while True:
  ejecutarScripts()