from database.conexao import conectar

def adicionar_usuario(nome:str, senha:str):
    """
    Adiciona o usuario e retorna se deu certo ou não
    """
    try:

        conexao, cursor = conectar()

        cursor.execute("INSERT INTO usuario (nome_usuario, senha) VALUES (%s, %s)", [nome, senha])

        conexao.commit()

        conexao.close()

        return True
    
    except Exception as erro:
        print (erro)    
     
def verificar_usuario(login:str, senha:str):
    """
    Função que verifica se o usuário está cadastrado
    Se estiver cadastrado retorno os dados d usuário
    Se não estiver cadastrado retorno None
    """
    try:
        conexao, cursor = conexao.conectar()
        cursor.execute("SELECT login, senha FROM usuario WHERE login = %s and senha = %s ", (login, senha))
        usuario = cursor.fetchone()
        conexao.close()
        return usuario
    except Exception as erro:
        print(erro)
