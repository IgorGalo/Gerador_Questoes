import streamlit as st

from utils.questoes import TIPOS, LETRAS, corrigir, texto_gabarito


def renderizar_simulado(questoes):
    """Renderiza o simulado e realiza a correção das respostas."""

    fin = st.session_state.finalizado
    rodada = st.session_state.rodada

    st.subheader("Responda às questões")

    for i, q in enumerate(questoes):
        chave = f"r_{rodada}_{i}"

        with st.container(border=True):
            st.markdown(
                f"**Questão {i + 1}** · _{TIPOS[q['tipo']]}_"
            )

            st.markdown(q["enunciado"])

            if q["tipo"] == "multipla_escolha":
                st.radio(
                    "Resposta",
                    range(len(q["alternativas"])),
                    index=None,
                    key=chave,
                    format_func=lambda j, q=q:
                        f"{LETRAS[j]}) {q['alternativas'][j]}",
                    disabled=fin,
                    label_visibility="collapsed"
                )

            elif q["tipo"] == "verdadeiro_falso":
                st.radio(
                    "Resposta",
                    ["Verdadeiro", "Falso"],
                    index=None,
                    key=chave,
                    disabled=fin,
                    label_visibility="collapsed"
                )

            else:
                st.text_input(
                    "Resposta",
                    key=chave,
                    disabled=fin,
                    label_visibility="collapsed",
                    placeholder="Digite sua resposta curta"
                )

            if fin:
                ok = corrigir(q, st.session_state.get(chave))

                (st.success if ok else st.error)(
                    "✅ Correto" if ok else "❌ Incorreto"
                )

                st.markdown(
                    f"**Gabarito:** {texto_gabarito(q)}"
                )

                st.write(q.get("explicacao", ""))

    if not fin:
        if st.button("Finalizar simulado", type="primary"):
            st.session_state.finalizado = True
            st.rerun()

    else:
        acertos = sum(
            corrigir(q, st.session_state.get(f"r_{rodada}_{i}"))
            for i, q in enumerate(questoes)
        )

        total = len(questoes)

        st.metric(
            "Pontuação",
            f"{acertos}/{total}",
            f"{100 * acertos / total:.0f}%"
        )

        st.caption(
            "Respostas curtas são corrigidas de forma aproximada "
            "(palavras-chave); confira o gabarito."
        )

        if st.button("Refazer simulado"):
            st.session_state.rodada += 1
            st.session_state.finalizado = False
            st.rerun()