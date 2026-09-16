#-----------------------------------------------------------------
# SISTEMA DE CADASTRO E LOGIN COM SENHA CRIPTOGRAFADA (HASH)
#-----------------------------------------------------------------

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

#-----------------------------------------------------------------
# FUNÇÕES
#-----------------------------------------------------------------
def cadastrar_usuario():
    nome_usuario = input("Usuário: ")
    senha = input("Senha: ")
    
    # Convertendo a senha para bytes. 
    senha_bytes = senha.encode("utf-8")
    # Criando um hash para a minha senha, que será criptografada com SHA256
    senha_hash = hashlib.sha256(senha_bytes).hexdigest()

    lista_usuarios[nome_usuario] = {
        "senha": senha_hash,
        "tentativas": 0
    }

    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as arquivo:
        json.dump(lista_usuarios, arquivo, indent=4)
        print(f"Usuário '{nome_usuario}' cadastrado com sucesso!")

def fazer_login():
    usuario_inexistente = 0

    while True:
            nome_usuario = input("Usuário: ")
            senha = input("Senha: ")

            if nome_usuario in lista_usuarios:
                # 1. Pega os dados e as tentativas do usuário
                dados_usuario = lista_usuarios.get(nome_usuario, {})
                tentativas = dados_usuario.get("tentativas", 0)

                if tentativas >= 3:
                    print("Você errou 3 vezes, acesso bloqueado!")
                    break
                                
                senha_bytes = senha.encode("utf-8")
                senha_hash = hashlib.sha256(senha_bytes).hexdigest()
                                    
                if dados_usuario["senha"] == senha_hash:
                     print(f"Login bem sucedido! Usuário conectado: {nome_usuario}")

                     dados_usuario["tentativas"] = 0
                     with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as arquivo:
                        json.dump(lista_usuarios, arquivo, indent=4)
                     break
                else:
                     print(f"Usuário não cadastrado ou incorreto!")
                     tentativas += 1
                                
                     dados_usuario["tentativas"] = tentativas
                     with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as arquivo:
                       json.dump(lista_usuarios, arquivo, indent=4)    
            else:
                print("Usuário não cadastrado ou incorreto!") 
                usuario_inexistente += 1

                if usuario_inexistente >= 3:
                    break
#-----------------------------------------------------------------
# MENU INTERATIVO
#-----------------------------------------------------------------
while True:
    print("""
    ========== MENU ===========
    1. Cadastrar novo usuário
    2. Fazer login
    0. Sair
    """)

    op = input("Digite o número da opção desejada: ")

    if op == "1":
        cadastrar_usuario()
    
    elif op == "2":
        fazer_login()

    elif op == "0":
        break