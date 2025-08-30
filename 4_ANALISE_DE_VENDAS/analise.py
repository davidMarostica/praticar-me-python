import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv('vendas_100.csv')

print("=== PRIMEIRAS LINHAS DO DATASET ===")
print(df.head())
print(f"\nShape do dataset: {df.shape}")
print(f"\nColunas disponíveis: {list(df.columns)}")

# Verificar dados nulos
print("\n=== DADOS NULOS ===")
print(df.isnull().sum())

# Tratar dados nulos (se necessário)
df = df.dropna()

# Calcular valor total com desconto
df["Valor_Total"] = df["Quantidade"] * df["Preço_Unitário"] * (1 - df['Desconto'])

# Análises principais
print("\n=== ANÁLISES PRINCIPAIS ===")

# 1. Vendas por cidade
vendas_por_cidade = df.groupby("Cidade")["Valor_Total"].sum().sort_values(ascending=False)
print("\n1. Vendas por Cidade:")
print(vendas_por_cidade)

# 2. Produtos mais vendidos
analise_produtos = df.groupby("Produto").agg({
    'Quantidade': 'sum',
    'Valor_Total': 'sum'
}).sort_values('Quantidade', ascending=False)

print("\n2. Top 5 Produtos Mais Vendidos:")
print(analise_produtos.head())

# 3. Receita total e por categoria
receita_total = df["Valor_Total"].sum()
receita_por_categoria = df.groupby("Categoria")["Valor_Total"].sum().sort_values(ascending=False)

print(f"\n3. Receita Total: R$ {receita_total:,.2f}")
print("\n4. Receita por Categoria:")
print(receita_por_categoria)

# 4. Análise temporal (se existir data)
if 'Data' in df.columns:
    df['Data'] = pd.to_datetime(df['Data'])
    vendas_por_mes = df.groupby(df['Data'].dt.to_period('M'))['Valor_Total'].sum()
    print("\n5. Vendas por Mês:")
    print(vendas_por_mes)

# Salvar resultados
vendas_por_cidade.to_csv("vendas_por_cidade.csv", header=["Total_Vendas"])
receita_por_categoria.to_csv("receita_por_categoria.csv", header=["Receita_Total"])
analise_produtos.to_csv("analise_produtos.csv")

print("\n=== ARQUIVOS SALVOS ===")
print("• vendas_por_cidade.csv")
print("• receita_por_categoria.csv") 
print("• analise_produtos.csv")

# Gerar gráficos (opcional)
try:
    vendas_por_cidade.plot(kind='bar', title='Vendas por Cidade', figsize=(10, 6))
    plt.ylabel('Valor Total (R$)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('vendas_por_cidade.png')
    plt.show()
    
except Exception as e:
    print(f"Erro ao gerar gráficos: {e}")

print("\n=== ANÁLISE CONCLUÍDA ===")