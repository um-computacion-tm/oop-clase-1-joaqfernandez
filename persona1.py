class Persona:
    def __init__(self, nombre: str = "pepe", apellido: str = "sanchez", dni: int= "4444"):
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__dni__= dni

    def __str__(self):
        return f'Mis datos son nombre = {self.__nombre__} / apellido = {self.__apellido__} / dni = {self.__dni__}'
        
