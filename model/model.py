from database.corso_DAO import DAO


class Model:
    def __init__(self):
        pass

    def getIscrittiCorso(self, codins):
        studenti = DAO.getIscrittiCorso(codins)
        studenti.sort(key = lambda s:s.cognome)
        return studenti

    def getAllCorsi(self):
        return DAO.getAllCorsi(self)

    def getStudenteFromMatricola(self, matricola):
        return DAO.getStudenteFromMatricola(matricola)

    def getCorsiFromMatricola(self, matricola):
        return DAO.getCorsiFromMatricola(matricola)

    def getNuovaIscrizione(self, matricola, codins):
        x = DAO.isStudenteInCorso(matricola, codins)
        if x:
            return 2

        isIscritto = DAO.nuovaIscrizione(matricola, codins)
        if isIscritto:
            return 0
        else:
            return 1
