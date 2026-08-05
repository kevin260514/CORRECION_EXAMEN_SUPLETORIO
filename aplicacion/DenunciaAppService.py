import datetime
from dominio.entidades.Denuncia import Denuncia
from dominio.VO.TipoAnomalia import TipoAnomalia
from dominio.VO.Descripcion import Descripcion
from dominio.VO.Dictamen import Dictamen
from dominio.VO.Tramite import Tramite
from dominio.VO.Cantidad import Cantidad
from dominio.VO.Resultado import Resultado
from dominio.servicios.Servicios import RuteoAnalistaService, PrioridadService


class DenunciaAppService:
    def __init__(self, repo_persona, repo_recinto, repo_denuncia, repo_fiscalia, notificador):
        self.repo_persona = repo_persona
        self.repo_recinto = repo_recinto
        self.repo_denuncia = repo_denuncia
        self.repo_fiscalia = repo_fiscalia
        self.notificador = notificador
        self.ruteo = RuteoAnalistaService(repo_persona)
        self.prioridad_service = PrioridadService()

    def registrar_denuncia(self, id_persona, codigo_recinto, numero_junta, tipo_anomalia, cantidad, descripcion):
        persona = self.repo_persona.buscar_por_id(id_persona)
        if persona is None:
            print("ERROR: la persona no esta registrada")
            return None
        if not persona.es_ciudadano():
            print("ERROR: solo un ciudadano puede presentar una denuncia")
            return None

        recinto = self.repo_recinto.buscar_por_codigo(codigo_recinto)
        if recinto is None:
            print("ERROR: el recinto no existe")
            return None
        if not recinto.habilitado:
            print("ERROR: el recinto " + codigo_recinto + " esta clausurado, no se aceptan denuncias")
            return None
        if numero_junta not in recinto.juntas:
            print("ERROR: la junta " + str(numero_junta) + " no pertenece al recinto " + codigo_recinto)
            return None

        tipos_validos = ["falsificada", "rota", "manchada", "acta_alterada", "otro"]
        if tipo_anomalia not in tipos_validos:
            print("ERROR: tipo de anomalia invalido. Use: " + str(tipos_validos))
            return None

        if cantidad < 1 or cantidad > 400:
            print("ERROR: la cantidad debe estar entre 1 y 400")
            return None

        if descripcion is None or len(descripcion.strip()) < 10:
            print("ERROR: la descripcion debe tener al menos 10 caracteres")
            return None

        if self.repo_denuncia.existe_denuncia_abierta(codigo_recinto, numero_junta, tipo_anomalia):
            print("AVISO: ya existe una denuncia abierta igual para esa junta")
            return None

        tipo = TipoAnomalia(tipo_anomalia)
        desc = Descripcion(descripcion)
        cant = Cantidad(cantidad)
        analista = self.ruteo.determinar_analista(tipo)
        prioridad = self.prioridad_service.calcular(tipo, cant)

        nuevo_id = self.repo_denuncia.siguiente_id()
        codigo_tramite = "DEN-" + str(datetime.datetime.now().year) + "-" + str(nuevo_id).zfill(4)
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        denuncia = Denuncia(
            nuevo_id,
            Tramite(codigo_tramite),
            persona,
            recinto,
            numero_junta,
            tipo,
            cant,
            desc,
            prioridad,
            analista,
            fecha
        )

        self.repo_denuncia.guardar(denuncia)
        self.notificador.enviar(
            analista.nombre,
            "[" + prioridad.valor + "] Nueva denuncia " + codigo_tramite + " en " + codigo_recinto,
            "El ciudadano " + persona.nombre + " reporto " + str(cantidad) + " papeleta(s) '" + tipo_anomalia + "' en la junta " + str(numero_junta) + ". Detalle: " + desc.texto
        )

        print(">> Denuncia registrada: " + codigo_tramite)
        print("   Recinto: " + codigo_recinto + " | Junta: " + str(numero_junta) + " | Tipo: " + tipo_anomalia)
        print("   Prioridad: " + prioridad.valor + " | Asignada a: " + analista.nombre)
        return denuncia

    def resolver_denuncia(self, id_denuncia, id_analista, resultado, dictamen):
        denuncia = self.repo_denuncia.buscar_por_id(id_denuncia)
        if denuncia is None:
            print("ERROR: la denuncia no existe")
            return

        analista = self.repo_persona.buscar_por_id(id_analista)
        if analista is None:
            print("ERROR: analista no existe")
            return

        if not denuncia.estado.es_abierta():
            print("ERROR: la denuncia ya estaba cerrada")
            return

        if denuncia.analista.id != analista.id:
            print("ERROR: solo el analista asignado puede resolver esta denuncia")
            return

        if resultado not in ["RATIFICADA", "DESESTIMADA"]:
            print("ERROR: el resultado debe ser RATIFICADA o DESESTIMADA")
            return

        if dictamen is None or len(dictamen.strip()) < 5:
            print("ERROR: debe escribir el dictamen tecnico")
            return

        res = Resultado(resultado)
        dic = Dictamen(dictamen)
        fecha_cierre = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        denuncia.resolver(analista, res, dic, fecha_cierre)
        self.repo_denuncia.guardar(denuncia)

        print(">> Denuncia " + str(denuncia.tramite) + " cerrada como " + resultado + " por " + analista.nombre)

        if denuncia.debe_escalar_fiscalia():
            alerta = {
                "tramite": str(denuncia.tramite),
                "recinto": denuncia.recinto.codigo,
                "junta": denuncia.junta,
                "motivo": "Presunto delito electoral: " + denuncia.tipo.valor,
                "fecha": fecha_cierre
            }
            self.repo_fiscalia.guardar(alerta)
            print("   !! Caso escalado a Fiscalia: " + alerta["motivo"])
