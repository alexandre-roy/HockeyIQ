import mysql.connector
import contextlib
import types

@contextlib.contextmanager
def creer_connexion():
    conn = mysql.connector.connect(
        user="root",
        password="Alexrr253977!",
        host="localhost",
        database="HockeyIQ"
    )
    conn.get_curseur = types.MethodType(get_curseur, conn)

    try:
        yield conn
    except Exception:
        conn.rollback()
        raise
    else:
        conn.commit()
    finally:
        conn.close()

@contextlib.contextmanager
def get_curseur(self):
    curseur = self.cursor(dictionary=True, buffered=True)
    try:
        yield curseur
    finally:
        curseur.close()

def sql(query, dictionnaire = None):
    with creer_connexion() as connection:
        with connection.get_curseur() as c:
            c.execute(query, dictionnaire)