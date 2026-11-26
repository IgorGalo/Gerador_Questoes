"""Gerador de mentira, só para desenvolver a interface sem o modelo (Parte 1 substitui por gerador.py)."""
import re
import random


def gerar_questoes(texto: str, quantidade: int, tipos: list) -> list:
    frases = [f.strip() for f in re.split(r"(?<=[.!?])\s+", texto) if len(f.strip()) > 40]
    if not frases:
        frases = [texto[:200]]
    questoes = []
    for i in range(quantidade):
        tipo = tipos[i % len(tipos)]
        f = frases[i % len(frases)]
        if tipo == "multipla_escolha":
            outras = [x for x in frases if x != f][:3]
            alts = (outras + ["Nenhuma das anteriores", "Não consta no texto", "Todas as anteriores"])[:3] + [f]
            random.shuffle(alts)
            questoes.append({"tipo": tipo, "enunciado": "Qual das afirmações aparece no texto?",
                             "alternativas": alts, "resposta_correta": alts.index(f),
                             "explicacao": "Trecho presente no texto fornecido."})
        elif tipo == "verdadeiro_falso":
            questoes.append({"tipo": tipo, "enunciado": f"Verdadeiro ou falso: {f}",
                             "resposta_correta": True, "explicacao": "A afirmação foi extraída do texto."})
        else:
            palavra = max(f.split(), key=len).strip(".,;:")
            questoes.append({"tipo": tipo, "enunciado": f"Complete com uma palavra-chave: {f.replace(palavra, '_____', 1)}",
                             "resposta_correta": palavra, "explicacao": "Palavra removida da frase original."})
    return questoes
