# ejercicio 1

precio_producto_completo=float(input("inserta el precio del producto"))
precio_porcentaje= precio_producto_completo / 1.16
precio_de_iva= precio_porcentaje * 0.16

print(f"la iva de ese producto es {precio_de_iva}")

# ejercicio 2 

mi_edad=int(input(" cual es tu edad "))
dias_vividos= mi_edad * 365

print(f" mis dias vividos son {dias_vividos}") 

# ejercicio 3 
 
radio_del_ciculo= float(input("introduce el valor de tu radio"))
pi= 3.1416 * 2
perimetro_del_circulo= pi * radio_del_ciculo

print(f"el perimetro de tu circulo es {perimetro_del_circulo} cm")

# ejercicio 4

verificacion_edad= int(input("ingresa tu edad "))
mayor_edad= verificacion_edad > 18

print(f" eres mayor de 18 {mayor_edad}  ")

# ejercicio 5 

km_recorridos= float(input(" ingresa los km recorridos "))
litros_usados= float(input(" ingresa litros usados "))
cuanto_rinde= km_recorridos / litros_usados

print(f"los litros que rinde por km son {cuanto_rinde} km recorridos por litros ")

#ejercicio 6
 
numero=float(input(" ingresa un numero "))
verificacion= numero < 10 and numero > 20

print(f"mi numero esta en el rango de 10 o 20 {verificacion}")


# ejercicio 7 

dias= int(input(" ingresa los dias "))
segundos= 86400
dias_en_segundos= dias * segundos

print(f" estos dias equivalen {dias_en_segundos} segundos")

# ejercicio 8

a=float(input(" ingresa un numero equivalente a a"))
b=float(input(" ingresa un numero equivalente a b "))
x=(" valor desconocido ")
resolver= x = b / a

print(f" la solucion de la ecuacion ax - b = 0 es { resolver }") 

# ejercicio 9

peso=float(input(" ingresa su peso corporal "))
altura=float(input(" ingresa tu las medidas de tu altura "))
indice= peso / (altura** 2) 

print(f" tu porcentaje de masa corporal es {indice} kg/m cuadrados  ") 

# ejercicio 10 

palabra1= input(" ingresa una palabra ")
palabra2= input(" ingresa otra palabra ")
comparacion= palabra1 > palabra2 

print(f" la palabra 2 es mas larga que la 1 { comparacion }")

