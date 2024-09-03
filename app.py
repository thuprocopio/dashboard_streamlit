import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go


st.title('Indicadores de Continuidade (DEC/FEC)')

date_column = 'Mes'
data_url = 'DEC_FEC_Consolidado_Distribuidora.xlsx'

data = pd.read_excel(data_url)
    
st.subheader('Base de Dados')
st.write(data)


# Converte os dados em um DataFrame
df = data.copy()

# Interface do usuário
st.title('DEC Global (12M)')

# Cria duas colunas
col1, col2 = st.columns(2)

# Seleção da distribuidora
with col1:
    distribuidora_selecionada = st.selectbox('Selecione a distribuidora:', df['Nome_Distribuidora'].unique(), index=0, key="distribuidora_select")

# Seleção do ano de início da análise
with col2:
    competencia_selecionada_1 = st.selectbox('Selecione o ano de início da análise:', df['Ano'].unique(), index=0, key="ano_select")

# Filtro dos dados pela distribuidora e ano selecionados
grafico_df = df[(df['Nome_Distribuidora'] == distribuidora_selecionada) & (df['Ano'] >= competencia_selecionada_1)]


# Criação do gráfico interativo com Plotly
fig = go.Figure()

# Adicionando os dados das barras empilhadas

fig.add_trace(go.Bar(
    x=grafico_df['Mes'],
    y=grafico_df['DEC apu INT_a'],
    name='DEC Apurado',
    marker_color='#18A0AE',
    text=grafico_df['DEC apu INT_a'],
    textposition='inside',
    hoverinfo='text'
))

fig.add_trace(go.Bar(
    x=grafico_df['Mes'],
    y=grafico_df['DEC exp TOTAL_a'],
    name='DEC Expurgado',
    marker_color='#e6e6e6',
    text=grafico_df['DEC exp TOTAL_a'],
    textposition='inside',
    hoverinfo='text'
))
# Adicionando a linha tracejada para DEC Limite
fig.add_trace(go.Scatter(
    x=grafico_df['Mes'],
    y=grafico_df['DEC LIMITE'],
    name='DEC Limite',
    mode='lines+markers',  # Marca pontos na linha
    line=dict(dash='dash', color='#E95445'),  # Linha tracejada
    hoverinfo='text',
    text=grafico_df['DEC LIMITE']
))

# Atualizando o layout do gráfico
fig.update_layout(
    title='Indicadores globais DEC (12M)',
    barmode='stack',
    xaxis_title='Competência',
    yaxis_title='Valores',
    legend_title='Legend',
    font=dict(color='white'),
    title_font=dict(size=12),
    plot_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
    paper_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
)

# Alterando a cor dos eixos
fig.update_xaxes(title_font=dict(color='white'), tickfont=dict(color='white'))
fig.update_yaxes(title_font=dict(color='white'), tickfont=dict(color='white'))
fig.update_layout(legend=dict(font=dict(color='white')))

# Exibir o gráfico interativo
st.plotly_chart(fig, use_container_width=True)
