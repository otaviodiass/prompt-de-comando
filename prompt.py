import platform
import os
import shutil

diretorio = ''

def ver():
    print(platform.system()) #retorna o nome do sistema operacional
    print(platform.release()) #retorna a versao do sistema operacional


def dir():
    print(os.listdir(diretorio)) #lista todos os arquivos e diretorios no caminho atual


def cat(arquivo):
    with open(arquivo) as arquivo :
        linha = arquivo.readlines()
        for linha in linha:
            print(linha) #abre o arquivo especificado e print na tela

def edit(arquivoEdit):
    arquivo = open(arquivoEdit, 'w')
    newArquivo = input()
    arquivo.write(newArquivo) #abre o arquivo especificado e permite a edicao do mesmo

def mkdir(newDir):
    os.mkdir(newDir) #cria um novo diretorio

def cd(local):
    attCaminho(local)
    addBarra()
    os.chdir(local) #altera o diretorio de trabalho atual

def rm(opcao, remove):
    if opcao == '-a':
        try:
          os.remove(remove) #remove o arquivo
        except IOError:
          print("nao foi possivel remover o arquivo")
    else:
        try:
          os.rmdir(remove) #remove o diretorio 
        except IOError:
          print("nao foi possivel remover o pasta")
    
def mv(nome_antigo, nome_novo):
    os.rename(nome_antigo, nome_novo) #renomeia 

def cp(nome_arquivo, pasta):
    shutil.copy(nome_arquivo,pasta) #faz a copia do arquivo para o diretorio


def at():
    print(os.getcwd()) #localizacao do diretorio de trabalho atual

def attCaminho(novoCaminho):
    global diretorio
    diretorio += novoCaminho #atualiza o caminho da variavel diretorio para o mais recente

def addBarra():
  global diretorio
  diretorio += '\\' #adiciona \\ no caminho para permitir a navegacao entre as pastas

comando = ""
while comando != "exit":
    comando = input(diretorio + "> ")
    if comando == "ver":
        ver()

    elif comando == "dir":
        dir()

    elif comando.split(' ')[0] == "cat":
        cat(comando.split(' ')[1])

    elif comando.split(' ')[0] == "edit":
        edit(comando.split(' ')[1])

    elif comando.split(' ')[0] == "mkdir":
        mkdir(comando.split(' ')[1])

    elif comando.split(' ')[0] == "cd":
        cd(comando.split(' ')[1::])

    elif comando.split(' ')[0] == "rm":
        rm(comando.split(' ')[1], comando.split(' ')[2])

    elif comando.split(' ')[0] == "mv":
        mv(comando.split(' ')[1], comando.split(' ')[2])

    elif comando.split(' ')[0] == "cp":
        cp(comando.split(' ')[1], comando.split(' ')[2])

    elif comando == "cd":
        cd()

    elif comando == "at":
        at()

    elif comando != "exit":
        print("Comando Invalido!")