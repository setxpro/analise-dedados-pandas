import xlsxwriter

# Cria um novo arquivo Excel
nome_arquivo = 'vendas_lojas.xlsx'
workbook = xlsxwriter.Workbook(nome_arquivo)

# Cria uma planilha para as vendas
worksheet_vendas = workbook.add_worksheet('Vendas')

# Dados das vendas por loja
dados_vendas = {
    'Loja': ['Loja A', 'Loja B', 'Loja C'],
    'Vendas': [5000, 7000, 3000],
    'Lucro': [1000, 1500, 800]
}

# Escreve os dados de vendas na planilha
colunas = list(dados_vendas.keys())
for col, titulo in enumerate(colunas):
    worksheet_vendas.write(0, col, titulo)  # Escreve os títulos das colunas
    for row, valor in enumerate(dados_vendas[titulo]):
        worksheet_vendas.write(row + 1, col, valor)  # Escreve os valores

# Cria uma planilha para a quantidade de produtos vendidos
worksheet_quantidade = workbook.add_worksheet('Quantidade')

# Dados de outra métrica (por exemplo, quantidade de produtos vendidos)
dados_quantidade = {
    'Loja': ['Loja A', 'Loja B', 'Loja C'],
    'Vendas': [5000, 7000, 3000],
    'Lucro': [1000, 1500, 800]
}

# Escreve os dados de quantidade na planilha
colunas = list(dados_quantidade.keys())
for col, titulo in enumerate(colunas):
    worksheet_quantidade.write(0, col, titulo)  # Escreve os títulos das colunas
    for row, valor in enumerate(dados_quantidade[titulo]):
        worksheet_quantidade.write(row + 1, col, valor)  # Escreve os valores

# Fecha o arquivo Excel
workbook.close()

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")