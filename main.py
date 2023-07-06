from Creativos import *
from funciones import *

arreglo = np.full((10,10),'---')
lista_persona = []
llenar(arreglo)

def salir():
    print("gracias por preferirnos")
    print("Desarrollador: Allan ")
    print("v1")

def agregarpersona(lista_persona,num_entrada):
    p = Creativos()
    p.rut = int(input("Ingrese rut: "))
    p.nombre = input("Ingrese nombre: ")
    p.apellido = input("Ingrese apellido: ")
    p.num_entrada = num_entrada
    if num_entrada>=1 and num_entrada<=20:
        p.valor = 120000
    if num_entrada>=21 and num_entrada<=50:
        p.valor = 80000
    if num_entrada>=51 and num_entrada<=100:
        p.valor = 50000
    lista_persona.append(p)

def comprarasiento(arreglo,lista_persona):
    try:
        ubicaciones = int(input("Numero de entradas a comprar:"))
        if ubicaciones>=1 and ubicaciones<=3:
            compra = 0
            while compra<ubicaciones:
                mostrar(arreglo)
                num_entrada = int(input("numero de asiento 1 - 100 "))
                if num_entrada >= 1 and num_entrada <= 100:
                    disponible = comprobarAsiento(arreglo,num_entrada)
                    if disponible == True:
                        agregarpersona(lista_persona,num_entrada)
                        comprar(arreglo,num_entrada)
                        compra = compra + 1
                    else:
                        print("No esta disponible")
                else:
                    print("No existe el asiento")
        else:
            print("Ubicaciones entre 1 y 100")
    except BaseException as error:
        print(f"Error: {error}")

def listarpersona(lista_persona):
    for Creativos in lista_persona:
        print(f"informacion:{Creativos.rut} {Creativos.nombre} Valor: {Creativos.apellido} Asiento: {Creativos.num_entrada}")




def totales(lista_persona):
    platinum=0
    gold=0
    silver=0
    total_p=0
    total_g=0
    total_s=0
    for Creativos in lista_persona:
        if int(Creativos.valor) == 120000:
            platinum = platinum + 1
            total_p = total_p + 120000
        if int(Creativos.valor) == 80000:
            gold =gold + 1
            total_g=total_g+ 80000
        if int(Creativos.valor) == 50000:
            silver = silver+ 1
            total_s = total_s + 50000
    print(f"platinum: Cantidad: {platinum} Total: {total_p}")
    print(f"gold: Cantidad: {gold} Total: {total_g}")
    print(f"silver: Cantidad: {silver} Total: {total_s}")


ciclo=True
while ciclo:

        print ("1) Comprar entradas")
        print("2) Mostrar ubicaciones disponibles")
        print("3) Ver listado de personas")
        print("4) Mostrar ganancias totales")
        print("5) salir")
        try:
            op=int(input("seleccione un numero del 1 al 5"))
            match op:
                case 1:
                    comprarasiento(arreglo, lista_persona)
                case 2:
                    mostrar(arreglo)
                case 3:
                    listarpersona(lista_persona)
                case 4:
                   totales(lista_persona)
                case 5:
                    salir()
                case _:
                    print("numero no reconocido")
        except BaseException as error:
            print(f"Error: {error}")