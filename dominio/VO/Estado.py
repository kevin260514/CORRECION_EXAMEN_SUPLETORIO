class Estado:
    ABIERTA = "ABIERTA"
    CERRADA = "CERRADA"

    def __init__(self, valor):
        self.valor = valor

    def es_abierta(self):
        return self.valor == self.ABIERTA
