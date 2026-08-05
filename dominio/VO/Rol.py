class Rol:
    def __init__(self, valor):
        self.valor = valor

    def es_ciudadano(self):
        return self.valor == "ciudadano"

    def es_analista(self):
        return self.valor == "analista"
