"""
Gerador Inteligente de Questões - Interface (Parte 2)

Contrato com o módulo da Parte 1 (arquivo gerador.py):

    gerar_questoes(texto: str, quantidade: int, tipos: list[str]) -> list[dict]

    tipos: subconjunto de ["multipla_escolha", "verdadeiro_falso", "resposta_curta"]

    Cada questão é um dict:
      multipla_escolha : {"tipo", "enunciado", "alternativas": [4 str],
                          "resposta_correta": int (0-3), "explicacao": str}
      verdadeiro_falso : {"tipo", "enunciado", "resposta_correta": bool, "explicacao": str}
      resposta_curta   : {"tipo", "enunciado", "resposta_correta": str, "explicacao": str}

Enquanto gerador.py não existir, usa gerador_mock.py (questões de exemplo).
"""
import streamlit as st

from utils.questoes import validar_questao
from interface.barra_lateral import renderizar_barra_lateral
from interface.revisao import renderizar_revisao
from interface.simulado import renderizar_simulado

try:
    from gerador import gerar_questoes
    USANDO_MOCK = False
except ModuleNotFoundError as e:
    if e.name != "gerador":
        raise  # o gerador existe, mas falta uma dependência dele (torch etc.)
    from gerador_mock import gerar_questoes
    USANDO_MOCK = True


# ---------- estado ----------
st.set_page_config(page_title="Gerador de Questões", page_icon="📝", layout="wide")
for chave, valor in {"questoes": [], "rodada": 0, "finalizado": False}.items():
    st.session_state.setdefault(chave, valor)

st.title("📝 Gerador Inteligente de Questões")
st.caption("Cole um texto didático ou envie um TXT e gere questões de revisão com gabarito.")
if USANDO_MOCK:
    st.warning("Modo demonstração: `gerador.py` não encontrado, usando questões de exemplo (`gerador_mock.py`).")


texto, quantidade, tipos_sel, gerar = renderizar_barra_lateral()

if gerar:
    if len(texto) < 200:
        st.sidebar.error("Informe um texto com pelo menos 200 caracteres.")
    elif not tipos_sel:
        st.sidebar.error("Selecione ao menos um tipo de questão.")
    else:
        try:
            with st.spinner("Gerando questões... isso pode levar alguns instantes."):
                bruto = gerar_questoes(texto, quantidade, tipos_sel)
            validas = [q for q in bruto if validar_questao(q)]
            if len(validas) < len(bruto):
                st.sidebar.warning(f"{len(bruto) - len(validas)} questão(ões) inválida(s) descartada(s).")
            if not validas:
                st.sidebar.error("Nenhuma questão válida foi gerada. Tente novamente.")
            else:
                st.session_state.questoes = validas
                st.session_state.rodada += 1
                st.session_state.finalizado = False
        except Exception as e:  # erro do modelo não deve derrubar a interface
            st.sidebar.error(f"Erro ao gerar questões: {e}")

questoes = st.session_state.questoes
if not questoes:
    st.info("Configure o conteúdo na barra lateral e clique em **Gerar questões**.")
    st.stop()

aba_rev, aba_sim = st.tabs(["📖 Revisão (com gabarito)", "🎯 Modo simulado"])

with aba_rev:
    renderizar_revisao(questoes)

with aba_sim:
    renderizar_simulado(questoes)