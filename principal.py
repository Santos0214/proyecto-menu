from menu import Menu
from cargo import Cargo
from departamento import Departamento
from empleados import Empleado
import os

def buscacargo(codC_edd):
    carg_edd = 0
    for posi_edd in range(0,len(Cargo.cargos)):
        car_edd = Cargo.cargos[posi_edd]
        if car_edd["codigo"] == codC_edd:
            carg_edd = car_edd["cargo"]
            break
    return carg_edd

def buscadepartamento(codD_edd):
    depa_edd = 0
    for posi_depa_edd in range(0,len(Departamento.departamentos)):
        depat_edd = Departamento.departamentos[posi_depa_edd]
        if depat_edd["codigo"] == codD_edd:
            depa_edd = depat_edd["departamento"]
            break
    return depa_edd

def es_decimal(suel):
    try:
        float(suel)
        return True
    except ValueError:
        return False

menu_edd = Menu()
list = ["1). =>Cargo","2). =>Departamento","3). =>Empleados","4). =>Salir"]
opcion_edd = ""
while True:
    os.system("cls")
    opcion_edd = menu_edd.menu_principal(list,"Menu Ficha Personal")
    if opcion_edd == "1":
        op1_edd = ""
        while True:
            os.system("cls")
            op1_edd = Menu.menu_principal("",["1). =>Ingreso","2). =>Consulta","3). =>Salir"],"Mantenimiento de cargos")
            os.system("cls")
            if op1_edd == "1":
                print("********** Ingreso de Cargos **********")
                cargo = input("Nombre del Cargo a Ingresar: ").strip().capitalize()
                while len(cargo) > 20 or len(cargo) == 0:
                    print("Error al ingresar el Cargo (Insuficientes caracteres o Excede caracteres)")
                    cargo = input("Nombre del Cargo a Ingresar: ").strip().capitalize()
                carg = Cargo(cargo)
                cargo1 = carg.registro_cargo_edd()
                Cargo.cargos.append(cargo1)
                input("Cargo ingresado correctamente, presione enter para continuar")
            elif op1_edd == "2":
                print("*************** Listado de cargos *******************")
                print("Código"," "*7,"Descripción")
                for carg in Cargo.cargos:
                    codCar = carg["codigo"]
                    desCar = carg["cargo"]
                    print(" "*1,codCar," "*(12-len(str(codCar))),desCar)
                print("*****************************************************************************************")
                input("Presione enter  para continuar")
            elif op1_edd == "3":
                break
    elif opcion_edd == "2":
        op1_edd = ""
        while op1_edd != "3":
            os.system("cls")
            op1_edd = Menu.menu_principal("",["1). =>Ingreso","2). =>Consulta","3). =>Salir"],"Mantenimiento De Departamentos")
            os.system("cls")
            if op1_edd == "1":
                print("**************** Ingreso de Departamentos *******************")
                departamento = input("Nombre del Departamento a Ingresar: ").strip().capitalize()
                while len(departamento) > 20 or len(departamento) < 5:
                    print("Error al ingresar el Departamento (Insuficientes caracteres o Excede caracteres)")
                    departamento = input("Nombre del Departamento a Ingresar: ").strip().capitalize()
                depa = Departamento(departamento)
                depar = depa.registro_departamento_edd()
                Departamento.departamentos.append(depar)
                input("Departamento ingresado correctamente, presione enter para continuar")
            elif op1_edd == "2":
                print("**************** Listado de departamentos *****************")
                print("Código"," "*7,"Descripción")
                for depa in Departamento.departamentos:
                    codDep = depa["codigo"]
                    desDep = depa["departamento"]
                    print(" "*1,codDep," "*(12-len(str(codDep))),desDep)
                print("*"*66)
                input("Presione enter para continuar")
    elif opcion_edd == "3":
        op1_edd = ""
        while op1_edd != "3":
            os.system("cls")
            op1_edd = Menu.menu_principal("",["1). =>Ingreso","2). =>Consulta","3). =>Salir"],"Mantenimiento De Empleados")
            os.system("cls")
            if op1_edd == "1":
                print("************** Ingreso de Empleados ****************")
                nombre1 = input("Nombre: ").strip().capitalize()
                while len(nombre1) < 3 or len(nombre1) > 20:
                    print("Error al ingresar el Nombre (Insuficientes caracteres o Excede caracteres)")
                    nombre1 = input("Nombre: ").strip().capitalize()
                cedula1 = input("Cédula: ")
                while cedula1.isdigit() == False:
                    print("Error al ingresar la cédula (sólo se tiene que ingresar número)")
                    cedula1 = input("Cédula: ")
                if cedula1.isdigit() == True:
                    while len(cedula1) < 10 or len(cedula1) > 10:
                        print("Error al ingresar el Cédula(Insuficientes o se Exceden dígitos)")
                        cedula1 = input("Cédula: ")
                cargo2 = int(input("Ingrese el código del Cargo: "))
                cargo3 = buscacargo(cargo2)
                while cargo3 == 0:
                    print("¡ERROR! El código del cargo no existe, por favor vuelva a intentarlo")
                    cargo2 = int(input("Ingrese el código del Cargo: "))
                    cargo3 = buscacargo(cargo2)
                departamento2 = int(input("Ingrese el código del Departamento: "))
                departamento3 = buscacargo(departamento2)
                while departamento3 == 0:
                    print("¡ERROR! El código del departamento no existe, por favor vuelva a intentarlo")
                    departamento2 = int(input("Ingrese el código del Departamento: "))
                    departamento3 = buscacargo(departamento2)
                sueldo1 = input("Sueldo: $")
                while es_decimal(sueldo1) is False:
                    print("¡Error al ingresar el sueldo! El tipo de dato ingresado no es correcto")
                    sueldo1 = input("Sueldo: $")
                sueldo1 = round(float(sueldo1),2)
                empleado1 = Empleado(nombre1,cedula1,cargo2,departamento2,sueldo1)
                empleado2 = empleado1.registro_empleados()
                Empleado.empleados.append(empleado2)
                input("Empleado ingresado correctamente, presione cualquier tecla para continuar")
            elif op1_edd == "2":
                print("****************************** Consulta de empleados *************************")
                print("Código"," "*7,"Nombre"," "*18,"Cédula"," "*13,"Cargo"," "*11,"Departamento", " "*5,"Sueldo")
                for empleado1 in Empleado.empleados:
                    codEmp = empleado1["codigo"]
                    nomb = empleado1["nombre"]
                    cedu = empleado1["cedula"]
                    cargo4 = empleado1["cargo"]
                    cargdes = buscacargo(cargo4)
                    depar1 = empleado1["departamento"]
                    depardes = buscadepartamento(depar1)
                    sueldo2 = empleado1["sueldo"]
                    print(" "*2,codEmp," "*8,nomb," "*(23-len(nomb)),cedu," "*(22-len(str(cedu))),cargdes," "*(16-len(str(cargdes))),depardes," "*(16-len(str(depardes))),sueldo2)
                print("**************************************************************************************************")
                input("Presione enter para continuar")
    elif opcion_edd == "4":
        break
        