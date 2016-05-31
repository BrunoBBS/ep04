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
    for x in range(len(lista)):
        clinha = n - lista[x][0]
        ccoluna = lista[x][1]
        tab[clinha][ccoluna] = 1
        
    i=1

