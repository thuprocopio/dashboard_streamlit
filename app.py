import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go



st.markdown("<h1 style='text-align: center;'>Indicadores de Continuidade (DEC/FEC) - Distribuidoras</h1>", unsafe_allow_html=True)

data_url = 'DEC_FEC_Consolidado_Distribuidora.xlsx'

data = pd.read_excel(data_url)

data['DEC exp EXT_a'] = data['DEC exp EXT_a'].astype(str).replace(",",".").astype(float)
data['DEC apu INT_a'] = data['DEC apu INT_a'].astype(str).replace(",",".").astype(float)
data['DEC exp ISE_a'] = data['DEC exp ISE_a'].astype(str).replace(",",".").astype(float)
data['DEC exp DC_a'] = data['DEC exp DC_a'].astype(str).replace(",",".").astype(float)
data['DEC exp ERAC_a'] = data['DEC exp ERAC_a'].astype(str).replace(",",".").astype(float)

data['FEC exp EXT_a'] = data['FEC exp EXT_a'].astype(str).replace(",",".").astype(float)
data['FEC apu INT_a'] = data['FEC apu INT_a'].astype(str).replace(",",".").astype(float)
data['FEC exp ISE_a'] = data['FEC exp ISE_a'].astype(str).replace(",",".").astype(float)
data['FEC exp DC_a'] = data['FEC exp DC_a'].astype(str).replace(",",".").astype(float)
data['FEC exp ERAC_a'] = data['FEC exp ERAC_a'].astype(str).replace(",",".").astype(float)
    
# Configurando colunas
col1, col2 = st.columns([3, 100])  # Ajuste as proporções conforme necessário

with col1:
    mostrar_dados = st.checkbox('', value=False)

with col2:
    st.subheader('Base de Dados')

if mostrar_dados:
    st.write(data)

# Converte os dados em um DataFrame
df = data.copy()

st.markdown("<h2 style='text-align: center;'>Indicadores Anualizados (12M)</h2>", unsafe_allow_html=True)
# Cria duas colunas
col1, col2, col3, col4 = st.columns(4)

# Seleção da indicador
with col1:
    indicador_selecionado_12m = st.selectbox('Selecione o indicador:', ['DEC', 'FEC'], index=0, key="indicador_select_12m")

# Seleção da distribuidora
with col2:
    distribuidora_selecionada_12m = st.selectbox('Selecione a distribuidora:', df['Nome_Distribuidora'].unique(), index=0, key="distribuidora_select_12m")

# Seleção do ano de início da análise
with col3:
    competencia_selecionada_1_12m = st.selectbox('Selecione o ano inicial da análise:', df['Ano'].unique(), index=0, key="ano_select1_12m")

with col4:
    competencia_selecionada_2_12m = st.selectbox('Selecione o ano final da análise:', df['Ano'].unique(), index=0, key="ano_select2_12m")

# Filtro dos dados pela distribuidora e ano selecionados
grafico_df = df[(df['Nome_Distribuidora'] == distribuidora_selecionada_12m) & (df['Ano'] >= competencia_selecionada_1_12m) & (df['Ano'] <= competencia_selecionada_2_12m)]


# Criação do gráfico interativo com Plotly
fig = go.Figure()

# Adicionando os dados das barras empilhadas

