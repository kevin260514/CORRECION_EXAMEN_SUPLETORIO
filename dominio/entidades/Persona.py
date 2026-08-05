from dominio.VO.Rol import Rol
from dominio.VO.Area import Area


class Persona:
    def __init__(self, id, nombre, rol, cedula, provincia=None, area=None):
        self.id = id
        self.nombre = nombre
        self.rol = Rol(rol)
        self.cedula = cedula
        self.provincia = provincia
        self.area = Area(area) if area else None

    def es_ciudadano(self):
        return self.rol.es_ciudadano()

    def es_analista_de_area(self, area):
        return self.rol.es_analista() and self.area and self.area.valor == area
