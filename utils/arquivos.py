def ler_arquivo(arquivo) -> str:
    dados = arquivo.getvalue()
    for enc in ("utf-8", "latin-1"):
        try:
            return dados.decode(enc)
        except UnicodeDecodeError:
            continue
    return ""
