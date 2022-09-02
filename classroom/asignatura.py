class Asignatura:

    def __init__(self, nombre, salon="remoto"):
        self._nombre = nombre
        self._salon = salon

    # Definir el método __str__()
    def __str__(self):
        cadena = self._nombre + " " + self._salon
        return cadena
