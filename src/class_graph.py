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
