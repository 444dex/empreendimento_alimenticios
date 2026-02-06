import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # seu usuário do MySQL
        password="",       # sua senha (padrão do XAMPP vem vazio)
        database="empreendimento_alimenticio"
    )
