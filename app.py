import os
import streamlit as st
import pandas as pd
import plotly.express as px
from io import BytesIO

from core.classificacao import classificar_centro_custo
from core.parser import parse_xml
from utils.prompt_loader import carregar_prompt

# Configuração visual
st.set_page_config(
    page_title="Classificador de Centro de Custo",
    page_icon="📁",
    layout="wide",
    initial_sidebar_state="collapsed"
)

hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 5rem;
            padding-right: 5rem;
        }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Carrega template do prompt
PROMPT_PATH = os.path.join('prompts', 'prompt_classificacao.txt')
prompt_template = carregar_prompt(PROMPT_PATH)

# Interface
st.markdown("## 🧾 Classificador de Centro de Custo via XML de NF-e")
st.markdown(
    "Envie arquivos XML contendo informações de produtos/serviços. "
    "A IA classificará cada item no centro de custo mais apropriado com base na descrição."
)
st.markdown("---")

uploaded_files = st.file_uploader(
    "📂 Envie arquivos XML (NF-e)",
    type="xml",
    accept_multiple_files=True
)

if uploaded_files:
    dados = []
    with st.spinner("🔍 Extraindo e classificando os dados..."):
        for file in uploaded_files:
            parsed = parse_xml(file)
            centro_custo = classificar_centro_custo(parsed["descricao"], prompt_template)
            parsed["centro_custo"] = centro_custo
            dados.append(parsed)

    df = pd.DataFrame(dados)

    st.markdown("### 📋 Tabela de Despesas Classificadas")
    st.dataframe(df, use_container_width=True)

    st.markdown("---")
    st.markdown("## 📊 Dashboard")

    fig = px.histogram(
        df,
        x="centro_custo",
        title="Distribuição de Despesas por Centro de Custo",
        color="centro_custo"
    )
    st.plotly_chart(fig, use_container_width=True)

    resumo = df.groupby("centro_custo")["valor"].sum().reset_index()
    resumo = resumo.sort_values(by="valor", ascending=False)

    st.markdown("### 💰 Total de Gastos por Centro de Custo")
    st.dataframe(resumo, use_container_width=True)

    # Exportar Excel
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Classificação')
    output.seek(0)

    st.download_button(
        label="📥 Baixar resultado em Excel",
        data=output,
        file_name="classificacao_centro_custo.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
else:
    st.info("📤 Envie ao menos um arquivo XML de Nota Fiscal para começar.")
