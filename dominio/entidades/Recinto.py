class Recinto:
    def __init__(self, codigo, nombre, canton, zona, juntas, habilitado):
        self.codigo = codigo
        self.nombre = nombre
        self.canton = canton
        self.zona = zona
        self.juntas = juntas
        self.habilitado = habilitado

    def verificar_habilitado(self):
        if not self.habilitado:
            raise ValueError("El recinto " + self.codigo + " esta clausurado, no se aceptan denuncias")

    def verificar_junta(self, numero):
        if numero not in self.juntas:
            raise ValueError("La junta " + str(numero) + " no pertenece al recinto " + self.codigo)
