import numpy as np
import colorama as c
import os
import msvcrt

edificio=np.empty((10,4),object)         #Arreglo numpy 10 filas , 4 columnas
dueños = {}                              #Se crea dueño para luego acceder al rut y ver los depas
ganancias=0                              #Total de ganancias para #OPCION 4
def limpiarpantalla():                   #Funcion://LIMPIAR PANTALLA
    printam("Presione una tecla para continuar ")
    msvcrt.getch()
    os.system('cls')

def printtiulo(texto):                  #Diseño/Titulo
    print(f"""
    {c.Fore.YELLOW}----------------------------------------{c.Fore.RESET}
    {c.Fore.BLUE}{texto}{c.Fore.RESET}  
    {c.Fore.YELLOW}----------------------------------------{c.Fore.RESET}""")
def printr(texto):                      #Diseño/Print ROJO
    print(f"{c.Fore.RED}{texto}{c.Fore.RESET}")
def printv(texto):                      #Diseño/Print Verde
    print(f"{c.Fore.GREEN}{texto}{c.Fore.RESET}")
def printam(texto):                     #Diseño/Print Amarillo
    print(f"{c.Fore.YELLOW}{texto}{c.Fore.RESET}")

def menu():                             #MOSTRAR MENU Y OPCIONES
    printtiulo("Sistema de Venta de Departamentos")
    printam("""
    1) Ver edifico
    2) Comprar departamento
    3) Buscar dueño
    4) Total de ganancias
    5) Salir

    """)

def validar_opcion():                   #VALIDAR OPCION E INGRESAR
    while True:
        try:
            opcion=int(input("Ingrese una opcion:"))
            if opcion>=1 and opcion<=5:
                return opcion
            else:
                printr("Por favor ingrese una opcion del 1 al 5")
        except:
            printr("Error de sistema")

def ver_edifico():                      #MOSTRAR EDIFICIO
    nro_piso=11
    print("\t A   B   C   D")
    for piso in range (10,0,-1):
        nro_piso-=1
        print(f"Piso.-{nro_piso}",end=" ")
        for depto in range(4):
            if edificio[piso-1,depto]==None:
                print("🟩",end=" ")
            else:
                print("🟥" ,end=" ")
        print("")
    print("""
    Departamentos Vendidos:🟥
    Departamentos Disponibles:🟩
    """)
            
def validar_piso():                     #VALIDAR N° de PISO
    while True:
        try:
            piso=int(input("Ingrese el numero de piso:"))
            if piso>=1 and piso<=10:
                return piso
            else:
                printr("Piso invalido")
        except:
            printr("Por favor ingrese numeros enteros")
def validar_depto():                    #VALIDAR LETRA DEPTO
    while True:
        try:
            depto=str(input("Ingrese el letra de depto A-B-C-D:")).upper()
            if len(depto)==1:
                if depto is "A" or "B" or "C" or "D":
                    return depto
                else:
                    printr("Por favor ingrese un depto valido")
            else:
                printr("Depto solo puede tener una letra")
        except:
            printr("ERROR!! Por favor ingrese numeros enteros")

def validar_nombre():                   #VALIDAR NOMBRE
    while True:
        try:
            nombre=str(input("Ingrese nombre del comprador:"))
            if len(nombre)>=3:
                return nombre
            else:
                printr("Ingrese un nombre valido")
        except:
            printr("ERROR!!! Por favor ingrese solo letras")

def validar_rut():                      #VALIDAR RUT
    while True:
        try:
            rut=int(input("Ingrese rut (sin puntos, ni digito verificador):"))
            if rut>11111111 and rut<99999999: #VALIDAMOS QUE TENGA 8 DIGITOS EJ: 12.345.678 or Len=8
                return rut 
            else:
                printr("Ingrese un rut valido")
        except:
            printr("ERROR!!! Por favor ingrese solo numeros (No puntos , no guiones , no digito verficiador)")
#a
def validar_precio(piso):               #VALIDAMOS PRECIO
    if piso>=1 and piso<=7:                 #PISO UNO AL 7
        printv("El valor del departamento tiene un valor de $150.000.000")
        precio=150000000          
        return precio
    elif piso>=8 and piso<=10:              #PISO AL 8-10
        printv("El valor del departamento tiene un valor de $200.000.000")
        precio=200000000
        return precio

def validar_pago(precio):                #VALIDAMOS PAGO
    while True:
        try:
            pago=int(input("Por favor ingrese monto de pago:$"))
            if pago>=precio:
                vuelto=pago-precio
                printv("Pago efectuado con exito")
                if vuelto>0:
                    printam(f"Su vuelto es:${vuelto}")
                    return vuelto
            else:
                printr("Pago insuficiente")
        except:
            printr("ERROR!! Por favor ingrese solo numeros")

ganancias=0                 #INICIO GANANCIAS EN 0 para ir sumando las compras de los deptos
def comprar_departamento():
    piso=validar_piso()      #_Validacion piso
    depto=validar_depto()    #_Validacion depto
    if edificio[piso-1,ord(depto)-65] is None: #Si es None
        precio=validar_precio(piso) #Validamos precio y dara el valor
        pago=validar_pago(precio) #Validamos pago y pedimos el pago

        global ganancias #Variable global
        ganancias+=precio #Actualizamos las ganancias

        rut=validar_rut()  #validamos que el rut sea correcto
        nombre=validar_nombre() #validamos el nombre que sea correcto 

        edificio[piso-1,ord(depto)-65] = { #Guardamos datos: Nombre ,rut , precio , pago
            "nombre": nombre,
            "rut": rut,
            "precio": precio,
            "pago": pago}
        printv("Muchas gracias por su compra!!")
        dueños[rut] = {     #Guardamos en diccionario dueños la ID de rut (y sus datos)
            "nombre": nombre,
            "piso": piso,
            "depto": depto}
    else:
        printr("El departamento ya fue vendido")
          

def buscar_dueño(): #Buscar dueño
    rut=validar_rut() #validamos rut
    if rut in dueños: # si el rut esta en dueño
        dueño=dueños[rut] #sacamos quien es
        nombre=dueño["nombre"] #obtenemos el nombre
        printv(f"El nombre del dueño es:{nombre}") # se muestra
        printam("Departamentos asociados al rut:") # los departamentos asociados
        for piso in range(10,0,-1): #Recorremos el edificio por piso
            for depto in range(4):# y depto
                if edificio[piso - 1, depto] is not None and edificio[piso - 1, depto]["rut"] == rut:
                    print(f"Piso: {piso} Depto: {chr(depto + 65)}")
    else:
        printr("No se encontró ningún dueño con ese rut")

def total_ganancias():
    printv(f"Total de ganancias:${ganancias}")