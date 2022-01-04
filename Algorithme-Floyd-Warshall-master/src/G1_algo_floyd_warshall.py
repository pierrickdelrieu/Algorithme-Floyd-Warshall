from G1_read_files import *


def floyd_warshall(Graph):
    interm_result = []
    # tableau qui contiendra les distances les plus courtes
    array_distance = []
    # tableau qui contiendra les chemins les plus court
    array_path = []
    # print(Graph.array_transitions)

    #absorbent = absorbent_circuit_detection(Graph.array_transitions)
    absorbent = False
    if(absorbent):
        print("Detection d'un circuit absorbent sur le graphe ! \nImpossibilité d'effectuer Floyd Warshall dessus ! ")
        return array_distance,array_path,interm_result,absorbent
    else:
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
        for i in range(len(Graph.array_transitions)):
            array_distance[Graph.array_transitions[i][0]][Graph.array_transitions[i][1]] = Graph.array_transitions[i][2]
            array_path[Graph.array_transitions[i][0]][Graph.array_transitions[i][1]] = Graph.array_transitions[i][0]
        # Le chemin partant d'un point et retournant dans ce meme point vaut initialement 0
        for i in range(len(array_distance)):
            array_distance[i][i] = 0
            array_path[i][i] = -1
        # print('\n')
        # print(array_path)
        # print(array_distance)
        # print('\n')
        interm_result.append("0 | distance : " + str(array_distance) + '\n' + "0 | predecesseur : " + str(array_path) + "\n")


        """Ces boucles imbriquées vont nous permettre de tester les N^3 possibilités de chemins, avec 
        N la dimension du graphe."""
        for intermediary in range(len(array_distance)):
            for begin in range(len(array_distance)):
                for final in range(len(array_distance)):
                    if (array_distance[begin][final] > array_distance[intermediary][final] + array_distance[begin][
                        intermediary]):
                        array_distance[begin][final] = array_distance[intermediary][final] + array_distance[begin][
                            intermediary]
                        array_path[begin][final] = array_path[intermediary][final]

                if array_distance[begin][begin] < 0:
                    interm_result.clear()
                    interm_result.append("Cycle de poids négatif")
                    return array_distance, array_path, interm_result,None
            interm_result.append(str(intermediary) + " | distance : " + str(array_distance) + '\n' + str(intermediary) + " | predecesseur : " + str(array_path) + "\n")

        # print(array_distance)
        # print(array_path)

        return array_distance, array_path, interm_result,absorbent


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
        if (array_transitions[i][2] > 0):
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

def absorbent_circuit_detection(array_transitions):
    """
    Detection d'un circuit absorbant dans un graphe:
    Retourne True lorsqu'un circuit absorbant est détecté, False sinon.
    """
    dictionnary_successor = dict()
    for vertice in range(len(array_transitions)):
        if(array_transitions[vertice][0] not in dictionnary_successor):
            dictionnary_successor[array_transitions[vertice][0]] = dict()
            dictionnary_successor[array_transitions[vertice][0]]["successor"] = []
            dictionnary_successor[array_transitions[vertice][0]]["weight"] = []
        if (array_transitions[vertice][1] not in dictionnary_successor):
            dictionnary_successor[array_transitions[vertice][1]] = dict()
            dictionnary_successor[array_transitions[vertice][1]]["weight"] = []
            dictionnary_successor[array_transitions[vertice][1]]["successor"] = []
        if(array_transitions[vertice][1] not in dictionnary_successor[array_transitions[vertice][0]]["successor"]):
            dictionnary_successor[array_transitions[vertice][0]]["successor"].append(array_transitions[vertice][1])
            dictionnary_successor[array_transitions[vertice][0]]["weight"].append(array_transitions[vertice][2])
    #Détection d'un chemin absorbant

    sommets_succ=[]
    sommets_succ.append(array_transitions[0][0])
    result = chercher_succ(sommets_succ, array_transitions, dictionnary_successor)
    sommets_succ = result[0]

    print(sommets_succ)
    poids = 0
    if result[1] == False: #vérification absorbance
        i = 1
        try:
            index_weight = dictionnary_successor[1]["successor"].index(1)
            poids+= dictionnary_successor[1]["weight"][index_weight]
            if(poids < 0):
                print("Detection d'un circuit absorbant !")
                return True
        except:
            return False
    return False
    

def chercher_succ (tab_succ, array_transitions, dictionnary_successor):
    for k in tab_succ:
        for i in range(len(array_transitions)):
            for j in dictionnary_successor[k]["successor"]:
                if j != tab_succ[0]:
                    tab_succ.append(j)
                if j == tab_succ[0]:
                    tab_succ.append(j)
                    #vérification de l'existance d'un circuit absorbant
                    return tab_succ,False
    return (tab_succ,True)

def get_solution_floyd_warshall(array_path, array_distance):
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
                message_shortest_path += " (poids = " + str(array_distance[v]) + ")"
                array_shortest_path.append(message_shortest_path)
    return array_shortest_path