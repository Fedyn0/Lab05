# Add whatever it is needed to interface with the DB Table corso
from database import DB_connect
from model.corso import Corso
from model.studente import Studente


class DAO:

    @staticmethod
    def getIscrittiCorso(codins):

        cnx = DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select s.* 
                    from iscrizione i, studente s
                    where s.matricola = i.matricola
                    and i.codins = %s"""

        cursor.execute(query, (codins,))

        res = []
        for row in cursor:
            res.append(Studente(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCodins(self):
        cnx = DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select codins
                    from corso"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["codins"])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllCorsi(self):
        cnx = DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select *
                    from corso"""

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Corso(
                codins=row["codins"],
                crediti=row["crediti"],
                nome=row["nome"],
                pd=row["pd"]
            ))

        cursor.close()
        cnx.close()
        return res

