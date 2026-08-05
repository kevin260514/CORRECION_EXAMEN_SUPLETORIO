class TipoAnomalia:
    TIPOS_VALIDOS = ["falsificada", "rota", "manchada", "acta_alterada", "otro"]

    def __init__(self, valor):
        if valor not in self.TIPOS_VALIDOS:
            raise ValueError("Tipo de anomalia invalido. Use: " + str(self.TIPOS_VALIDOS))
        self.valor = valor
