class Profesor:
    def __init__ (self, el_nombre, el_mail):         ##*__init__ crea el objeto (OBLIGATORIO)
        self.__nombre__ = el_nombre
        self.__mail__ = el_mail

    def dame_tu_nombre(self):
        return self.__nombre__

class Alumno:
    def __init__ (self, el_nombre_del_alumno):
        self.__nombre__ = el_nombre_del_alumno
        self.__inasistencia__ = 0
        self.__dieta__ = ""
        self.__mentor__ = None
    def mentoria(self,profesor):
        self.__mentor__ = profesor

    def falta(self):
        self.__inasistencia__ += 1

    def elegi_dieta_especial(self, la_dieta):
        self.__dieta__ = la_dieta

    def es_vegano(self):
        self.__dieta__ = "vegano"

    def esta_libre(self):
        if self.__inasistencia__ >= 5:
            return "Esta libre"
        else:
            return "No esta libre"



#OBJETOS

profe_gabi = Profesor ("Gabriel", "elio@gmail.com")              
profe_elio = Profesor ("Elio", "gabriel@um.edu.ar")

print(profe_elio.dame_tu_nombre())
print(profe_gabi.dame_tu_nombre())

alumno_joaquin = Alumno("Joaquin")
alumno_lucas = Alumno("Lucas")


alumno_joaquin.falta()
alumno_joaquin.falta()
alumno_joaquin.falta()
alumno_joaquin.falta()
print(alumno_joaquin.esta_libre)
alumno_joaquin.falta()
alumno_joaquin.falta()
print(alumno_joaquin.esta_libre)

alumno_lucas.elegi_dieta_especial("vegetariana")
print(alumno_joaquin.es_vegano())
alumno_joaquin.mentoria(profe_elio)
print(alumno_joaquin.__mentor__)