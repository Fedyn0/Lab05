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