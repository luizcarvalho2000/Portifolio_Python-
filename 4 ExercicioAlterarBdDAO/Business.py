import DAO as PreferenciasDAO

class Preferencias:
    def __init__(self):
        super().__init__()

    objPreferenciasDAO = PreferenciasDAO.PreferenciasDAO()

    def impTxtWhile(self):
        try:
            lista =[]

            arqPreferencias = open("Preferencias.txt", "r", encoding="utf-8")
            strLinhaLida = arqPreferencias.readline()

            while strLinhaLida != "":
                lista.append(strLinhaLida)
                strLinhaLida = arqPreferencias.readline()
            arqPreferencias.close()

            return lista

        except Exception as erro:
            return erro

    def impTxtFor(self):
        try:
            lista = []

            arqPreferencias = open("Preferencias.txt", "r", encoding="utf-8")
            arrStrLinhaLida = arqPreferencias.readlines()
            arqPreferencias.close()

            for item in range(len(arrStrLinhaLida)):
                item = arrStrLinhaLida[item]
                lista.append(item)

            return lista

        except Exception as erro:
            return erro

    def impTxtForEach(self):
        try:
            lista = []

            with open("Preferencias.txt", "r", encoding="utf-8") as arqPreferencias:

                for item in arqPreferencias:
                    lista.append(item)
                arqPreferencias.close()

            return lista

        except Exception as erro:
            return erro

    def impBdConect(self):

        try:
            objPreferenciasDAO = PreferenciasDAO.PreferenciasDAO()

            return objPreferenciasDAO.impBdConect()

        except Exception as erro:
            return erro

    def impBdDesconect(self):
        try:
            objPreferenciasDAO = PreferenciasDAO.PreferenciasDAO()

            return objPreferenciasDAO.impBdDesconect()

        except Exception as erro:
            return erro

    def consultBd(self, parPreferenciasDescricao):

        try:
            objPreferenciasDAO = PreferenciasDAO.PreferenciasDAO()
            return objPreferenciasDAO.consultBd(parPreferenciasDescricao)

        except Exception as erro:
            return erro

    def inserirBd(self, descricao):

        try:
            objPreferenciasDAO = PreferenciasDAO.PreferenciasDAO()
            return objPreferenciasDAO.inserirBd(descricao)

        except Exception as erro:
            return erro

    def excluirBd(self, idDaLinhaSelecionada):

        try:
            objPreferenciasDAO = PreferenciasDAO.PreferenciasDAO()
            return objPreferenciasDAO.excluirBd(idDaLinhaSelecionada)

        except Exception as erro:
            return erro

    def alterarBd(self, descricao, idDaLinhaSelecionada):

        try:
            objPreferenciasDAO = PreferenciasDAO.PreferenciasDAO()
            return objPreferenciasDAO.alterarBd(descricao, idDaLinhaSelecionada)

        except Exception as erro:
            return erro
