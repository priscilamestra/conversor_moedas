import streamlit as st

# Importa a lógica de cálculo do seu arquivo
from currency_converter import brl_to, SUPPORTED


# Configuração da aba do navegador
st.set_page_config(
    page_title="Currency Converter",
    page_icon="💱"
)


# Título da aplicação web
st.title("💱 Currency Converter (BRL Base)")
st.markdown("Check **real-time** exchange rates using the Frankfurter API.")


# Organização visual em duas colunas
col1, col2 = st.columns(2)

with col1:
    valor_input = st.number_input(
        "Enter the amount in Brazilian Reais (BRL):",
        min_value=0.0,
        value=None,
        step=10.0,
        placeholder="0,00",
        key="valor_brl"
    )

with col2:
    moeda_destino = st.selectbox(
        "Which currency?",
        sorted(list(SUPPORTED)),
        key="moeda_destino"
    )


st.write("---")


# Botão de ação
if st.button("Convert Currency", type="primary"):

    # Impede conversão sem valor informado
    if valor_input is None:
        st.warning("Please enter an amount in Brazilian Reais (BRL).")

    elif valor_input <= 0:
        st.warning("Please enter an amount greater than zero.")

    else:
        try:
            # Chama a função original de conversão
            resultado = brl_to(
                moeda_destino,
                valor_input
            )

            # Renderiza o resultado na tela
            st.success("Conversion completed successfully!")

            st.metric(
                label=f"Amount converted to {moeda_destino}",
                value=f"{resultado:.2f} {moeda_destino}"
            )

        except Exception as e:
            st.error(f"Conversion error: {e}")