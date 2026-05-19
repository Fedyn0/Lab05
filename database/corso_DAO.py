# Add whatever it is needed to interface with the DB Table corso
import mysql

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

    @staticmethod
    def getStudenteFromMatricola(matr):
        cnx = DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select *
                    from studente s
                    where s.matricola = %s"""

        cursor.execute(query, (matr, ))

        res = []
        for row in cursor:
            res.append(Studente(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorsiFromMatricola(matr):
        cnx = DB_connect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ select c.*
                    from iscrizione i, corso c, studente s
                    where s.matricola = i.matricola and c.codins = i.codins 
                    and s.matricola = %s"""

        cursor.execute(query, (matr, ))

        res = []
        for row in cursor:
            res.append(Corso(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def isStudenteInCorso(matricola, codins):
        cnx = DB_connect.get_connection()
        cursor = cnx.cursor()

        query = """SELECT * 
                   FROM iscrizione
                   WHERE matricola = %s 
                     AND codins = %s"""

        cursor.execute(query, (matricola, codins))

        rows = cursor.fetchall()

        cursor.close()
        cnx.close()

        return len(rows) > 0

    @staticmethod
    def nuovaIscrizione(matricola, codins):
        cnx = DB_connect.get_connection()
        cursor = cnx.cursor()

        query = """insert into iscrizione(matricola, codins)
                    values (%s, %s)"""
        try:
            cursor.execute(query, (matricola, codins))
            cnx.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Errore durante l'iscrizione: {err}")
            return False

        finally:
            cursor.close()
            cnx.close()