if indicador_selecionado_12m == 'DEC':
# Interface do usuário
    st.subheader('DEC Global Total (12M)')

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
        y=grafico_df['DEC exp ISE_a'],
        name='DEC Expurgado ISE',
        marker_color='#059046',
        text=grafico_df['DEC exp ISE_a'],
        textposition='inside',
        hoverinfo='text'
    ))

    fig.add_trace(go.Bar(
        x=grafico_df['Mes'],
        y=grafico_df['DEC exp DC_a'],
        name='DEC Expurgado DICRI',
        marker_color='#EC9533',
        text=grafico_df['DEC exp DC_a'],
        textposition='inside',
        hoverinfo='text'
    ))

    fig.add_trace(go.Bar(
        x=grafico_df['Mes'],
        y=grafico_df['DEC exp ERAC_a'],
        name='DEC Expurgado ERAC',
        marker_color='#0058FF',
        text=grafico_df['DEC exp ERAC_a'],
        textposition='inside',
        hoverinfo='text'
    ))

    fig.add_trace(go.Bar(
        x=grafico_df['Mes'],
        y=grafico_df['DEC exp EXT_a'],
        name='DEC Expurgado Externo',
        marker_color='#e6e6e6',
        text=grafico_df['DEC exp EXT_a'],
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
        title='',
        barmode='stack',
        xaxis_title='Competência',
        yaxis_title='DEC [horas]',
        legend_title='Legend',
        font=dict(color='white'),
        title_font=dict(size=12),
        plot_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
        paper_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
    )
if indicador_selecionado_12m == 'FEC':
# Interface do usuário
    st.subheader('FEC Global Total (12M)')

    fig.add_trace(go.Bar(
        x=grafico_df['Mes'],
        y=grafico_df['FEC apu INT_a'],
        name='FEC Apurado',
        marker_color='#18A0AE',
        text=grafico_df['FEC apu INT_a'],
        textposition='inside',
        hoverinfo='text'
    ))

    fig.add_trace(go.Bar(
        x=grafico_df['Mes'],
        y=grafico_df['FEC exp ISE_a'],
        name='FEC Expurgado ISE',
        marker_color='#059046',
        text=grafico_df['FEC exp ISE_a'],
        textposition='inside',
        hoverinfo='text'
    ))

    fig.add_trace(go.Bar(
        x=grafico_df['Mes'],
        y=grafico_df['FEC exp DC_a'],
        name='FEC Expurgado DICRI',
        marker_color='#EC9533',
        text=grafico_df['FEC exp DC_a'],
        textposition='inside',
        hoverinfo='text'
    ))

    fig.add_trace(go.Bar(
        x=grafico_df['Mes'],
        y=grafico_df['FEC exp ERAC_a'],
        name='FEC Expurgado ERAC',
        marker_color='#0058FF',
        text=grafico_df['FEC exp ERAC_a'],
        textposition='inside',
        hoverinfo='text'
    ))

    fig.add_trace(go.Bar(
        x=grafico_df['Mes'],
        y=grafico_df['FEC exp EXT_a'],
        name='FEC Expurgado Externo',
        marker_color='#e6e6e6',
        text=grafico_df['FEC exp EXT_a'],
        textposition='inside',
        hoverinfo='text'
    ))
# Adicionando a linha tracejada para FEC Limite
    fig.add_trace(go.Scatter(
        x=grafico_df['Mes'],
        y=grafico_df['FEC LIMITE'],
        name='FEC Limite',
        mode='lines+markers',  # Marca pontos na linha
        line=dict(dash='dash', color='#E95445'),  # Linha tracejada
        hoverinfo='text',
        text=grafico_df['FEC LIMITE']
    ))

    # Atualizando o layout do gráfico
    fig.update_layout(
        title='Indicadores globais FEC TOTAL(12M)',
        barmode='stack',
        xaxis_title='Competência',
        yaxis_title='FEC [vezes]',
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

st.markdown("<h2 style='text-align: center;'>Indicadores Ano</h2>", unsafe_allow_html=True)

grafico_df_ano_1 = df[df['Mes'].str.startswith('Dezembro')]

col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

# Seleção da indicador
with col1:
    competencia_selecionada_1_ano = st.selectbox('Selecione o ano da análise:', grafico_df_ano_1['Ano'].unique(), index=0, key="ano_select_ano_1")

# Cria duas colunas
col1, col2 = st.columns([1, 1])

# Seleção da indicador
with col1:

    grafico_df_ano_1 = grafico_df_ano_1[(grafico_df_ano_1['Ano'] == competencia_selecionada_1_ano)].sort_values(by='DECTOT_a')

    # Criação do gráfico interativo com Plotly
    fig2 = go.Figure()

    st.subheader('DEC Global Total')

    fig2.add_trace(go.Bar(
        y=grafico_df_ano_1['Nome_Distribuidora'],
        x=grafico_df_ano_1['DEC apu INT_a'],
        name='DEC Apurado',
        orientation='h',
        marker_color='#18A0AE',
        text=grafico_df_ano_1['DEC apu INT_a'],
        textposition='inside',
        hoverinfo='text'
    ))

    fig2.add_trace(go.Bar(
        y=grafico_df_ano_1['Nome_Distribuidora'],
        x=grafico_df_ano_1['DEC exp ISE_a'],
        name='DEC Expurgado ISE',
        orientation='h',
        marker_color='#059046',
        text=grafico_df_ano_1['DEC exp ISE_a'],
        textposition='inside',
        hoverinfo='text'
    ))

    fig2.add_trace(go.Bar(
        y=grafico_df_ano_1['Nome_Distribuidora'],
        x=grafico_df_ano_1['DEC exp DC_a'],
        name='DEC Expurgado DICRI',
        orientation='h',
        marker_color='#EC9533',
        text=grafico_df_ano_1['DEC exp DC_a'],
        textposition='inside',
        hoverinfo='text'
    ))

    fig2.add_trace(go.Bar(
        y=grafico_df_ano_1['Nome_Distribuidora'],
        x=grafico_df_ano_1['DEC exp ERAC_a'],
        name='DEC Expurgado ERAC',
        orientation='h',
        marker_color='#0058FF',
        text=grafico_df_ano_1['DEC exp ERAC_a'],
        textposition='inside',
        hoverinfo='text'
    ))

    fig2.add_trace(go.Bar(
        y=grafico_df_ano_1['Nome_Distribuidora'],
        x=grafico_df_ano_1['DEC exp EXT_a'],
        name='DEC Expurgado Externo',
        orientation='h',
        marker_color='#e6e6e6',
        text=grafico_df_ano_1['DEC exp EXT_a'],
        textposition='inside',
        hoverinfo='text'
    ))

    # Atualizando o layout do gráfico
    fig2.update_layout(
        title='',
        barmode='stack',
        xaxis_title='DEC [horas]',
        yaxis_title='Distribuidora',
        legend_title='Legend',
        font=dict(color='white'),
        title_font=dict(size=12),
        plot_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
        paper_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
        width=600,  # Aumentando a largura do gráfico
        height=1200   # Ajuste a altura se necessário
    )
    # Alterando a cor dos eixos
    fig2.update_xaxes(title_font=dict(color='white'), tickfont=dict(color='white'))
    fig2.update_yaxes(title_font=dict(color='white'), tickfont=dict(color='white'))
    fig2.update_layout(legend=dict(font=dict(color='white')))

    # Exibir o gráfico interativo
    st.plotly_chart(fig2, use_container_width=True)


with col2:

    grafico_df_ano_2 = grafico_df_ano_1[(grafico_df_ano_1['Ano'] == competencia_selecionada_1_ano)].sort_values(by='FECTOT_a')

    # Criação do gráfico interativo com Plotly
    fig3 = go.Figure()

    st.subheader('FEC Global Total')

    fig3.add_trace(go.Bar(
        y=grafico_df_ano_2['Nome_Distribuidora'],
        x=grafico_df_ano_2['FEC apu INT_a'],
        name='FEC Apurado',
        orientation='h',
        marker_color='#18A0AE',
        text=grafico_df_ano_2['FEC apu INT_a'],
        textposition='inside',
        hoverinfo='text'
    ))

    fig3.add_trace(go.Bar(
        y=grafico_df_ano_2['Nome_Distribuidora'],
        x=grafico_df_ano_2['FEC exp ISE_a'],
        name='FEC Expurgado ISE',
        orientation='h',
        marker_color='#059046',
        text=grafico_df_ano_2['FEC exp ISE_a'],
        textposition='inside',
        hoverinfo='text'
    ))

    fig3.add_trace(go.Bar(
        y=grafico_df_ano_2['Nome_Distribuidora'],
        x=grafico_df_ano_2['FEC exp DC_a'],
        name='FEC Expurgado DICRI',
        orientation='h',
        marker_color='#EC9533',
        text=grafico_df_ano_2['FEC exp DC_a'],
        textposition='inside',
        hoverinfo='text'
    ))

    fig3.add_trace(go.Bar(
        y=grafico_df_ano_2['Nome_Distribuidora'],
        x=grafico_df_ano_2['FEC exp ERAC_a'],
        name='FEC Expurgado ERAC',
        orientation='h',
        marker_color='#0058FF',
        text=grafico_df_ano_2['FEC exp ERAC_a'],
        textposition='inside',
        hoverinfo='text'
    ))

    fig3.add_trace(go.Bar(
        y=grafico_df_ano_2['Nome_Distribuidora'],
        x=grafico_df_ano_2['FEC exp EXT_a'],
        name='FEC Expurgado Externo',
        orientation='h',
        marker_color='#e6e6e6',
        text=grafico_df_ano_2['FEC exp EXT_a'],
        textposition='inside',
        hoverinfo='text'
    ))

    # Atualizando o layout do gráfico
    fig3.update_layout(
        title='',
        barmode='stack',
        xaxis_title='FEC [vezes]',
        yaxis_title='Distribuidora',
        legend_title='Legend',
        font=dict(color='white'),
        title_font=dict(size=12),
        plot_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
        paper_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
        width=600,  # Aumentando a largura do gráfico
        height=1200   # Ajuste a altura se necessário
    )
    # Alterando a cor dos eixos
    fig3.update_xaxes(title_font=dict(color='white'), tickfont=dict(color='white'))
    fig3.update_yaxes(title_font=dict(color='white'), tickfont=dict(color='white'))
    fig3.update_layout(legend=dict(font=dict(color='white')))

    # Exibir o gráfico interativo
    st.plotly_chart(fig3, use_container_width=True)