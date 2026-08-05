class Dictamen:
    def __init__(self, texto):
        if texto is None or len(texto.strip()) < 5:
            raise ValueError("El dictamen debe tener al menos 5 caracteres")
        self.texto = texto.strip()
