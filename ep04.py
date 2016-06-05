import numpy
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

def geraListaVivos(tab,n,m):
    listaVivos  =[]
    for i in range(m):

        for j in range(n):

            if tab[i][j] == 1:
                listaVivos.append((((m-1)-i),j))        #verifica se a celula esta viva e adiciona na lista

    return listaVivos

def leEntrada(nome):
    listaVivos = []
    modo = 0
    doc = open(nome,'r')
    for linha in doc:
        if linha == 'Q\n':
            modo = 0
        elif linha == 'H\n':
            modo = 1
        else:
            par = linha.split(',')                      #separa as coordenadas e converte em numeros
            listaVivos.append((int(par[0]),int(par[1])))
    return modo,listaVivos

def simulaQuad(n,m,lista,t):
    tab =  [[0 for k in range(n)] for l in range(m)]
    for x in range(len(lista)):
        clinha = (m-1) - lista[x][0]                    #inverte a coordenada para ser usada numa matriz comum
        ccoluna = lista[x][1]
        tab[clinha][ccoluna] = 1                        #preenche as casas vivas inicialmente

    for vezes in range(t):

        tab2 =  [[0 for c in range(n)] for d in range(m)]

        for i in range(m):

            for j in range(n):
                                                        #faz a soma dos vizinhos
                somViz = tab[(i-1)%m][(j-1)%n] + tab[(i-1)%m][j] + tab[(i-1)%m][(j+1)%n] + tab[i][(j-1)%n] + tab[i][(j+1)%n] + tab[(i+1)%m][(j-1)%n] + tab[(i+1)%m][j] + tab[(i+1)%m][(j+1)%n]

                if (somViz == 3):

                    tab2[i][j] = 1                      #aplica as regras de acordo com o numero de vizinhos

                elif tab[i][j] == 1 and somViz == 2 :

                    tab2[i][j] = 1

        tab = tab2
    #print(numpy.matrix(tab))
    return geraListaVivos(tab,n,m)
        
def desenhaQuad(n,m,lista,figura):
    codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY]

    fig = plt.figure()
    imagem = fig.add_subplot(111)

    for i in range(m):
        for j in range(n):
            cor = '#ffffff'
            if (i,j) in lista:
                cor = '#6600cc'
            verts = [(i,j),(i+1,j),(i+1,j+1),(i,j+1),(i,j)]
            path = Path(verts,codes)
            patch = patches.PathPatch(path, facecolor = cor, lw=1)
            imagem.add_patch(patch)

    plt.savefig(figura)
    imagem.set_xlim(0,m)
    imagem.set_ylim(0,n)
    plt.show()

def main():
    m = int(input('colunas: '))
    n = int(input('linhas: '))
    t = int(input('vezes: '))
    modo,listaVivos = leEntrada('teste.txt')
    if modo == 0:
        desenhaQuad(n,m,simulaQuad(n,m,listaVivos,t),'rola.png')


main()