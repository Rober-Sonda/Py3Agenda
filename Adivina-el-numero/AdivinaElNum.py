import random

  

def jugarAdivina():
  print("Bienvenido a adivina un número - elije la dificultad del juego")
  print("F - Facil")
  print("M - Media")
  print("D - Difícil")
  dificultad = input("Elije la dificultad -> ")
  if dificultad == "F":
    vidas = 5
    numero_inicio = 1
    numero_final = 10
  elif dificultad=="M":
    vidas = 5
    numero_inicio = 1
    numero_final = 40
  elif dificultad == "D":
    vidas = 3
    numero_inicio = 1
    numero_final = 40

  ElNumero = random.randint(numero_inicio, numero_final)
  print("Bienvenido a este juego, adivina un número del {} al {}".format(numero_inicio,numero_final))
  
  while vidas > 0:
    try:
      numerointento=int(input("Ingresá un número-> "))
    except ValueError:
      print("Esa opción no es correcta")
    else:
      if numerointento == ElNumero:
        print("Acertaste!! Felicitaciones Crack!")
        print("Gracias por jugar a \"Adivina un número\"")
        JugarOtraVez = input("¿Querés jugar otra vez?: si | no -> ")
        print("Esa opción no es correcta")
        if JugarOtraVez.lower() =="si":
          jugarAdivina()
        else:
          print("Gracias por jugar a \"Adivina un número\"")
          break
      else:
        if numerointento > ElNumero:
          print("Fallaste!, El nùmero es menor")
          vidas-=1
          print("Te quedan {} vidas".format(vidas))
        else:
          print("Fallaste!, El nùmero es mayor")
          vidas-=1
          print("Te quedan {} vidas".format(vidas))
  else:
    print("Te quedaste sin vidas!!")
    print("El número era el {} ".format(ElNumero))
    print("Gracias por jugar a \"Adivina un número\"")
    JugarOtraVez = input("¿Querés jugar otra vez?: si | no -> ")
    print("Esa opción no es correcta")
    if JugarOtraVez.lower() =="si":
      jugarAdivina()
    else:
      print("Gracias por jugar a \"Adivina un número\"")

jugarAdivina()