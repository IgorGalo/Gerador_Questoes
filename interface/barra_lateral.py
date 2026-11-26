import streamlit as st

from utils.arquivos import ler_arquivo
from utils.questoes import TIPOS


LIMITE_CARACTERES_AVISO = 12000


def renderizar_barra_lateral():

    # Entrada e configuração
    with st.sidebar:
        st.header("1. Conteúdo")

        modo = st.radio(
            "Como enviar o texto?",
            ["Colar texto", "Enviar arquivo TXT"]
        )

        texto = ""

        if modo == "Colar texto":
            texto = st.text_area(
                "Texto de estudo",
                height=260,
                placeholder="Cole aqui o conteúdo..."
            )
        else:
            arq = st.file_uploader("Arquivo .txt", type=["txt"])

            if arq:
                texto = ler_arquivo(arq)

                with st.expander("Pré-visualizar texto"):
                    st.text(
                        texto[:1500] +
                        ("..." if len(texto) > 1500 else "")
                    )

        texto = texto.strip()

        st.caption(f"{len(texto)} caracteres")

        if len(texto) > LIMITE_CARACTERES_AVISO:
            st.warning(
                "Texto longo: o modelo pode perder qualidade. "
                "Considere enviar um trecho menor."
            )

        st.header("2. Configuração")

        quantidade = st.slider(
            "Quantidade de questões", 1, 20, 5
        )

        tipos_sel = st.multiselect(
            "Tipos de questão",
            list(TIPOS),
            default=list(TIPOS),
            format_func=TIPOS.get
        )

        gerar = st.button(
            "Gerar questões",
            type="primary",
            use_container_width=True
        )

    return texto, quantidade, tipos_sel, gerar