from acessa_banco import pegar_dados
import pandas as pd

"""
DADOS A SEREM APRESENTADOS:
- TOP 5 (10?) PRODUTO MAIS VENDIDO
- TOP 5 (10?) PRODUTO MENOS VENDIDO
- TOP 5 (10?) LOJAS QUE MAIS VENDERAM E O VALOR TOTAL DA VENDA
- TOP 5 (10?) LOJAS QUE MENOS VENDERAM E O VALOR TOTAL DA VENDA
- TOP 5 (10?) LOJAS COM MAIOR RECEITA  --> OK
- TOP 5 (10?) LOJAS COM MENOR RECEITA  --> OK
"""

def criar_data_frame(consulta_sql: str):
    """
    Recebe uma consulta SQL para solicitar os dados da função "pegar_dados()"
    :param consulta_sql: A consulta na linguagem SQL.
    :return: Retorna o DataFrame contendo os dados solicitados.
    """
    dados = pegar_dados(consulta_sql)
    tabela = pd.DataFrame(dados)
    tabela.columns = ['Produto', 'Quantidade']  # -> Definindo o nome das colunas
    return tabela


def buscar_produtos_mais_vendidos(quantidade: int) -> list:
    """
    Busca pelos produtos mais vendidos do banco de dados.
    :param quantidade: A quantidade de produtos a serem pegos.
    :return: Uma lista contendo os X produtos mais vendidos.
    """
    comando = "SELECT produto, quantidade FROM Vendas;"
    produtos = criar_data_frame(comando)

    mais_vendidos = produtos.groupby('Produto').sum()
    mais_vendidos.sort_values(by='Quantidade', inplace=True, ascending=False)
    # by='Quantidade' -> Ordena pela coluna 'Quantidade'.
    # inplace=True -> Altera o dataframe diretamente.
    # ascending=False -> Ordena de forma decrescente.

    return mais_vendidos[:quantidade]


def buscar_produtos_menos_vendidos(quantidade: int) -> list:
    """
    Busca pelos produtos menos vendidos do banco de dados.
    :param quantidade: A quantidade de produtos a serem pegos.
    :return: Uma lista contendo os X produtos menos vendidos.
    """
    comando = "SELECT produto, quantidade FROM Vendas;"
    produtos = criar_data_frame(comando)

    menos_vendidos = produtos.groupby('Produto').sum()
    menos_vendidos.sort_values(by='Quantidade', inplace=True)

    return menos_vendidos[:quantidade]


if __name__ == '__main__':
    print(buscar_produtos_mais_vendidos(5))
    print(buscar_produtos_menos_vendidos(5))
