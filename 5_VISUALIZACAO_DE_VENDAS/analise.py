import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Carregar dados
df = pd.read_csv("dados_vendas_dashboard.csv")

print("=== ANÁLISE EXPLORATÓRIA ===")
print(f"Shape do dataset: {df.shape}")
print(f"Colunas: {list(df.columns)}")
print(f"Dados nulos:\n{df.isnull().sum()}")

# Tratar dados
df['Data_Venda'] = pd.to_datetime(df['Data_Venda'])
df = df.fillna(0)

# 1. Resumo Geral - Vendas ao Longo do Tempo
resumo_geral = df.groupby("Data_Venda").sum(numeric_only=True).reset_index()

fig1 = px.line(
    resumo_geral,
    x="Data_Venda",
    y="Quantidade",
    title="📈 Resumo Geral: Vendas ao Longo do Tempo",
    labels={'Quantidade': 'Quantidade Vendida', 'Data_Venda': 'Data'},
    markers=True
)
fig1.update_layout(width=1000, height=500, template='plotly_white')
fig1.show()

# 2. Vendas Por Produto
vendas_por_produto = df.groupby("Produto").sum(numeric_only=True).reset_index().sort_values('Quantidade', ascending=False)

fig2 = px.bar(
    vendas_por_produto,
    x="Produto",
    y="Quantidade",
    color="Produto",
    title="📊 Vendas Por Produto (Quantidade Total)",
    text_auto=True
)
fig2.update_layout(width=1000, height=600, template='plotly_white', xaxis_tickangle=-45)
fig2.update_traces(textposition='outside')
fig2.show()

# 3. Distribuição Regional
vendas_por_regiao = df.groupby("Região").sum(numeric_only=True).reset_index()

fig3 = px.pie(
    vendas_por_regiao,
    names="Região",
    values="Quantidade",
    title="🗺️ Distribuição Regional das Vendas",
    hole=0.3
)
fig3.update_layout(width=800, height=600, template='plotly_white')
fig3.update_traces(textinfo='percent+label+value')
fig3.show()

# 4. Heatmap - Relação entre Categorias e Regiões
heatmap_data = df.pivot_table(
    index="Região", 
    columns="Categoria", 
    values="Quantidade", 
    aggfunc="sum",
    fill_value=0
)

fig4 = px.imshow(
    heatmap_data,
    title="🔥 Relação entre Categorias e Regiões - Heatmap",
    color_continuous_scale="Blues",
    aspect="auto",
    labels=dict(x="Categoria", y="Região", color="Quantidade Vendida")
)
fig4.update_layout(width=1000, height=600, template='plotly_white')
fig4.update_xaxes(side="top")
fig4.show()

# 5. Acompanhamento de Produtos Populares
produtos_populares = df.groupby(['Data_Venda', 'Produto']).sum(numeric_only=True).reset_index()

# Top 5 produtos mais vendidos para não poluir o gráfico
top_produtos = df.groupby('Produto')['Quantidade'].sum().nlargest(5).index
df_top = produtos_populares[produtos_populares['Produto'].isin(top_produtos)]

fig5 = px.line(
    df_top,
    x="Data_Venda",
    y="Quantidade",
    color="Produto",
    title="⭐ Top 5 Produtos Populares - Evolução Temporal",
    markers=True
)
fig5.update_layout(width=1000, height=600, template='plotly_white')
fig5.show()

# 6. Dashboard Resumo (Bônus)
print("\n=== 📋 RELATÓRIO ESTATÍSTICO ===")
print(f"Total de Vendas: {df['Quantidade'].sum():,} unidades")
print(f"Período: {df['Data_Venda'].min().date()} a {df['Data_Venda'].max().date()}")
print(f"Produto Mais Vendido: {vendas_por_produto.iloc[0]['Produto']} ({vendas_por_produto.iloc[0]['Quantidade']:,} unidades)")
print(f"Região com Maior Volume: {vendas_por_regiao.loc[vendas_por_regiao['Quantidade'].idxmax(), 'Região']}")

# Salvar gráficos
fig1.write_html("1_resumo_geral_vendas.html")
fig2.write_html("2_vendas_por_produto.html")
fig3.write_html("3_distribuicao_regional.html")
fig4.write_html("4_heatmap_categorias_regioes.html")
fig5.write_html("5_produtos_populares.html")

print("✅ Análise concluída! Gráficos salvos como HTML.")