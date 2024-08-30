alumnos = [
    {
    "nombre": "Emmanuel",
     "apellido": "Yapura",
     "dni": 12342997,
     "fecha de nacimiento": "03-11-96",
     "tutor": "Maria",
     "notas": [8,7,6,9,8,10],
     "faltas": 1,
     "amonestaciones": 0
     },
     {
     "nombre": "Matias",
     "apellido": "Apaza",
     "dni": 42572917,
     "fecha de nacimiento": "18-02-20",
     "tutor": "Jorge",
     "notas": [10,7,6,8,8,10],
     "faltas": 15,
     "amonestaciones": 3
     },
     {
     "nombre": "Sofia",
     "apellido": "Laborda",
     "dni": 41142095,
     "fecha de nacimiento": "21-11-98",
     "tutor": "Marina",
     "notas": [6,4,10,9,8,7],
     "faltas": 0,
     "amonestaciones": 5
     }
]

def mostrar_alumnos(alumnos):    
    id = 0

    for alumno in alumnos:
        print(f"{id}.{alumno} \n")
        id += 1
    

def modificar_alumno(alumno):
    while True:
        dato = input("Que dato desea modificar? Ingrese salir para volver al menu")

        if dato.lower().strip() in alumno:
            nuevo_dato = input(f"Ingrese el nuevo dato {'(separar las notas con espacio)' if dato == "notas" else ""}: ")
            alumno[dato] = list(nuevo_dato.replace(" ","")) if dato == "notas" else nuevo_dato
            print("Alumno modificado, ingrese salir para dejar de modificar:  \n")

        elif dato.lower() == "salir":
            break

        else:
            print("Ingese un dato correcto a modificar o salir: ")


def crear_alumno(alumnos):
    alumno = {}

    propiedades = ["nombre","apellido","dni","fecha de nacimiento","tutor","notas","faltas","amonestaciones"]
    
    for propiedad in propiedades:
        dato = input(f"Ingrese {propiedad} {'(separadas con un espacio)' if propiedad == "notas" else ""}: ")
        alumno[propiedad] = dato
    
    alumno["notas"] = list(alumno["notas"].replace(" ", ""))
    
    alumnos.append(alumno)
    
    print("Alumno agregado \n")


def eliminar_alumno(alumnos):
    mostrar_alumnos(alumnos)

    indice = int(input("Que alumno desea eliminar? Ingrese su numero de registro: "))
    
    if indice <  len(alumnos):        
        alumnos.pop(indice)
        print("Alumno eliminado \n")

    else:
        print("El alumno ingresado es incorrecto")



def iniciar_registro():
    while True:
        accion = int(input(f"Que accion desea realizar? \n 0.Mostrar alumnos \n 1.Modificar alumnos \n 2.Agregar alumno \n 3.Eliminar alumno \n 4.Salir : "))
        if accion == 0:
            mostrar_alumnos(alumnos)
        elif accion == 1:
            mostrar_alumnos(alumnos)
            indice_alumno = int(input("Que alumno desea modificar? Ingrese salir para volver al menu"))
            modificar_alumno(alumnos[indice_alumno])
        elif accion == 2:
            crear_alumno(alumnos)
        elif accion == 3:
            eliminar_alumno(alumnos)    
        elif accion == 4:
            break
        else:
            print("Accion no valida! ")


iniciar_registro()
