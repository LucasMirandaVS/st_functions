from etl import ler_csv, filtrar_produtos_nao_entregues, somar_valores_produtos

path_arquivo = "vendas.csv"

csv_lido = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(csv_lido)
valor_produtos = somar_valores_produtos(produtos_entregues)
print(valor_produtos)

