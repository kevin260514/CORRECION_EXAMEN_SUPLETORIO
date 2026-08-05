class Reportes:
    def __init__(self, repo_denuncia, repo_fiscalia, notificador):
        self.repo_denuncia = repo_denuncia
        self.repo_fiscalia = repo_fiscalia
        self.notificador = notificador

    def listar_denuncias_de_analista(self, id_analista):
        print("--- Bandeja del analista " + str(id_analista) + " ---")
        denuncias = self.repo_denuncia.listar_por_analista(id_analista)
        if not denuncias:
            print("  (sin denuncias)")
            return
        for d in denuncias:
            print("  " + str(d.tramite) + " | " + d.estado.valor + " | " + d.prioridad.valor + " | " + d.recinto.codigo + " junta " + str(d.junta) + " | " + d.tipo.valor)

    def reporte_general(self):
        print(" REPORTE GENERAL ")
        denuncias = self.repo_denuncia.listar_todas()
        total = len(denuncias)
        abiertas = 0
        cerradas = 0
        papeletas = 0
        conteo = {}
        for d in denuncias:
            if d.estado.es_abierta():
                abiertas += 1
            else:
                cerradas += 1
            papeletas += d.cantidad.valor
            conteo[d.tipo.valor] = conteo.get(d.tipo.valor, 0) + 1
        print("Total: " + str(total) + " | Abiertas: " + str(abiertas) + " | Cerradas: " + str(cerradas))
        print("Por tipo: " + str(conteo))
        print("Papeletas afectadas: " + str(papeletas))
        print("Casos en Fiscalia: " + str(self.repo_fiscalia.contar()))
        print("=====================================")

    def ver_bandeja_correos(self):
        print(" CORREOS ENVIADOS ")
        for c in self.notificador.listar_correos():
            print("Para: " + c["para"])
            print("Asunto: " + c["asunto"])
            print("-" * 40)
