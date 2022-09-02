# from classroom.asignatura import Asignatura   Línea duplicada
from classroom.asignatura import Asignatura


class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self._listadoAlumnos = estudiantes

    # Agregar el método __str__()
    def __str__(self):
        cadena = "Grupo de estudiantes: " + self._grupo
        return cadena

    # Agregar el ** a kwargs
    def listadoAsignaturas(self, **kwargs):
        # Crear la lista vacía para asignaturas
        self._asignaturas = []
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    # Inicializar lista como None
    def agregarAlumno(self, alumno, lista = None):
        if(lista is None):
            #self._listadoAlumnos = [alumno]
        #else:
            # Crear la lista vacía
            lista = []
        lista.append(alumno)
        self._listadoAlumnos = lista
        # self.listadoAlumnos = [alumno]

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre

    # Se pone al final para que este sea el utilizado
    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre