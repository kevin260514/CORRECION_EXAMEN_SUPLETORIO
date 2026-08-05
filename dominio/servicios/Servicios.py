from dominio.VO.Prioridad import Prioridad

PAPELETAS_POR_JUNTA = 400


class RuteoAnalistaService:
    def __init__(self, repo_persona):
        self.repo_persona = repo_persona

    def determinar_analista(self, tipo):
        if tipo.valor == "falsificada":
            area = "falsificacion"
        elif tipo.valor == "acta_alterada":
            area = "actas"
        elif tipo.valor in ["rota", "manchada"]:
            area = "material"
        else:
            area = "actas"

        analista = self.repo_persona.buscar_analista_por_area(area)
        if analista is None:
            raise ValueError("No hay analista para el area " + area)
        return analista


class PrioridadService:
    def calcular(self, tipo, cantidad):
        if tipo.valor in ["falsificada", "acta_alterada"]:
            prioridad = Prioridad(Prioridad.ALTA)
        elif tipo.valor == "rota":
            prioridad = Prioridad(Prioridad.MEDIA)
        else:
            prioridad = Prioridad(Prioridad.BAJA)

        if cantidad.valor > (PAPELETAS_POR_JUNTA * 0.10):
            prioridad = Prioridad(Prioridad.ALTA)

        return prioridad
