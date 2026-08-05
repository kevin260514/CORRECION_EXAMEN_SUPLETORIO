PAPELETAS_POR_JUNTA = 400

class Cantidad:
    def __init__(self, valor):
        if valor < 1 or valor > PAPELETAS_POR_JUNTA:
            raise ValueError("La cantidad debe estar entre 1 y " + str(PAPELETAS_POR_JUNTA))
        self.valor = valor
