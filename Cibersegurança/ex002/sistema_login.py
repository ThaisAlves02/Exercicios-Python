import json

#-----------------------------------------------------------------
#LEITURA DO ARQUIVO USUÁRIO
#-----------------------------------------------------------------
try:
    with open("usuarios.json", "r", encoding="utf-8") as arquivo:
        usuarios = json.load(arquivo)
        print("Conteúdo lido com sucesso:", usuarios)

except FileNotFoundError:
    print("O arquivo de usuários ainda não existe.")
    usuarios = {} # Evita erros nas próximas linhas do código

except json.JSONDecodeError:
    print("O arquivo existe, mas está vazio. Iniciando sistema com dados vazios.")
    usuarios = {} # Cria um dicionário vazio na memória para o programa não quebrar


senha_cadastrada = usuarios.get("senha", "admin123") # admin123 é uma senha padrão, caso não achar nada.
tentativas = usuarios.get("tentativas", 0)

#-----------------------------------------------------------------
#ESCRITA DO ARQUIVO TENTATIVAS
#-----------------------------------------------------------------

if tentativas >= 3:
    print("Você errou a senha 3 vezes, acesso bloqueado!")
          
else:
    while True:
       if tentativas >= 3:
            print("Você errou a senha 3 vezes, acesso bloqueado!")
            break
       else:
            senha_digitada = input("Digite a sua senha:")

            if not senha_digitada == senha_cadastrada:
                print("Senha incorreta!")
                tentativas += 1

                usuarios["tentativas"] = tentativas
                with open("usuarios.json", "w", encoding="utf-8") as arquivo:
                    json.dump(usuarios, arquivo, indent=4)

            if senha_digitada == senha_cadastrada:
                print("Login bem sucedido!")

                usuarios["tentativas"] = 0
                with open("usuarios.json", "w", encoding="utf-8") as arquivo:
                    json.dump(usuarios, arquivo, indent=4)
                break
