# Add whatever it is needed to interface with the DB Table corso
from database import DB_connect



class DAO:

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
                pd = row["pd"]
            ))

        cursor.close()
        cnx.close()
        return res