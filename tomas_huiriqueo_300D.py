
repe=1
while repe==1:
    pr1=0
    pr2=0
    pr3=0
    pr4=0
    pr5=0

    op1=1
    op2=0
    op3=0

    revaluar=1

    nombre = input("ingrese su nombre:\n")
    direccion= input("ingrese su direccion:\n")
    telefono= int(input("ingrese su telefono:\n"))

    while op1==1:
        print("opciones para su pedido:")
        print("|1) Abono        $1200 X unidad |")
        print("|2) Tierra       $1000 X unidad |")
        print("|3) Lirio        $1100 X unidad |")
        print("|4) Rosas Rojas  $1700 X unidad |")
        print("|5) Margaritas   $1100 X unidad |")
        print("|6) Salir                       |")
        op2 = int(input("Que eligue?:\n"))

        if op2==1:
            pr1 = int(input("cuantas unidades?:\n")) + pr1
        elif op2==2:
            pr2 = int(input("cuantas unidades?:\n")) + pr2
        elif op2==3:
            pr3 = int(input("cuantas unidades?:\n")) + pr3
        elif op2==4:
            pr4 = int(input("cuantas unidades?:\n")) + pr4
        elif op2==5:
            pr5 = int(input("cuantas unidades?:\n")) + pr5
        elif op2==6:
            op1=2

        op1 = int(input("desea seguir comprando?:\n 1.- SI\n 2.- NO\n"))

    print("antes de continuar, por favor compruebe que sus datos esten bien:")
    print("Nombre: ", nombre)
    print("Direccion: ", direccion)
    print("Telefono: ",telefono)
    print("productos comprados:")
    if pr1>=1:
        print("|",pr1," de Abono X$",pr1*1200,"|")
    if pr2>=1:
        print("|",pr2," de Tierra X$",pr2*1000,"|")
    if pr3>=1:
        print("|",pr3," de Lirio X$",pr3*1100,"|")
    if pr4>=1:
        print("|",pr4," de Rosas Rojas X$",pr4*1700,"|")
    if pr5>=1:
        print("|",pr5," de Margaritas X$",pr5*1100,"|")

    revaluar=int(input("algun dato esta mal?:\n 1.- SI\n 2.- NO\n"))

    while revaluar==1:
        print("cual dato esta mal?:")
        print("|1) nombre        |")
        print("|2) telefono      |")
        print("|3) Direccion     |")
        print("productos:")
        print("|4) Abono         |")
        print("|5) Tierra        |")
        print("|6) Lirio         |")
        print("|7) Rosas Rojas   |")
        print("|8) Margaritas    |")
        op3=int(input("cual esta equivocado:\n"))
        if op3==1:
            nombre=input("cual es su nombre entonces:\n")
        elif op3==2:
            direccion=input("cual es su direccion entonces:\n")
        elif op3==3:
            telefono=int(input("cual es su celular entonces:\n"))
        elif op3==4:
            pr1 = int(input("cuantas unidades?:\n")) + pr1
        elif op3==5:
            pr2 = int(input("cuantas unidades?:\n")) + pr2
        elif op3==6:
            pr3 = int(input("cuantas unidades?:\n")) + pr3
        elif op3==7:
            pr4 = int(input("cuantas unidades?:\n")) + pr4
        elif op3==8:
            pr5 = int(input("cuantas unidades?:\n")) + pr5

        print("compruebe que sus datos esten bien:")
        print("Nombre: ", nombre)
        print("Direccion: ", direccion)
        print("Telefono: ",telefono)
        print("productos comprados:")
        if pr1>=1:
            print("|",pr1," de Abono X$",pr1*1200,"|")
        if pr2>=1:
            print("|",pr2," de Tierra X$",pr2*1000,"|")
        if pr3>=1:
            print("|",pr3," de Lirio X$",pr3*1100,"|")
        if pr4>=1:
            print("|",pr4," de Rosas Rojas X$",pr4*1700,"|")
        if pr5>=1:
            print("|",pr5," de Margaritas X$",pr5*1100,"|")

        revaluar=int(input("algun otro dato esta mal?:\n 1.- SI\n 2.- NO\n"))

    print("su boleta:")
    print("Nombre: ", nombre)
    print("Direccion: ", direccion)
    print("Telefono: ",telefono)
    print("productos comprados:")
    if pr1>=1:
        print("|",pr1," de Abono X$",pr1*1200,"|")
    if pr2>=1:
        print("|",pr2," de Tierra X$",pr2*1000,"|")
    if pr3>=1:
        print("|",pr3," de Lirio X$",pr3*1100,"|")
    if pr4>=1:
        print("|",pr4," de Rosas Rojas X$",pr4*1700,"|")
    if pr5>=1:
        print("|",pr5," de Margaritas X$",pr5*1100,"|")

    repe=int(input("desea comprar de nuevo?"))
