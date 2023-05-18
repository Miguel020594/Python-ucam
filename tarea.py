
nombre = input("¿como te llamas?")
apellidoPaterno = input("¿cual es tu apellido paterno?")
apellidoMaterno = input("¿cual es tu apellido materno?")
edad = float(input("cuantos años tienes"))
estatura = float(input("¿cual es tu altura?"))
peso = float(input("¿cual es tu peso?"))

Imc = peso/estatura**2

print (f"hola{nombre} {apellidoPaterno} {apellidoMaterno} tu indice de masa corporal es {Imc}")