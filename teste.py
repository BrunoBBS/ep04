import numpy
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY]
m = 10
n = 10
lista = [(1,2),
(0,2),
(1,1),
(1,3),
(2,1),
(2,2),
(2,3)]
fig = plt.figure()
imagem = fig.add_subplot(111)

for p in range(m):
    i = p - (p*0.25)
    for j in range(n):
        cor = '#ffffff'
        print ((p,j))
        if (p,j) in lista:
            cor = '#6600cc'
        if p%2 != 0:
            j = j - 0.5
             
        verts = [(i+1,j+0.5),(i+0.75,j+1),(i+0.25,j+1),(i,j+0.5),(i+0.25,j),(i+0.75,j),(i,j)]
        path = Path(verts,codes)
        patch = patches.PathPatch(path, facecolor = cor, lw=1)
        imagem.add_patch(patch)

imagem.set_xlim(-1,m)
imagem.set_ylim(-1,n+1)
plt.savefig('nego.png')
plt.show()