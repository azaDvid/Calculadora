n1=float(input("Ingresa tu 1er valor = "))
n2=float(input("Ingresa tu 2do valor = "))
while True:
  print("""
  Menu pricipal
  
  ¿Qué operación deseas realizar?
  1. Potencia
  2. Modal
  3. División
  4. Menú dos
  5.Salir
  """)

  opcion=int(input("Escoge una opción "))
  if opcion==1:
    print("La potencia de ", n1, "^", n2, " = ", n1**n2)
  elif opcion==2:
    print("El residuo de ", n1, "/", n2, " = ", n1%n2)
  elif opcion==3:
    print("La división de ", n1, "/", n2, " = ", n1/n2)
  elif opcion==4:
    n41=float(input("Ingresa tu 1er valor = "))
    n42=float(input("Ingresa tu 2do valor = "))
    n43=float(input("Ingresa tu 3er valor = "))
    opcion2=0
    while True:
      print("""
      Menú secundario
      
      ¿Qué operación deseas realizar?
      4.1 Suma
      4.2 Resta
      4.3 Regresar al menú anterior
      """)
      opcion2=float(input("Ingresa una opción "))
      if opcion2==4.1:
        print("La suma de los números es ", n41, "+", n42, "+", n43, " = ", n41+n42+n43)
      elif opcion2==4.2:
        print("La resta de los números es ", n41, "-", n42, "-", n43, " = ", n41-n42-n43)
      elif opcion2==4.3:
        print("Regresando al menú anterior...")
        break
      else:
        print("Opción no valida")
  elif opcion==5:
    print("Vuelve pronto")
    break
  else:
    print("Opción no valida")