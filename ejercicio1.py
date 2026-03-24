nombre_usuario = "paul"       #   una variable "nombe_usuario"   que guarda el texto "paul"
edad = 17                     #   una variable "edad"    que guarda el numero 17
hobbie = "futbol"             #   una variabe "hobbie"    que guarda el texto "futbol"
# presentacion 
print(nombre_usuario)         
print(edad)                   
print(hobbie)                 

print(f"nombre de usuario {nombre_usuario} mi edad es {edad} mi hobbie es {hobbie} " ) 
  

nombre_usuario=input("cual es tu nombre: ")
que_te_gusta_hacer=input("cque te gusta hacer: ")
cual_es_tu_comida_favorita=input("cual es tu comida favorita")
print(nombre_usuario)
print(que_te_gusta_hacer)
print(cual_es_tu_comida_favorita)
print(f"mi nombre es {nombre_usuario} mi cosa favorita es{que_te_gusta_hacer} y mi comida favorita es {cual_es_tu_comida_favorita}")

#calculadora

numero1=float(input("ingresa numero uno "))
numero2=float(input("ingresa numero dos "))

suma= numero1 + numero2
resta= numero1 - numero2
multiplicacion= numero1 * numero2
division= numero1 / numero2

print(suma)
print(resta)
print(division)
print(multiplicacion)

#convertidor de moneda

mi_moneda_=float(input("ingresa la cantidad en tu moneda: "))
moneda_convertir=float(input("ingresa la catidad de la moneda que quieras convertir: "))

multiplicacio_si_es_mayor=mi_moneda_ * moneda_convertir
division_si_es_menor= moneda_convertir / mi_moneda_

print(f"en bolivars es {multiplicacio_si_es_mayor}")
print(f"en dolares es {division_si_es_menor}")

#presentacion de mascota 

mascota_especie=input("ingresa la especie de tu mascota: ")
nombre_mascota=input("nombre de tu mascota: ")
edad_mascota=input("edad de tu mascota: ")

print(f"tu mascota es una {mascota_especie} su nombre es {nombre_mascota} y tiene {edad_mascota}")

# area y perimetro de un rectangulo

base=int(input("ingresa la base de tu rectangulo"))
altura=int(input("ingresa la altura de tu rectangulo"))

el_area_de_tu_rectanglo= base * altura
el_perimtro_es= 2 * (base + altura)
print(f"el area de tu rectangulo es {el_area_de_tu_rectanglo} cm cuadrados y el perimetro es {el_perimtro_es} ")

# mi edad en el futuro 

print("en el 2050 cuantos año tendras")
edad_actual=int(input(" cual es tu edad actual: "))  

mi_edad_en_el_futuro= 24 + edad_actual

print(f"mi edad en el 2050 sera {mi_edad_en_el_futuro}")

# promedio de notas 

nota1=(15)
nota2=(20)
nota3=(18)

promedio= nota1 + nota2 + nota3 
promedio_total= promedio / 3 

print(F"el promedio es de {promedio_total} puntos ")

# ejercicio 9

es_estudiante= True
tiene_trabajo= False

print(f"hola soy estudiante{es_estudiante} y trabajo {tiene_trabajo} ")

# ejercicio 10 

hola= "hola"
mundo= "mundo" 

print(f"{hola} {mundo}") 






