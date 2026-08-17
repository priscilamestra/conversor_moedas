import streamlit as st

# Importa a lógica de cálculo do seu arquivo
from currency_converter import brl_to, SUPPORTED 

# Configuração da aba do navegador
st.set_page_config(page_title="Conversor de Moedas", page_icon="💱")

# Título da aplicação web
st.title("💱 Conversor de Moedas (Base BRL)")
st.markdown("Consulte cotações em **tempo real** usando a API Frankfurter.")

# Organização visual em duas colunas
col1, col2 = st.columns(2)

with col1:
    valor_input = st.number_input("Digite o valor em Reais (R$):", min_value=0.01, value=100.00, step=10.0)

with col2:
    moeda_destino = st.selectbox("Para qual moeda?", sorted(list(SUPPORTED)))

st.write("---") 

# Botão de ação
if st.button("Converter Moeda", type="primary"):
    try:
        # Chama a SUA função original
        resultado = brl_to(moeda_destino, valor_input)
        
        # Renderiza o resultado na tela
        st.success("Conversão realizada com sucesso!")
        st.metric(
            label=f"Valor convertido para {moeda_destino}", 
            value=f"{resultado:.2f} {moeda_destino}"
        )
        
    except Exception as e:
        st.error(f"Erro na conversão: {e}")