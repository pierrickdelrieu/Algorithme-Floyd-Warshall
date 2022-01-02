from read_files import *
from class_graph import *


def get_init_sommet(array_trans):
    vertices = []
    for trans in array_trans:
        vertices.append(trans[0])

    return min(vertices, default=None)


def bellman(Graph, init_sommet):
    global prec
    distances = {}
    predecesseurs = {}

    # Initialisation
    for vertice in range(0, Graph.number_vertices):
        distances[vertice] = float("inf")
        predecesseurs[vertice] = None
    distances[init_sommet] = 0
    temp = [init_sommet]
    print(distances)

    # Algorithme
    # for i in range(1, Graph.number_vertices):
    #     for j in range(Graph.number_vertices):
    #         suiv = get_suiv(Graph.array_transitions, j)
    #         for k in suiv:
    #             if distances[k] > distances[j] + suiv[k]:
    #                 distances[k] = distances[j] + suiv[k]
    #                 predecesseurs[k] = j
    #     print(distances)

    distances_prec = distances.copy()
    stop = True

    k = 1
    while stop:
        prec = temp
        temp = []
        for i in prec:
            suiv = get_suiv(Graph.array_transitions, i)
            for j in suiv:
                if (distances[i] + suiv[j]) <= distances_prec[j]:
                    distances_prec[j] = distances[i] + suiv[j]
                    predecesseurs[j] = i
                    temp.append(j)

        k = k + 1
        if k >= Graph.number_vertices or distances == distances_prec:
            stop = False
        distances = distances_prec.copy()
        print(k-1, distances)

    # Detection de circuit absorbant
    for i in prec:
        suiv = get_suiv(Graph.array_transitions, i)
        for j in suiv:
            if (distances[i] + suiv[j]) <= distances_prec[j]:
                return None, None

    return distances, predecesseurs


def display_solution_bellman(distances, Graph):
    print("Plus courte distance pour chaque sommet a partir du sommet initiale", get_init_sommet(Graph.array_transitions), ":")
    for v in distances:
        print(str(v) + ' => ' + str(distances[v]))
