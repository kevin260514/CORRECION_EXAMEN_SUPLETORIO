from dominio.repositorio.RecintoRepositorio import RecintoRepositorio
from dominio.entidades.Recinto import Recinto


class RecintoRepositorioMemoria(RecintoRepositorio):
    def __init__(self):
        self.recintos = [
            Recinto("REC-PICH-001", "U.E. Mejia",         "Quito",     "Centro", list(range(1, 21)), True),
            Recinto("REC-PICH-002", "Colegio Montufar",   "Quito",     "Sur",    list(range(1, 31)), True),
            Recinto("REC-GUAY-001", "Esc. Simon Bolivar", "Guayaquil", "Norte",  list(range(1, 16)), False),
        ]

    def buscar_por_codigo(self, codigo):
        for r in self.recintos:
            if r.codigo == codigo:
                return r
        return None
