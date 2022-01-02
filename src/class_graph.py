class Graph:
    def __init__(self, number_vertices=0, number_arcs=0, array_transitions=[]):
        self.number_vertices = number_vertices
        self.number_arcs = number_arcs
        self.array_transitions = array_transitions


def get_suiv(array_trans, vertice):
    """
    Recuperation des sommets suivants avec le poids de l'arrete sous forme de dictionnaire
    exemple : {<sommet_suivant>: <poids de l'arrete>
    """

    pred = {}
    for trans in array_trans:  # Parcours du tableau des transitions pour recuperer les suivants
        if trans[0] == vertice:
            pred[trans[1]] = trans[2]

    return pred


def get_matrice_adjacence(graph):
    matrice_adj = []
    sommets = graph.number_vertices

    for i in range(0, sommets + 1):
        matrice_sous_adj = []
        for j in range(0, sommets + 1):
            if i == 0:
                if j == 0:
                    matrice_sous_adj.append(' ')
                if j > 0:
                    matrice_sous_adj.append(j - 1)
            if j == 0 and i != 0:
                matrice_sous_adj.append(i - 1)
            if i != 0 and j != 0:
                matrice_sous_adj.append(0)
        matrice_adj.append(matrice_sous_adj)

    for k in range(len(graph.array_transitions)):
        matrice_adj[graph.array_transitions[k][0] + 1][graph.array_transitions[k][1] + 1] = 1

    return matrice_adj

