import json
import os


def verificar_ou_criar_json(caminho, estrutura_inicial):
    """Verifica se o arquivo existe; se não existir, cria com a estrutura inicial."""
    if not os.path.exists(caminho):
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(
                arquivo,
                indent=4,
                ensure_ascii=False
            )

#---------------------------------------------
# CARREGAR JSON (retorna tuplas)
#---------------------------------------------

def carregar_json(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        return dados

#---------------------------------------------
# SALVAR JSON (salva listas)
#---------------------------------------------

def salvar_json(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(
            arquivo,
            indent=4,
            ensure_ascii=False
        )
