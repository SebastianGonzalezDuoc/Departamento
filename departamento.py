import funciones as f

while True:
    f.limpiarpantalla()
    f.menu()
    opcion=f.validar_opcion()
    if opcion==1:
        f.ver_edifico()
    elif opcion==2:
        f.comprar_departamento()
    elif opcion==3:
        f.buscar_dueño()
    elif opcion==4:
        f.total_ganancias()
    elif opcion==5:
        print("Saliendo del sistema")
        break