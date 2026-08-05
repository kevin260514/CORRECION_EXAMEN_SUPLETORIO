class Resultado:
    RATIFICADA = "RATIFICADA"
    DESESTIMADA = "DESESTIMADA"

    def __init__(self, valor):
        if valor not in [self.RATIFICADA, self.DESESTIMADA]:
            raise ValueError("El resultado debe ser RATIFICADA o DESESTIMADA")
        self.valor = valor

    def es_ratificada(self):
        return self.valor == self.RATIFICADA
