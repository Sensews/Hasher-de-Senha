# -------------------------------- IMPORTS
import os
import hashlib
import re

# -------------------------------- FUNÇÃO DE LIMPEZA
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# -------------------------------- FUNÇÃO QUE CONVERTE A SENHA PRA HASH
def salvar_arquivo(nome_arquivo, nome_usuario, senha):
    with open(nome_arquivo, 'a+') as arquivo:
        hash_senha = hashlib.md5(senha.encode()).hexdigest()
        arquivo.write(f"{nome_usuario},{hash_senha}\n")

# -------------------------------- FUNÇÃO QUE "LÊ" O ARQUIVO
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

        usuarios = []
        for linha in linhas:
            usuario, senha = linha.strip().split(",")
            usuarios.append((usuario, senha))

    return usuarios

ARQUIVO = 'Hasher de Senha/usuarios.txt'

def cadastrar_usuario():
    limpar_tela()
    nome_usuario = input("Digite seu usuário: ")
    senha_usuario = input("Digite sua senha (mínimo 8 caracteres, com pelo menos uma letra maiúscula, um caractere especial e um número): ")

# -------------------------------- VERIFICA SENHA
    if (len(senha_usuario) < 8 or
            not re.search(r"[A-Z]", senha_usuario) or
            not re.search(r"[0-9]", senha_usuario) or
            not re.search(r"[!@#$%^&*()\-_=+{};:,<.>]", senha_usuario)):
        print("A senha deve ter no mínimo 8 caracteres, incluindo pelo menos uma letra maiúscula, um número e um caractere especial.")
        return

# -------------------------------- VERIFICA SE JÁ ESTÁ CADASTRADO
    for usuario in usuarios:
        nome = usuario[0]
        if nome == nome_usuario:
            print("Usuário já cadastrado!")
            return

    salvar_arquivo(ARQUIVO, nome_usuario, senha_usuario)
    print("Usuário cadastrado com sucesso!")
    input("Pressione Enter para continuar...")
    limpar_tela()

def autenticar_usuario():
    limpar_tela()
    nome_usuario = input("Digite seu usuário: ")
    senha_usuario = input("Digite sua senha: ")

# -------------------------------- PESQUISA O USER E A AUTENTICAÇÃO
    for usuario in usuarios:
        nome = usuario[0]
        senha = usuario[1]
        if nome == nome_usuario:
            if senha == hashlib.md5(senha_usuario.encode()).hexdigest():
                print("Seja bem-vindo!")
                input("Pressione Enter para continuar...")
                limpar_tela()
                return
            else:
                print("Usuário ou senha incorreto!")
                input("Pressione Enter para continuar...")
                limpar_tela()
                return
    print("Usuário não encontrado!")
    input("Pressione Enter para continuar...")
    limpar_tela()

# -------------------------------- IDENTIFICAÇÃO DO USER
usuarios = ler_arquivo(ARQUIVO)

# -------------------------------- MENU MANEIRO
while True:
    print("\nMenu:")
    print("1. Cadastrar usuário")
    print("2. Autenticar usuário")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_usuario()
    elif opcao == '2':
        autenticar_usuario()
    elif opcao == '3':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Escolha novamente.")
        input("Pressione Enter para continuar...")
        limpar_tela()
