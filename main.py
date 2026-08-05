from infraestructura.PersonaRepositorioMemoria import PersonaRepositorioMemoria
from infraestructura.RecintoRepositorioMemoria import RecintoRepositorioMemoria
from infraestructura.DenunciaRepositorioMemoria import DenunciaRepositorioMemoria
from infraestructura.AlertaFiscaliaRepositorioMemoria import AlertaFiscaliaRepositorioMemoria
from infraestructura.NotificadorEmail import NotificadorEmail
from aplicacion.DenunciaAppService import DenunciaAppService
from presentacion.Reportes import Reportes


def main():
    repo_persona = PersonaRepositorioMemoria()
    repo_recinto = RecintoRepositorioMemoria()
    repo_denuncia = DenunciaRepositorioMemoria()
    repo_fiscalia = AlertaFiscaliaRepositorioMemoria()
    notificador = NotificadorEmail()

    servicio = DenunciaAppService(repo_persona, repo_recinto, repo_denuncia, repo_fiscalia, notificador)
    reportes = Reportes(repo_denuncia, repo_fiscalia, notificador)

    print("### DEMO SISTEMA DE DENUNCIAS ELECTORALES - CNE ###\n")

    servicio.registrar_denuncia(1, "REC-PICH-001", 5, "falsificada", 12, "Las papeletas no tienen la marca de agua ni el sello")
    print()

    servicio.registrar_denuncia(2, "REC-PICH-002", 12, "rota", 3, "Tres papeletas llegaron rasgadas por la mitad")
    print()

    servicio.registrar_denuncia(2, "REC-PICH-002", 30, "acta_alterada", 1, "El acta tiene cifras corregidas con esferografico")
    print()

    servicio.registrar_denuncia(1, "REC-PICH-001", 99, "manchada", 5, "Papeletas con manchas de tinta")
    print()

    servicio.registrar_denuncia(1, "REC-GUAY-001", 3, "rota", 2, "Papeletas dobladas y rotas en la mesa")
    print()

    servicio.registrar_denuncia(2, "REC-PICH-001", 5, "falsificada", 4, "Sigue habiendo papeletas sin marca de agua")
    print()

    servicio.registrar_denuncia(1, "REC-PICH-001", 7, "manchada", 0, "No se cuantas papeletas estaban manchadas")
    print()

    servicio.resolver_denuncia(1, 3, "RATIFICADA", "Peritaje confirma que el papel no es el oficial del CNE")
    print()

    servicio.resolver_denuncia(2, 3, "DESESTIMADA", "intento indebido")
    print()

    reportes.listar_denuncias_de_analista(3)
    reportes.listar_denuncias_de_analista(4)
    print()

    reportes.reporte_general()
    print()

    reportes.ver_bandeja_correos()


if __name__ == "__main__":
    main()
