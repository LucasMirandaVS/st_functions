import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_do_arquivo_csv:str) -> list[dict]:
    """
    Função para ler o arquivo csv e retornar uma lista de dicionários.
    """
    lista = []
    with open(nome_do_arquivo_csv, mode = "r", encoding = 'utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

def filtrar_produtos_nao_entregues(lista:list[dict]) -> list[dict]:
    """
    Função que filtra produtos onde entregue = True
    """
    lista_com_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_com_filtrados.append(produto)
    return lista_com_filtrados

def somar_valores_produtos(lista_com_filtrados:list[dict]) -> int:
    """
    Função que soma os produtos que estao na lista
    """
    valor_total = 0
    for produto in lista_com_filtrados:
        valor_total += int(produto.get("price"))
    return valor_total

csv_lido = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(csv_lido)
valor_produtos = somar_valores_produtos(produtos_entregues)
print(valor_produtos)
