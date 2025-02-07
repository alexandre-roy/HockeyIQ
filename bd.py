"""Modules"""
import contextlib
import types
import mysql.connector

@contextlib.contextmanager
def creer_connexion():
    """Création de la connection"""
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
    """Obtenir le  curseur"""
    curseur = self.cursor(dictionary=True, buffered=True)
    try:
        yield curseur
    finally:
        curseur.close()

def sql(query, dictionnaire = None):
    """Effectue des requêtes SQL"""
    with creer_connexion() as connection:
        with connection.get_curseur() as c:
            c.execute(query, dictionnaire)
