import platform
import os
import shutil

diretorio = '.'

def ver():
    print(platform.system())
    print(platform.release())


def dir():
    print(os.listdir(diretorio))


def cat():
    arquivo = input()
    with open(arquivo) as arquivo :
        linha = arquivo.readlines()
        for linha in linha:
            print(linha)

def edit():
    arquivoEdit = input()
    arquivo = open(arquivoEdit, 'w')
    newArquivo = input()
    arquivo.write(newArquivo)

def mkdir():
    newDir = input()
    os.mkdir(newDir)

def cd():
    local = input()
    attCaminho(local)
    x = os.chdir(os.path.join(os.getcwd(),local))

def rm():
    x=input()
    remover = input()
    if x == '-a':
        os.remove(remover)
    else:
        os.rmdir(remover)
    
def mv():
    nomeAntigo = input()
    newNome = input()
    os.rename(nomeAntigo,newNome)

def cp():
    nomeArquivo = input()
    pasta = input()
    shutil.copy(nomeArquivo,pasta)

def at():
    print(os.getcwd())


def attCaminho(novoCaminho):
    global diretorio
    diretorio = novoCaminho

comando = ""
while comando != "exit":
    comando = input("/> ")
    if comando == "ver":
        ver()

    elif comando == "dir":
        dir()

    elif comando == "cat":
        cat()

    elif comando == "edit":
        edit()

    elif comando == "mkdir":
        mkdir()

    elif comando == "cd":
        cd()

    elif comando == "rm":
        rm()

    elif comando == "mv":
        mv()

    elif comando == "cp":
        cp()

    elif comando == "cd":
        cd()

    elif comando == "at":
        at()

    elif comando != "exit":
        print("Comando Invalido!")
