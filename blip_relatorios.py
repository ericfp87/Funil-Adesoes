import os
import pandas as pd

diretorio = 'G:\\Drives compartilhados\\Analise de Dados\\02 - Projetos\\03 - Relatorios\\Adesões Funil\\Blip'

dfs = []

for arquivo in os.listdir(diretorio):
    if arquivo.endswith(".csv"):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        
        df = pd.read_csv(caminho_arquivo, delimiter=";", encoding="utf-8")
        dfs.append(df)

df_final = pd.concat(dfs, ignore_index=True)

arquivo_inicial = 'G:\\Drives compartilhados\\Analise de Dados\\02 - Projetos\\03 - Relatorios\\Adesões Funil\\Arquivos\\Documento Final\\Blip_relatorios.csv'

os.remove(arquivo_inicial)

arquivo_final = 'G:\\Drives compartilhados\\Analise de Dados\\02 - Projetos\\03 - Relatorios\\Adesões Funil\\Arquivos\\Documento Final\\Blip_relatorios.csv'

df_final.to_csv(arquivo_final, encoding="utf-8", index=False)

print(f'Arquivo final salvo em: {arquivo_final}')
