from dominio.repositorio.AlertaFiscaliaRepositorio import AlertaFiscaliaRepositorio


class AlertaFiscaliaRepositorioMemoria(AlertaFiscaliaRepositorio):
    def __init__(self):
        self.alertas = []

    def guardar(self, alerta):
        self.alertas.append(alerta)

    def contar(self):
        return len(self.alertas)
