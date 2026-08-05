from dominio.repositorio.PersonaRepositorio import PersonaRepositorio
from dominio.entidades.Persona import Persona


class PersonaRepositorioMemoria(PersonaRepositorio):
    def __init__(self):
        self.personas = [
            Persona(1, "Ana Torres", "ciudadano", "1712345678", provincia="Pichincha"),
            Persona(2, "Luis Perez", "ciudadano", "1798765432", provincia="Pichincha"),
            Persona(3, "Marta Ruiz", "analista",  "1700000001", area="falsificacion"),
            Persona(4, "Jorge Vaca", "analista",  "1700000002", area="material"),
            Persona(5, "Sofia Leon", "analista",  "1700000003", area="actas"),
        ]

    def buscar_por_id(self, id):
        for p in self.personas:
            if p.id == id:
                return p
        return None

    def buscar_analista_por_area(self, area):
        for p in self.personas:
            if p.es_analista_de_area(area):
                return p
        return None
