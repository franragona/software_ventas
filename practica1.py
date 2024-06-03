def fibonacci (numero = print("Tenes que escribir un numero pa")):
    lista = []
    start = numero - 2
    lista.append(start)
    lista.append(numero)
    for i in range(10):
        suma = lista[-2] + lista[-1]
        lista.append(suma)
    print(lista)

fibonacci(2)