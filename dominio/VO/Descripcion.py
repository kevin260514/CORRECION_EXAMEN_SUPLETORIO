class Descripcion:
    def __init__(self, texto):
        if texto is None or len(texto.strip()) < 10:
            raise ValueError("La descripcion debe tener al menos 10 caracteres")
        self.texto = texto.strip()
