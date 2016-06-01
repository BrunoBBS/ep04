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
            par = linha.split(',')
            listaVivos.append((int(par[0]),int(par[1])))
    return modo,listaVivos

def simulaQuad(n,m,lista,t):
    tab =  [[0 for k in range(m)] for l in range(n)]
    tab2 =  [[0 for c in range(m)] for d in range(n)]
    for x in range(len(lista)):
        clinha = n - lista[x][0]
        ccoluna = lista[x][1]
        tab[clinha][ccoluna] = 1
    for vezes in range(t):
        for i in range(n):
            for j in range(m):

                somViz = tab[i-1][j-1] + tab[i-1][j] + tab[i-1][j+1] + tab[i][j-1] + tab[i][j+1] + tab[i+1][j-1] + tab[i+1][j+1]

                if (somViz == 3):

                    tab2[i][j] = 1

                elif tab[i][j] == 1 and somViz == 2 :

                    tab2[i][j] = 1

    for row in tab2:
    for val in row:
        print '{:4}'.format(val),
    print
        

