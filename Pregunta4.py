{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Pregunta4.py",
      "provenance": [],
      "authorship_tag": "ABX9TyMYmq9g6qunlCLg+Wlje0dr",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ronaldo91929-glic/Practicas-Comple/blob/main/Pregunta4.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Xnnpm7N2QzD4",
        "outputId": "421c9b6d-ac82-4471-e038-58e576433f8d"
      },
      "source": [
        "#TopoSort\n",
        "def topoSort(G):\n",
        "  n = len(G)\n",
        "  visited = [False]*n\n",
        "  ts = []\n",
        "\n",
        "  def dfs(u):\n",
        "    if not visited[u]:\n",
        "      visited[u] = True\n",
        "      for v in G[u]:\n",
        "        if not visited[v]:\n",
        "          dfs(v)\n",
        "      ts.append(u)\n",
        "\n",
        "  for u in range(n):\n",
        "    dfs(u)\n",
        "\n",
        "  return ts\n",
        "\n",
        "#Kosaraju\n",
        "\n",
        "def reverse(G):\n",
        "  n = len(G)\n",
        "  Grev = [[] for _ in range(n)]\n",
        "  for u in range(n):\n",
        "    for v in G[u]:\n",
        "      Grev[v].append(u)\n",
        "  return Grev\n",
        "\n",
        "def kosaraju(G):\n",
        "  n = len(G)\n",
        "  visited = [False]*n\n",
        "  f = []\n",
        "\n",
        "  Grev = reverse(G)\n",
        "\n",
        "  def dfs1(u):\n",
        "    visited[u] = True\n",
        "    for v in Grev[u]:\n",
        "      if not visited[v]:\n",
        "        dfs1(v)\n",
        "    f.append(u)\n",
        "\n",
        "  def dfs2(u, cc):\n",
        "    visited[u] = True\n",
        "    for v in G[u]:\n",
        "      if not visited[v]:\n",
        "        dfs2(v, cc)\n",
        "    cc.append(u)\n",
        "\n",
        "  for u in range(n):\n",
        "    if not visited[u]:\n",
        "      dfs1(u)\n",
        "\n",
        "  scc = []\n",
        "  visited = [False]*n\n",
        "  for u in reversed(f):\n",
        "    if not visited[u]:\n",
        "      cc = []\n",
        "      dfs2(u, cc)\n",
        "      scc.append(cc)\n",
        "\n",
        "  return scc\n",
        "\n",
        "#Se eligió este grafo, porque tiene 3 ciclos dentro de él\n",
        "#Como el toposort, para llegar a cada grafo, tienes que cumplir con sus requerimientos\n",
        "#Pero como es un ciclo, no se puede cumplir con los requerimientos y, por ello,\n",
        "#es imposible que se pueda hallar un orden\n",
        "\n",
        "G = [[], [4], [8], [6], [7], [2], [9], [1], [5, 6], [3, 7]]\n",
        "\n",
        "print(topoSort(G)) #Aunque llegue a votar resultado, la respuesta está mal, pues no existe un orden topologico, pues es un ciclo\n",
        "print(kosaraju(G))\n",
        "\n",
        "#Primera respuesta [0, 7, 4, 1, 5, 3, 9, 6, 8, 2] #Aquí vota resultado, pues entra si el nodo no está visitado, pero está mal\n",
        "#Segunda respuesta [[7, 4, 1], [6, 3, 9], [2, 5, 8], [0]] #Este sí puede detectar ciclos, pues son conexos"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0, 7, 4, 1, 5, 3, 9, 6, 8, 2]\n",
            "[[7, 4, 1], [6, 3, 9], [2, 5, 8], [0]]\n"
          ]
        }
      ]
    }
  ]
}