def pegar_dados(consulta_sql: str) -> tuple:
    """
    Recebe a consulta sql desejada e retorna os dados da base de dados.
    :param consulta_sql: Consulta na linguagem SQL que será utilizada no banco de dados.
    :return: Retorna um conjunto de tuplas com os dados do banco de dados.
    """
    import mysql.connector

    with open('dados_login.txt', 'r') as arquivo:
        dados = arquivo.read().strip()
        host, user, password, database = dados.split(';')
        # print(host, user, password, database, sep='\n')

    # Estabelecendo a conexão com o banco de dados MySQL e fornecendo as informações adequadas do servidor:
    conexao = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    # Criando um objeto de cursor para executar as consultas SQL:
    cursor = conexao.cursor()

    # Executando a consulta SQL desejada:
    cursor.execute(consulta_sql)

    # Recuperando os resultados, caso existam:
    resultados = cursor.fetchall()  # Retorna um conjunto de tuplas com os dados do banco de dados.


    # Fechando o cursor e a conexão:
    cursor.close()
    conexao.close()

    return resultados


if __name__ == '__main__':
    print(pegar_dados("SELECT produto, quantidade FROM Vendas;"))
