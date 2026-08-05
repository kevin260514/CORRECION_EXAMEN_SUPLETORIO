from dominio.VO.Estado import Estado
from dominio.eventos.DenunciaRegistrada import DenunciaRegistrada
from dominio.eventos.DenunciaRatificada import DenunciaRatificada


class Denuncia:
    def __init__(self, id, tramite, denunciante, recinto, junta, tipo, cantidad, descripcion, prioridad, analista, fecha):
        self.id = id
        self.tramite = tramite
        self.denunciante = denunciante
        self.recinto = recinto
        self.junta = junta
        self.tipo = tipo
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.analista = analista
        self.fecha = fecha
        self.estado = Estado(Estado.ABIERTA)
        self.resultado = None
        self.dictamen = None
        self.fecha_cierre = None
        self.eventos = []
        self.eventos.append(DenunciaRegistrada(
            str(tramite), recinto.codigo, junta,
            tipo.valor, analista.nombre, prioridad.valor, fecha
        ))

    def resolver(self, analista, resultado, dictamen, fecha_cierre):
        if not self.estado.es_abierta():
            raise ValueError("La denuncia ya estaba cerrada")
        if self.analista.id != analista.id:
            raise ValueError("Solo el analista asignado puede resolver esta denuncia")
        self.estado = Estado(Estado.CERRADA)
        self.resultado = resultado
        self.dictamen = dictamen
        self.fecha_cierre = fecha_cierre
        if resultado.es_ratificada():
            self.eventos.append(DenunciaRatificada(
                str(self.tramite), self.tipo.valor,
                self.recinto.codigo, self.junta,
                analista.nombre, fecha_cierre
            ))

    def debe_escalar_fiscalia(self):
        return self.resultado and self.resultado.es_ratificada() and self.tipo.valor in ["falsificada", "acta_alterada"]
