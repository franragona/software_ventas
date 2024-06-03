import datetime

# Obtener la fecha y hora actual
fecha_hora_actual = datetime.datetime.now()

# Formatear la fecha y hora
formato = fecha_hora_actual.strftime("%a %b %d %H:%M:%S %Y")


def solo_letras(mensaje):
    while True:
        nombre = input(mensaje)
        if nombre.isalpha():
            return nombre.capitalize()
        else:
            print("Por favor solo utilize letras de A hasta Z.")
            
def solo_numeros(mensaje):
    while True:
        try:
            ingreso = int(input(mensaje))
            return ingreso
        except ValueError:
            print("Opcion incorrecta.")
            
def pedido():
    
    cliente = solo_letras("Ingrese nombre del cliente: ")
    combo_s = solo_numeros("Ingrese cantidad Combo S : ")
    combo_d = solo_numeros("Ingrese cantidad Combo D : ")
    combo_t = solo_numeros("Ingrese cantidad Combo T : ")
    flurby = solo_numeros("Ingrese cantidad Flurby : ")
    
    total = (combo_s * 5) + (combo_d * 6) + (combo_t * 7) + (flurby * 2)
    print(f"Total ${total}")
    while True:
        abona = solo_numeros("Abona con $")
        vuelto = abona - total
        if vuelto >= 0:
            print(f"Vuelto ${vuelto}")
            break
        else:
            print("El monto no es suficiente. Por favor, ingrese un monto mayor o igual al total.")
    
    while True:
        confirmar = solo_letras("¿Confirma pedido? Y/N : ")
        if confirmar == "Y":
            with open("ventas.txt","a") as f:
                f.write(f"{cliente};{formato};Combo S:{combo_s};Combo D:{combo_d};Combo T:{combo_t};Flurby:{flurby};Total:{total}\n")
            return total
        elif confirmar == "N":
            print("Bueno andate a la concha de tu madre")
            return 0
        else:
            print("Y si escribimos Y o N la puta que te pario no sabes leer?")
            
def ingreso():
    with open("registro.txt","a") as f:
        f.write(f"IN;{formato};Encargad@ {nombre}\n")

def salida():
    with open("registro.txt","a") as f:
        f.write(f"OUT;{formato};Encargad@ {nombre}; Caja:${caja}\n" + "#"*50 + "\n")

ejecutar_programa = True

while ejecutar_programa:
    
    caja = 0
    
    #Introduccion
    print("Bienvenido a Hamburguesas IT")

    #Ingreso encargado
    nombre = solo_letras("Ingrese su nombre encargad@: ")
    if nombre:
        ingreso()

    #Menu
    print(f"Hamburguesas IT\nEncargad@ -> {nombre}\nRecuerda, siempre hay que recibir al cliente con una sonrisa :)")
    while True:
        #Opciones
        opcion = solo_numeros("1 – Ingreso nuevo pedido\n2 – Cambio de turno\n3 – Apagar sistema\n>>> ")

        if opcion == 1:
            caja += pedido()
        elif opcion == 2:
            salida()
            break
        elif opcion == 3:
            salida()
            print("Apagando sistema...")
            ejecutar_programa = False
            break
    
