#.n Bruno Boaventura Scholl
#.u 9793586


import numpy
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

def geraListaVivos(tab,n,m):
    listaVivos  =[]
    for i in range(m):

        for j in range(n):

            #verifica se a celula esta viva e adiciona na lista
            if tab[i][j] == 1:
                listaVivos.append((((m-1)-i),j))

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

            #separa as coordenadas e converte em numeros
            par = linha.split(',')
            listaVivos.append((int(par[1]),int(par[0])))
    doc.close()
    return modo,listaVivos

def simulaQuad(n,m,lista,t):
    tab =  [[0 for k in range(n)] for l in range(m)]
    for x in range(len(lista)):

        #inverte a coordenada para ser usada numa matriz comum
        clinha = (m-1) - lista[x][0]
        ccoluna = lista[x][1]

         #preenche as casas vivas inicialmente
        tab[clinha][ccoluna] = 1

    for vezes in range(t):
        desenhaQuad(n,m,geraListaVivos(tab,n,m), str(vezes) + ".png")

        tab2 =  [[0 for c in range(n)] for d in range(m)]

        for i in range(m):

            for j in range(n):
                #faz a soma dos vizinhos      
                somViz = tab[(i-1)%m][(j-1)%n] + tab[(i-1)%m][j] + tab[(i-1)%m][(j+1)%n] + tab[i][(j-1)%n] + tab[i][(j+1)%n] + tab[(i+1)%m][(j-1)%n] + tab[(i+1)%m][j] + tab[(i+1)%m][(j+1)%n]

                #aplica as regras de acordo com o numero de vizinhos
                if somViz == 3:

                    tab2[i][j] = 1

                elif tab[i][j] == 1 and somViz == 2 :

                    tab2[i][j] = 1

        tab = tab2
    return geraListaVivos(tab,n,m)

def simulaHex(n,m,lista,t):
    tab =  [[0 for k in range(n)] for l in range(m+1)]
    for x in range(len(lista)):

        #inverte a coordenada para ser usada numa matriz comum
        clinha = (m-1) - lista[x][0]
        ccoluna = lista[x][1]

        #preenche as casas vivas inicialmente
        tab[clinha][ccoluna] = 1

    for vezes in range(t):

        tab2 =  [[0 for c in range(n)] for d in range(m+1)]

        for i in range(m+1):

            for j in range(n):

                #faz a soma de vizinhos de acordo com a coluna se ela eh par ou impar
                if i%2 == 0:
                    somViz = tab[(i-1)%m][(j+1)%n] + tab[(i-1)%m][j] + tab[(i+1)%m][(j+1)%n] + tab[i][(j-1)%n] + tab[i][(j+1)%n] + tab[(i+1)%m][j]
                else:
                    somViz =  tab[(i-1)%m][j] + tab[i][(j-1)%n] + tab[i][(j+1)%n] + tab[(i+1)%m][(j-1)%n] + tab[(i+1)%m][j] + tab[(i-1)%m][(j-1)%n]

                #aplica as regras de acordo com o numero de vizinhos

                if (i,j) == (4,2):
                    print (somViz)

                if somViz == 3 or somViz == 5:

                    tab2[i][j] = 1 

                elif tab[i][j] == 1 and somViz == 2 :

                    tab2[i][j] = 1

        tab = tab2
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
            #calcula a coordenada dos vertices considerando um quadrado de 1x1
            verts = [(i,j),(i+1,j),(i+1,j+1),(i,j+1),(i,j)]
            path = Path(verts,codes)
            patch = patches.PathPatch(path, facecolor = cor, lw=1)
            imagem.add_patch(patch)

    imagem.set_xlim(0,m)
    imagem.set_ylim(0,n)
    plt.savefig(figura)
    plt.close()
    #plt.show()

def desenhaHex(n,m,lista,figura):
    codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY]

    fig = plt.figure()
    imagem = fig.add_subplot(111)
    
    #calcula as coordenadas dos vertices considerando o raio do circulo circunscrito no hexagono como 0.5
    for p in range(m):
        i = p - (p*0.25)
        for j in range(n):
            if (p,j) in lista:
                cor = '#6600cc'
            else:
                cor = '#ffffff'
            if p%2 != 0:
                j = j - 0.5
             
            verts = [(i+1,j+0.5),(i+0.75,j+1),(i+0.25,j+1),(i,j+0.5),(i+0.25,j),(i+0.75,j),(i,j)]
            path = Path(verts,codes)
            patch = patches.PathPatch(path, facecolor = cor, lw=1)
            imagem.add_patch(patch)

    imagem.set_xlim(-1,m)
    imagem.set_ylim(-1,n+1)
    plt.savefig(figura)
    plt.show()

def main():
    m = int(input('colunas: '))
    n = int(input('linhas: '))
    t = int(input('vezes: '))
    modo,listaVivos = leEntrada('teste.txt')
    if modo == 0:
        desenhaQuad(n,m,simulaQuad(n,m,listaVivos,t),'t.png')
    elif modo == 1:
        desenhaHex(n,m,simulaHex(n,m,listaVivos,t),'t.png')


main()