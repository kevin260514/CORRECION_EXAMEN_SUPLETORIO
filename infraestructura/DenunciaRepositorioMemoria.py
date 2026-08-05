from dominio.repositorio.DenunciaRepositorio import DenunciaRepositorio


class DenunciaRepositorioMemoria(DenunciaRepositorio):
    def __init__(self):
        self.denuncias = []
        self.secuencia = 0

    def siguiente_id(self):
        self.secuencia += 1
        return self.secuencia

    def guardar(self, denuncia):
        encontrado = False
        for i in range(len(self.denuncias)):
            if self.denuncias[i].id == denuncia.id:
                self.denuncias[i] = denuncia
                encontrado = True
                break
        if not encontrado:
            self.denuncias.append(denuncia)

    def buscar_por_id(self, id):
        for d in self.denuncias:
            if d.id == id:
                return d
        return None

    def existe_denuncia_abierta(self, codigo_recinto, junta, tipo):
        for d in self.denuncias:
            if d.recinto.codigo == codigo_recinto and d.junta == junta and d.tipo.valor == tipo and d.estado.es_abierta():
                return True
        return False

    def listar_por_analista(self, id_analista):
        resultado = []
        for d in self.denuncias:
            if d.analista.id == id_analista:
                resultado.append(d)
        return resultado

    def listar_todas(self):
        return self.denuncias
