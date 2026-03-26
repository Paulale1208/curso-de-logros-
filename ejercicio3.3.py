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
division_año_bisiesto= ( años % 4 == 0 and años % 100 != 0 ) or ( años % 400 == 0 )

if division_año_bisiesto: 
   print(f"{años} es un anio biciesto ")
else:
   print(f"{años} no es un anio bisiesto ")

# ejercicio 6 

cantidad1= float(input(" agrega una cantidad "))
cantidad2= float(input(" ingresa una cantidad "))

print(" que desesas realizar ")
print(" 1 suma ")
print(" 2 resta ")
print("3 multiplicacion")
print("4 division ")

opcion= int(input(" ingrese el numero de su operacion"))



if opcion ==  1 :
   resultado= cantidad1 + cantidad2
   print(f" el resultado es {resultado}")
   
elif opcion==  2 :
   resultado=cantidad1-cantidad2
   print(f"resultado es {resultado}")
elif opcion == 3 :
   resultado=cantidad1 * cantidad2
   print(f" su resultado es { resultado}")
elif opcion==  4 :
   resultado=cantidad1 / cantidad2
   print(f" su resultado es { resultado }")
else:
   print("ingrese una operacion valida")

#ejercicio 7

lado1= float(input(" ingresa la cantidad de el lado del triangunlo "))
lado2= float(input(" ingresa la cantidad de el lado del triangunlo "))
lado3= float(input(" ingresa la cantidad de el lado del triangunlo "))

if lado1 == lado2 == lado3 :
   print(f" tu triangulo es un equilatero ")
elif(lado1 == lado2 != lado3) or ( lado1 == lado3 != lado2) or ( lado2 == lado3 != lado1) :
   print(f" tu triangulo es isoseles")
else: 
   print(f" es triangulo escaleno ")

#ejercicio 8

nota=float(input(" ingres tu nota "))


if nota >= 90 and nota <= 100 :
   print(f" tu nota es a ")
elif nota >= 80 and nota <= 89 :
   print(f" tu nota es b ")  
elif nota >= 70 and nota <= 79 :
   print(f" tu nota es c ")
elif nota >= 60 and nota <= 69 : 
   print(f" tu nota es d ")
elif nota >= 0 and nota <= 59 : 
   print(f" tu nota es e")
else:
   print(f" errrorrr ")

#ejercicio 9 

print( " bienvenidos a becas zulia tuya ")

promedio=float(input(" ingresa tu promedio "))
solicita_ingresos= float(input(" cual es tu ingreso familiar "))
conducta=bool(input(" tienes buena conducta (si/no)")) 

if ( promedio > 8.5 and solicita_ingresos < 1000) and conducta :
   print( " felicidades tienes una beca del zuliatuya ")
else: 
   print( " lo sentimos no tienes los requisitos  , suerte para la proxima vez ")

# ejercicico 10 
print(' bienvenidos a papel piedras y tijeras ')

jugador1=input( "elige piedra papel o tijeras" )
jugador2= input(" elige piedra papel o tijeras ")

print(f' jugador 1 eligio {jugador1}')
print(f" jugador 2 eligio { jugador2}")

if jugador1 == jugador2 :
 print(" empateee ")
elif (jugador1 == " piedra " and jugador2 == " tijera ") or jugador1== " papel " and jugador2== " piedra "  or (  jugador1== " tijera " and  jugador2 == " papel ") :
   print(" gano el jugador 1 wuuu ")
else :
   print(" gano el jugador 2 loser ")


      

 
 

