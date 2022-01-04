from G1_read_files import *
from G1_src.G1_class_graph import *


def floyd_warshall(Graph):
    interm_result = []
    # tableau qui contiendra les distances les plus courtes
    array_distance = []
    # tableau qui contiendra les chemins les plus court
    array_path = []
    # print(Graph.array_transitions)


    """Construction de la table initial des distances remplie de "inf" et de dimension nb de sommets * nb de sommets
    + construction de la table initiale des chemins les plus courts, remplie de -1"""
    for i in range(Graph.number_vertices):
        subtable_initialization = []
        subtable_path = []
        for l in range(Graph.number_vertices):
            subtable_initialization.append(float("inf"))  # valeur infinie
            subtable_path.append(-1)
        array_distance.append(subtable_initialization)
        array_path.append(subtable_path)
    # print(array_path)
    # print(array_distance)


    """Remplissage de la matrice d'initialisation des distances avec les valeurs réelles et de la matrice des chemins 
    avec les valeurs réelles"""
    # Le chemin partant d'un point et retournant dans ce meme point vaut initialement 0

    for i in range(len(array_distance)):
        array_distance[i][i] = 0
        array_path[i][i] = -1

    for i in range(len(Graph.array_transitions)):
        array_distance[Graph.array_transitions[i][0]][Graph.array_transitions[i][1]] = Graph.array_transitions[i][2]
        array_path[Graph.array_transitions[i][0]][Graph.array_transitions[i][1]] = Graph.array_transitions[i][0]

    # print('\n')
    # print(array_path)
    # print(array_distance)
    # print('\n')
    interm_result.append("k = 0\n     distance : \n" + get_matrice_from_tab("          ",array_distance) + "\n     predecesseur : \n" + get_matrice_from_tab("          ", array_path) + "\n")


    """Ces boucles imbriquées vont nous permettre de tester les N^3 possibilités de chemins, avec 
    N la dimension du graphe."""
    for intermediary in range(len(array_distance)):
        for begin in range(len(array_distance)):
            for final in range(len(array_distance)):
                if array_distance[begin][final] > array_distance[begin][intermediary] + array_distance[intermediary][final]:
                    array_distance[begin][final] = array_distance[intermediary][final] + array_distance[begin][intermediary]
                    array_path[begin][final] = array_path[intermediary][final]

            if array_distance[begin][begin] < 0:
                # interm_result.append("erreur : " + str(begin) + "\n     distance : \n" + get_matrice_from_tab("          ", array_distance) + "\n     predecesseur : \n" + get_matrice_from_tab("          ", array_path) + "\n")
                interm_result.append("Cycle de poids négatif")
                return None, None, interm_result

        interm_result.append("k = " + str(intermediary+1) + "\n     distance : \n" + get_matrice_from_tab("          ", array_distance) + "\n     predecesseur : \n" + get_matrice_from_tab("          ", array_path) + "\n")


    # print(array_distance)
    # print(array_path)

    return array_distance, array_path, interm_result


def display_smallest_path(array_path, begin, final):
    smallest_path = str(begin)
    # Si l'on a encore des intermédiaires (prédecesseur)
    if array_path[begin][final] != begin:
        """Appel récursive de notre fonction puisque l'on doit changer le sommet final en l'intermédiaire
        jusqu'à avoir pour sommet final la valeur du sommet initial, alors on aura notre chemin le plus court"""
        smallest_path = display_smallest_path(array_path, begin, array_path[begin][final])
    return smallest_path + " -> " + str(final)


# fonction qui affiche un graphe à l'aide de son tableau de transitions
def display_array_graph(array_transitions):
    print("                     --------------------------------------------------")
    print("                     |  sommet initial | sommet final |     poids     |")
    print("                     --------------------------------------------------")
    for i in range(len(array_transitions)):
        message_display_graph = ""
        message_display_graph += str("                     |        ")
        message_display_graph += str(array_transitions[i][0])
        message_display_graph += str("        |      ")
        message_display_graph += str(array_transitions[i][1])

        message_display_graph += str("       |        ")
        message_display_graph += str(array_transitions[i][2])
        if array_transitions[i][2] > 0:
            message_display_graph += str("      |")
        else:
            message_display_graph += str("     |")
        print(message_display_graph)
        print("                     --------------------------------------------------")


