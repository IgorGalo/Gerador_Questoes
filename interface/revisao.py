import streamlit as st

from utils.questoes import TIPOS, LETRAS, texto_gabarito


def renderizar_revisao(questoes):
    """Renderiza a aba de revisão com gabarito."""

    st.subheader(f"{len(questoes)} questões geradas")

    for i, q in enumerate(questoes):
        with st.container(border=True):
            st.markdown(
                f"**Questão {i + 1}** · _{TIPOS[q['tipo']]}_"
            )

            st.markdown(q["enunciado"])

            if q["tipo"] == "multipla_escolha":
                for j, alt in enumerate(q["alternativas"]):
                    st.markdown(f"{LETRAS[j]}) {alt}")

            with st.expander("Ver gabarito e explicação"):
                st.success(
                    f"Resposta correta: {texto_gabarito(q)}"
                )

                st.write(q.get("explicacao", "Sem explicação."))