import numpy

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
    M = []                     
    for i in range(n+2):       
        M.append([])           
        for j in range(m+2):
            M[i].append(0)  


    for x in range(len(lista)):
        clinha = (n-1) - lista[x][0] + 1
        ccoluna = lista[x][1] + 1
        tab[clinha][ccoluna] = 1
    
    for k in range(t):
        Mp = []
        for i in range(n+2):
            Mp.append([])
            for j in range(m+2):
                Mp[i].append(0)

        M[0][0] =  M[n][m]
        M[n+1][0] =  M[1][m]
        M[0][m+1] =  M[n][1]
        M[n+1][m+1] = M[1][1]
        
        for i in range(1, n+1, 1): 
            M[i][0] = M[i][m]
            M[i][m+1] = M[i][1]

        for i in range(1, m+1, 1): 
            M[0][i] = M[n][i]
            M[n+1][i] = M[1][i]


    
    for vezes in range(t):
        tab2 =  [[0 for c in range(m)] for d in range(n)]
        for i in range(n):
            for j in range(m):

                tab[i-1][j-1] + tab[i-1][j] + tab[i-1][((j+1)%(m-1))-1] + tab[i][j-1] + tab[i][((j+1)%(m-1))-1] + tab[((i+1)%(n-1))-1][j-1] + tab[((i+1)%(n-1))-1][j] +tab[((i+1)%(n-1))-1][((j+1)%(m-1))-1]
                print(tab[i-1][j-1])
                print(tab[i-1][j])
                print(tab[i-1][((j+1)%(m-1))-1])
                print(tab[i][j-1])
                print(tab[i][((j+1)%(m-1))-1])
                print(tab[((i+1)%(n-1))-1][j-1])
                print(tab[((i+1)%(n-1))-1][j])
                print(tab[((i+1)%(n-1))-1][((j+1)%(m-1))-1])
                print('=========================\n')
                if (somViz == 3):

                    tab2[i][j] = 1

                elif tab[i][j] == 1 and somViz == 2 :

                    tab2[i][j] = 1

        tab = tab2
    print(numpy.matrix(tab))
        
def main():
    m = int(input('colunas: '))
    n = int(input('linhas: '))
    t = int(input('vezes: '))
    modo,listaVivos = leEntrada('teste.txt')
    if modo == 0:
        simulaQuad(n,m,listaVivos,t)

main()