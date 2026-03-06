import mysql.connector

@staticmethod
def conectar():

    conexao = mysql.connector.connect(
        host="localhost",
        port = 3306,
        user = "root",
        password = "root",
        database = "LogonMusic"
    )

    cursor = conexao.cursor(dictionary=True)

    return conexao, cursor

