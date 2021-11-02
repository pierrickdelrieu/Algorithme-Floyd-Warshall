from read_files import *
def floyd_warshall(Graph):
    #tableau qui contiendra les distances les plus courtes
    array_distance = []
    #tableau qui contiendra les chemins les plus court
    array_path = []
    """Construction de la table initial des distances remplie de "inf" et de dimension le nb de sommets
    + construction de la table intiail des chemins les plus courts, remplie de -1"""
    for i in range(Graph.number_vertices[0]):
        subtable_initialization = []
        subtable_path = []
        for l in range(Graph.number_vertices[0]):
            subtable_initialization.append(float("inf"))
            subtable_path.append(-1)
        array_distance.append(subtable_initialization)
        array_path.append(subtable_path)
    """Remplissage de la matrice d'initialisation des distances avec les valeurs réelles et de la matrice des chemins 
    avec les valeurs réelles"""
    for i in range(len(Graph.array_transitions)):
        array_distance[Graph.array_transitions[i][0]][Graph.array_transitions[i][1]] = Graph.array_transitions[i][2]
        array_path[Graph.array_transitions[i][0]][Graph.array_transitions[i][1]] = Graph.array_transitions[i][0]
    print(array_path)
    #Le chemin partant d'un point et retournant dans ce même point vaut initialement 0
    for i in range(len(array_distance)):
        array_distance[i][i] = 0
        array_path[i][i] = -1
    """Ces boucles imbriquées vont nous permettre de tester les N^3 possibilités de chemins, avec 
    N la dimension du graphe."""
    for intermediary in range (len(array_distance)):
        for begin in range(len(array_distance)):
            for final in range(len(array_distance)):
                if(array_distance[begin][final] > array_distance[intermediary][final] + array_distance[begin][intermediary]):
                    array_distance[begin][final] = array_distance[intermediary][final] + array_distance[begin][intermediary]
                    array_path[begin][final] = array_path[intermediary][final]
            if(array_distance[begin][begin] < 0):
                print("Cycle de poids négatif")
                return

    return array_distance,array_path
def display_smallest_path(array_path,begin,final):
    smallest_path = str(begin)
    # Si l'on a encore des intermédiaires (prédecesseur)
    if(array_path[begin][final] != begin):
        """Appel récursive de notre fonction puisque l'on doit changer le sommet final en l'intermédiaire
        jusqu'à avoir pour sommet final la valeur du sommet initial, alors on aura notre chemin le plus court"""
        smallest_path = display_smallest_path(array_path,begin,array_path[begin][final])
    return smallest_path + " -> " + str(final)

def display_solution(array_path):
    for i in range(len(array_path)):
        for v in range(len(array_path)):
            if(array_path[i][v] != -1):
                print("Plus court chemin de ",i," à ",v, " : (", display_smallest_path(array_path,i,v),")")