def create_array_display_graph(array_graph_transitions):
    array_display_graph = []
    array_display_graph.append(str("--------------------------------------------------"))
    array_display_graph.append(str("|  sommet initial | sommet final |     poids     |"))
    array_display_graph.append(str("--------------------------------------------------"))
    for vertices in range(len(array_graph_transitions)):
        message_display_graph = ""
        message_display_graph += str("|        ")
        message_display_graph += str(array_graph_transitions[vertices][0])
        message_display_graph += str("        |      ")
        message_display_graph += str(array_graph_transitions[vertices][1])
        message_display_graph += str("       |        ")
        message_display_graph += str(array_graph_transitions[vertices][2])
        message_display_graph += str("      |")
        array_display_graph.append(message_display_graph)
        array_display_graph.append("--------------------------------------------------")
    return array_display_graph


"""Fonction permettant de retourner un tableau contenant l'affichage d'un tableau à l'aide du tableau des distances
créé avec l'algorithme de Floyd Warshall"""


def create_array_display_graph_Floyd(array_distance):
    array_display_graph = []
    array_display_graph.append(str("--------------------------------------------------"))
    array_display_graph.append(str("|  sommet initial | sommet final |     poids     |"))
    array_display_graph.append(str("--------------------------------------------------"))
    for initial_vertice in range(len(array_distance)):
        for final_vertice in range(len(array_distance[initial_vertice])):
            if (array_distance[initial_vertice][final_vertice] != 0 and array_distance[initial_vertice][
                final_vertice] != float("inf") and array_distance[initial_vertice][final_vertice] > 0):
                message_display_graph = ""
                message_display_graph += str("|        ")
                message_display_graph += str(initial_vertice)
                message_display_graph += str("        |      ")
                message_display_graph += str(final_vertice)
                message_display_graph += str("       |        ")
                message_display_graph += str(array_distance[initial_vertice][final_vertice])
                message_display_graph += str("      |")
                array_display_graph.append(message_display_graph)
                array_display_graph.append("--------------------------------------------------")
            elif (array_distance[initial_vertice][final_vertice] != 0 and array_distance[initial_vertice][
                final_vertice] < 0):
                message_display_graph = []
                message_display_graph = ""
                message_display_graph += str("|        ")
                message_display_graph += str(initial_vertice)
                message_display_graph += str("        |      ")
                message_display_graph += str(final_vertice)
                message_display_graph += str("       |       ")
                message_display_graph += str(array_distance[initial_vertice][final_vertice])
                message_display_graph += str("      |")
                array_display_graph.append(message_display_graph)
                array_display_graph.append("--------------------------------------------------")
    return array_display_graph


# fonction permettant l'affichage du graphe en console
def display_graph(array_display_graph):
    for i in range(len(array_display_graph)):
        print("                             ", array_display_graph[i])


def get_solution_floyd_warshall(array_path, array_diatance):
    """
    Affichage des solution de l'algorithme de Floyd Warshall
    Affichage de l'ensemble des plus court chemin pour de chaque sommet a chaque sommet
    """
    array_shortest_path = []
    for i in range(len(array_path)):
        for v in range(len(array_path)):
            if array_path[i][v] != -1:
                message_shortest_path = "Plus court chemin de "
                message_shortest_path += str(i)
                message_shortest_path += " à "
                message_shortest_path += str(v) + " : "
                message_shortest_path += display_smallest_path(array_path, i, v)
                message_shortest_path += " (poids = " + str(array_diatance[i][v]) + ")"
                array_shortest_path.append(message_shortest_path)
    return array_shortest_path