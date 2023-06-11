# passo 1: Importar a base de dados
# passo 2: Calcular o faturamento de cada loja
# passo 3: Calcular a quantidade de produtos vendido de cada loja
# passo 4: Calcular o Ticket Médio dos produtos de cada loja
# passo 5: enviar e-mail para a Diretoria
# passo 6: enviar e-mail para cada loja

import pandas as pd

# passo 1: Importar a base de dados
tabela_vendas = pd.read_excel("./vendas_lojas.xlsx")

# print(tabela_vendas) 

# passo 2: Calcular o faturamento de cada loja
tabela_faturamento = tabela_vendas[["LojaId", "Lucro"]].groupby("LojaId").sum()
tabela_faturamento = tabela_faturamento.sort_values(by="Lucro", ascending=False)
# print(tabela_faturamento)

# passo 3: Calcular a quantidade de produtos vendido de cada loja

tabela_quantidade = tabela_vendas[["LojaId", "Vendas"]].groupby("LojaId").sum()
print(tabela_quantidade)
