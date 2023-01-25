import platform
import os
import shutil

diretorio = ''

def ver():
    print(platform.system()) #retorna o nome do sistema operacional
    print(platform.release()) #retorna a versao do sistema operacional


def dir():
    print(os.listdir(diretorio)) #lista todos os arquivos e diretorios no caminho atual


def cat():
    arquivo = input()
    with open(arquivo) as arquivo :
        linha = arquivo.readlines()
        for linha in linha:
            print(linha) #abre o arquivo especificado e print na tela

def edit():
    arquivoEdit = input()
    arquivo = open(arquivoEdit, 'w')
    newArquivo = input()
    arquivo.write(newArquivo) #abre o arquivo especificado e permite a edicao do mesmo

def mkdir():
    newDir = input()
    os.mkdir(newDir) #cria um novo diretorio

def cd():
    local = input()
    attCaminho(local)
    addBarra()
    os.chdir(local) #altera o diretorio de trabalho atual

def rm():
    x=input()
    remover = input()
    if x == '-a':
        try:
          os.remove(remover) #remove o arquivo
        except IOError:
          print("nao foi possivel remover o arquivo")
    else:
        try:
          os.rmdir(remover) #remove o diretorio 
        except IOError:
          print("nao foi possivel remover o pasta")
    
def mv():
    nomeAntigo = input()
    newNome = input()
    os.rename(nomeAntigo,newNome) #renomeia 

def cp():
    nomeArquivo = input()
    pasta = input()
    shutil.copy(nomeArquivo,pasta) #faz a copia do arquivo para o diretorio


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