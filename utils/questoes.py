import difflib
import re
import unicodedata

TIPOS = {
    "multipla_escolha": "Múltipla escolha",
    "verdadeiro_falso": "Verdadeiro ou falso",
    "resposta_curta": "Resposta curta",
}
LETRAS = "ABCDEFGH"


def normalizar(s: str) -> str:
    s = unicodedata.normalize("NFD", str(s).lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return " ".join(re.sub(r"[^a-z0-9 ]+", " ", s).split())


def resposta_curta_correta(resposta: str, gabarito: str) -> bool:
    """Correção aproximada: similaridade de texto ou cobertura das palavras-chave do gabarito."""
    r, g = normalizar(resposta), normalizar(gabarito)
    if not r:
        return False
    if r == g or g in r:
        return True
    if difflib.SequenceMatcher(None, r, g).ratio() >= 0.8:
        return True
    palavras = [p for p in g.split() if len(p) > 3]
    if not palavras:
        return False
    cobertas = sum(1 for p in palavras if p in r.split())
    return cobertas / len(palavras) >= 0.6

def validar_questao(q) -> bool:
    """Protege a interface contra saídas malformadas do modelo."""
    try:
        if q["tipo"] not in TIPOS or not str(q["enunciado"]).strip():
            return False
        if q["tipo"] == "multipla_escolha":
            alts = q["alternativas"]
            return len(alts) >= 2 and isinstance(q["resposta_correta"], int) \
                and 0 <= q["resposta_correta"] < len(alts)
        if q["tipo"] == "verdadeiro_falso":
            return isinstance(q["resposta_correta"], bool)
        return bool(str(q["resposta_correta"]).strip())
    except (KeyError, TypeError):
        return False


def texto_gabarito(q) -> str:
    if q["tipo"] == "multipla_escolha":
        i = q["resposta_correta"]
        return f"{LETRAS[i]}) {q['alternativas'][i]}"
    if q["tipo"] == "verdadeiro_falso":
        return "Verdadeiro" if q["resposta_correta"] else "Falso"
    return str(q["resposta_correta"])




def corrigir(q, resposta) -> bool:
    if resposta is None or resposta == "":
        return False
    if q["tipo"] == "multipla_escolha":
        return resposta == q["resposta_correta"]
    if q["tipo"] == "verdadeiro_falso":
        return (resposta == "Verdadeiro") == q["resposta_correta"]
    return resposta_curta_correta(resposta, q["resposta_correta"])

