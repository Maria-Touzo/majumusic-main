from database.conexao import conectar


def recuperar_musicas(ativos:bool=False,genero=None):
    conexao, cursor = conectar()

    if ativos == False:
        cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero, ativo FROM musica;")

    else:
        cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero, ativo FROM musica WHERE ativo = 1;")

    musicas = cursor.fetchall()

    conexao.close()

    return musicas


def adicionar_musica(cantor:str, duracao:str, nome_musica:str, imagem: str, genero:str) -> bool:
    """
    Salva a música e retorna se conseguiu salvar ou não
    """
    try:

        conexao, cursor = conectar()

        cursor.execute("INSERT INTO musica (cantor, duracao, nome, url_imagem, nome_genero, ativo) VALUES (%s, %s, %s, %s, %s)", [cantor, duracao, nome_musica, imagem, genero])

        conexao.commit()

        conexao.close()

        return True
    
    except Exception as erro:
        print (erro)
        return False
    

def excluir_musica(codigo:int):
    """
    Deleta a musica selecionada
    """

    try:

        conexao, cursor = conectar()

        cursor.execute("DELETE FROM musica WHERE codigo = %s", [codigo,])

        conexao.commit()

        conexao.close()

        return True
    
    except Exception as erro:
        print (erro)
        return False
    
def ativar_musica(codigo:int, status:bool):
    try:

        conexao, cursor = conectar()

        cursor.execute("UPDATE musica SET ativo = %s WHERE codigo = %s", [status, codigo])

        conexao.commit()

        conexao.close()

        return True
    
    except Exception as erro:
        print (erro)
        return False







    