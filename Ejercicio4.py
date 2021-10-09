#TopoSort
def topoSort(G):
  n = len(G)
  visited = [False]*n
  ts = []

  def dfs(u):
    if not visited[u]:
      visited[u] = True
      for v in G[u]:
        if not visited[v]:
          dfs(v)
      ts.append(u)

  for u in range(n):
    dfs(u)

  return ts

#Kosaraju

def reverse(G):
  n = len(G)
  Grev = [[] for _ in range(n)]
  for u in range(n):
    for v in G[u]:
      Grev[v].append(u)
  return Grev

def kosaraju(G):
  n = len(G)
  visited = [False]*n
  f = []

  Grev = reverse(G)

  def dfs1(u):
    visited[u] = True
    for v in Grev[u]:
      if not visited[v]:
        dfs1(v)
    f.append(u)

  def dfs2(u, cc):
    visited[u] = True
    for v in G[u]:
      if not visited[v]:
        dfs2(v, cc)
    cc.append(u)

  for u in range(n):
    if not visited[u]:
      dfs1(u)

  scc = []
  visited = [False]*n
  for u in reversed(f):
    if not visited[u]:
      cc = []
      dfs2(u, cc)
      scc.append(cc)

  return scc

#Se eligió este grafo, porque tiene 3 ciclos dentro de él
#Como el toposort, para llegar a cada grafo, tienes que cumplir con sus requerimientos
#Pero como es un ciclo, no se puede cumplir con los requerimientos y, por ello,
#es imposible que se pueda hallar un orden

G = [[], [4], [8], [6], [7], [2], [9], [1], [5, 6], [3, 7]]

print(topoSort(G)) #Aunque llegue a votar resultado, la respuesta está mal, pues no existe un orden topologico, pues es un ciclo
print(kosaraju(G))

#Primera respuesta [0, 7, 4, 1, 5, 3, 9, 6, 8, 2] #Aquí vota resultado, pues entra si el nodo no está visitado, pero está mal
#Segunda respuesta [[7, 4, 1], [6, 3, 9], [2, 5, 8], [0]] #Este sí puede detectar ciclos, pues son conexos
