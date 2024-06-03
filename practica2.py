"""

def promedio_variable(*args):
    x = 0
    a = 0
    promedio = 0
    for i in args:
        x += 1
        a += i
    promedio = a / x
    return promedio
     
print(promedio_variable(1,2,3,4,5))

def promedio_variable2(*args):
    return sum(args) / len(args)

print(promedio_variable2(5,5,5,))

"""

"""

primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]

def iguales(lista1,lista2):
    tercera = []
    for i in lista1:
        if i in lista2 and i not in tercera:
            tercera.append(i)
    return tercera



def iguales2(lista1,lista2):
    conjunto_comun = set()
    for i in lista1:
        if i in lista2:
            conjunto_comun.add(i)
            
    return list(conjunto_comun)

print(iguales(primera,segunda))

"""

"""

entrada = {"franco":1}
while True:
    try:
        opcion_1 = int(input("Bienvenido al registro de entrada\n1.Registrarme\n2.Ver registros\n3.Salir\n>>> "))
    except ValueError:
        print("Por favor ingrese solo numeros.")
        continue
    
    if opcion_1 == 1:
        nombre = input("Ingrese su nombre: ")
        entrada[nombre] = entrada.get(nombre, 0) + 1
        print("¡Se registro su entrada con exito!")
    elif opcion_1 == 2:
        nombre_audit = input("Ingrese el nombre: ")
        if nombre_audit in entrada:
            print(f"{nombre_audit} ingreso {entrada[nombre_audit]} veces el dia de hoy.")
        else:
            print(f"No se encuentra registrado el nombre {nombre_audit}")
    elif opcion_1 == 3:
        print("Usted esta saliendo del programa...")
        break
    else:
        print("La opcion escojida no existe.")
        
"""
"""
def conv(numero):
    hora = numero // 3600  # Calcula las horas
    minuto = (numero % 3600) // 60  # Calcula los minutos restantes
    segundo = numero % 60  # Calcula los segundos restantes
    
    tiempo = f"{hora:02}:{minuto:02}:{segundo:02}"  # Formato de tiempo en HH:MM:SS con ceros a la izquierda
    
    return tiempo

print(conv(4000))
"""
"""lista = [1,2,3,4,5]

def superior(funcion,lista):
    resultado = []
    for i in lista:
        resultado.append(funcion(i))
    return resultado

print(superior(lambda x:x**2,lista))"""

'''while True:
    try:
        x1 = int(input("Ingrese un numero: "))
        x2 = int(input("Ingrese un numero: "))
        break
    except ValueError:
        print("Solo numero por favor.")
        
try:
    suma = x1 + x2
    resta = x1 - x2
    mult = x1 * x2
    div = x1 / x2
except ZeroDivisionError:
    div = "No se puede divivir por cero"
    
print(suma)
print(resta)
print(mult)
print(div)
    '''

#Diccionario código: país.

paises = {
"ar": "Argentina",
"es": "España",
"us": "Estados Unidos",
"fr": "Francia"
}

''''while True:
    while True:
        print("1.Introducir codigo pais\n2.Salir")
        try:
            opcion = int(input("Ingrese una opcion: "))
            break
        except ValueError:
            print("Ingrese solo numeros.")
    if opcion == 1:
        print(
            "Paises y Codigos:\n Argentina - ar\n España - es\n Estados unidos - us\n Francia - fr"
        )
        valor = input("Ingrese el codigo de su pais: ")
        if valor in paises:
            print(paises[valor])
        else:
            print("Codigo inexistente.")
    elif opcion == 2:
        break
    else:
        print("Opcion inexistente.")
    '''
    
'''nombres =  ["juan salvo","henry courtney","elizabeth bennet","marge simpson"]

def mayusculas(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].title()
    return lista

print(mayusculas(nombres))        '''

'''with open("archivo.txt","w") as f:
    f.write("Hola Mundo")
    
with open("archivo.txt","r") as f:
    texto = f.read()

print(texto)'''
    
'''personas = {"Juan":20,"Romina":32,"Tamara":25,"Melanie":19}
with open("personas.txt","w") as f:
    for nombre,edad in personas.items():
        f.write(f"{nombre} - {edad}\n")'''
        
'''personas = {}

with open("personas.txt","r") as f:
    for linea in f:
        nombre,edad = linea.strip().split("-")
        personas[nombre.capitalize()] = int(edad)
        
print(personas)

transaccion = {}

with open("ventas.txt","r") as f:
    f.write(f"{cliente};{date};{combo_s};{combo_d};{combo_t};{flurby};{total}")'''
    
import time as tk

print(tk.time())