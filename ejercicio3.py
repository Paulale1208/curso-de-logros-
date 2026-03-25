# ejercicio 1 

numero=int(input(" ingresa un numero "))
division= numero % 2 
print(f" tu numero es { numero }")
if division == 0:
    print(f" es un numero par")

else: 
  print(f" es un numero impar ")

  # ejercicio 2

  numero1= int(input(" agrega un numero "))
  numero2= int(input(" agrega otro numero "))

  if numero1 >> numero2:
     print(f" numero uno es mayor ")
  elif numero1 << numero2:
     print(f" numero dos es mayor ")
  elif numero1 == numero2:
     print(f" los numero son iguales ")
  else: 
     print(f" error ")

# ejercicio 3 

edad1=int(input(" ingresa tu edad "))
  
if edad1 >= 18: 
   print(f" eres mayor de edad ")

else: 
   print(f" eres menor de edad ")

# ejercicio 4

monto= float(input(" ingresa el monto"))

if monto > 1000: 
   print(f" tu monto descontado es { monto * 0.15 }") 
else: 
   print(f" tu monto es el mismo ") 

# ejercicio 5 

años= int(input(" ingresa tu año "))
division_año_bisiesto= años % 4

if division_año_bisiesto 



