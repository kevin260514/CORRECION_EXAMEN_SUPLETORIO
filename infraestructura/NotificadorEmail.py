class NotificadorEmail:
    def __init__(self):
        self.correos = []

    def enviar(self, para, asunto, cuerpo):
        correo = {
            "para": para,
            "asunto": asunto,
            "cuerpo": cuerpo
        }
        self.correos.append(correo)

    def listar_correos(self):
        return self.correos
