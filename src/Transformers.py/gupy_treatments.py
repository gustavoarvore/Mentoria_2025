import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
with open('./data/vagas_gupy.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

# Criar um DataFrame
df = pd.DataFrame(dados['vagas'])

# Exibir as primeiras linhas do DataFrame
print(df.head())

# Análise Exploratória
# Exemplo: Contar o número de vagas por empresa
vagas_por_empresa = df['company'].value_counts()

# Visualizar os dados
plt.figure(figsize=(10, 6))
sns.barplot(x=vagas_por_empresa.index, y=vagas_por_empresa.values)
plt.xticks(rotation=90)
plt.title('Número de Vagas por Empresa')
plt.xlabel('Empresa')
plt.ylabel('Número de Vagas')
plt.show()