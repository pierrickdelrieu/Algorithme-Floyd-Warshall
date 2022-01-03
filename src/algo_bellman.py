from read_files import *
from class_graph import *


def get_init_sommet(array_trans):
    """
    Renvoie le sommet de base avec lequel nous allons commence l'algorithme de bellman
    Ce sommet correspond au sommet d'indice le plus petit
    """
    vertices = []  # liste de tous les sommets

    for trans in array_trans:  # parcours du tableau des transitions
        vertices.append(trans[0])

    # retour du sommet d'indice le plus petit parmis tous les autres sommets (0 en cas d'erreur)
    return min(vertices, default=None)


def bellman(Graph, init_sommet):
    """
    Algorithme de calcul des plus courts chemin a partir du sommet init_sommet
    """
    interm_result = []
    distances = {}  # tableau des distances
    predecesseurs = {}  # tableau des predecesseurs associes a chaque distances

    # Initialisation des deux tableaux
    for vertice in range(0, Graph.number_vertices):
        distances[vertice] = float("inf")  # valeur infini pour toutes les distances
        predecesseurs[vertice] = vertice  # Initialisation de aucun predecesseur
    distances[init_sommet] = 0  # la distance du sommet initial vers lui meme est 0

    interm_result.append("0 | distance : " + str(distances) + '\n' + "0 | predecesseur : " + str(predecesseurs) + "\n")

    # Algorithme sous forme de pseudo code
    # for i in range(1, Graph.number_vertices):
    #     for j in range(Graph.number_vertices):
    #         suiv = get_suiv(Graph.array_transitions, j)
    #         for k in suiv:
    #             if distances[k] > distances[j] + suiv[k]:
    #                 distances[k] = distances[j] + suiv[k]
    #                 predecesseurs[k] = j
    #     print(distances)

    temp = [init_sommet]  # ce tableau correspond au sommet dont les distances changent a l'iteration actuelle
    distances_prec = distances.copy()
    stop = True

    k = 1  # initialisation du compteur d'iteration
    while stop:
        prec = temp  # ce tableau correspond au sommet dont les distances ont change a l'iteration precedente
        temp = []
        for i in prec:  # pour chaque sommet dont la distance a change, on reverifie les chemins vers leurs suivants
            suiv = get_suiv(Graph.array_transitions, i)
            for j in suiv:
                # si le chemin avec le suivant est plus petit que le chemin deja present
                if (distances[i] + suiv[j]) <= distances_prec[j]:
                    distances_prec[j] = distances[i] + suiv[j]  # on modifie la valeur de la distance
                    predecesseurs[j] = i  # on modifie aussi la valeur du predecesseur associe a la distance
                    temp.append(j)  # on ajoute le sommet comme un sommet dont la distance a change a cette iteration

        k = k + 1  # incrementation de l'iteration

        # verification de la condition d'arret de l'algorithme
        if k >= Graph.number_vertices or distances == distances_prec:
            stop = False

        distances = distances_prec.copy()

        interm_result.append(str(k-1) + " | distance : " + str(distances) + '\n' + str(k-1) + " | predecesseur : " + str(predecesseurs) + "\n")

    # Detection de circuit absorbant
    prec = temp
    for i in prec:
        suiv = get_suiv(Graph.array_transitions, i)
        for j in suiv:
            if (distances[i] + suiv[j]) <= distances_prec[j]:
                return None, None, interm_result

    return distances, predecesseurs, interm_result


def display_smallest_path_bellman(predecesseurs, init_sommet, vertice):
    smallest_path = str(init_sommet)

    # Si l'on a encore des intermédiaires (prédecesseur)
    if predecesseurs[vertice] != init_sommet:
        """Appel récursive de notre fonction puisque l'on doit changer le sommet final en l'intermédiaire
        jusqu'à avoir pour sommet final la valeur du sommet initial, alors on aura notre chemin le plus court"""
        smallest_path = display_smallest_path_bellman(predecesseurs, init_sommet, predecesseurs[vertice])
    return smallest_path + " -> " + str(vertice)


def get_solution_bellman(distances, predecesseurs, init_sommet):
    """
    Affichage des solution de l'algorithme de bellman
    Affichage de l'ensemble des plus court chemin pour chaque sommet par rapport au sommet initial
    """
    array_shortest_path = []
    for v in distances:
        message_shortest_path = "Plus court chemin de "
        message_shortest_path += str(init_sommet)
        message_shortest_path += " à "
        message_shortest_path += str(v) + " : "
        message_shortest_path += display_smallest_path_bellman(predecesseurs, init_sommet, v)
        message_shortest_path += " (poids = " + str(distances[v]) + ")"
        array_shortest_path.append(message_shortest_path)

    return array_shortest_path
