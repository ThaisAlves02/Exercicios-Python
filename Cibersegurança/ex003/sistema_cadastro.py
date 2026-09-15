# Sistema de cadastro e login com senha criptografada(hash)

import json
import hashlib
from pathlib import Path


ARQUIVO_USUARIOS = Path("usuarios.json")

#-----------------------------------------------------------------
# LEITURA DO ARQUIVO USUÁRIO
#-----------------------------------------------------------------
if ARQUIVO_USUARIOS.exists():
    try:
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as arquivo:
            lista_usuarios = json.load(arquivo)
            print("Conteúdo lido com sucesso:", lista_usuarios)

    except FileNotFoundError:
        print("O arquivo de usuários ainda não existe.")
        lista_usuarios = {} # Evita erros nas próximas linhas do código

    except json.JSONDecodeError:
        print("O arquivo existe, mas está vazio. Iniciando sistema com dados vazios.")
        lista_usuarios = {} # Cria um dicionário vazio na memória para o programa não quebrar

else:
    lista_usuarios = {}


# funcoes
def cadastrar_usuario():
    nome_usuario = input("Usuário: ")
    senha = input("Senha: ")

    # Convertendo a senha para bytes. 
    senha_bytes = senha.encode("utf-8")
    # Criando um hash para a minha senha, que será criptografada com SHA256
    senha_hash = hashlib.sha256(senha_bytes).hexdigest()

    lista_usuarios[nome_usuario] = {
        "senha": senha_hash
    }

    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as arquivo:
        json.dump(lista_usuarios, arquivo, indent=4)
        print(f"Usuário '{nome_usuario}' cadastrado com sucesso!")

def fazer_login():
    nome_usuario = input("Usuário: ")
    senha = input("Senha: ")
  
    senha_bytes = senha.encode("utf-8")
    senha_hash = hashlib.sha256(senha_bytes).hexdigest()

    if nome_usuario in lista_usuarios and lista_usuarios[nome_usuario]["senha"] == senha_hash:
        print(f"Login bem sucedido! Usuário conectado: {nome_usuario}")
    else:
        print("Usuário não cadastrado ou senha incorreta.")

  
print("""
========== MENU ===========
1. Cadastrar novo usuário
2. Fazer login
""")

op = input("Digite o número da opção desejada: ")

if op == "1":
    cadastrar_usuario()
  
elif op == "2":
    fazer_login()
