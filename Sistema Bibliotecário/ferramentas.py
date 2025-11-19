import json
import os

def verificar_ou_criar_json(caminho, estrutura_inicial):
    if not os.path.exists(caminho):
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(estrutura_inicial, arquivo, indent=4, ensure_ascii=False)

def carregar_json(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_json(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
