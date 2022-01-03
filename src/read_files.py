from class_graph import *
import re

# Fonction nous permettant de lire un graphe sous forme de fichier texte
from src.algo_bellman import *
from src.algo_floyd_warshall import *


def read_graph(file_name):
    try:
        RepresentationGraph = Graph(0, 0, [])
        array_number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        array_graph = []
        file = open("../graph_files/G1-Graphe" + file_name + ".txt", "r")

        """Nous allons lire le fichier ligne par ligne. Lorsque l'on rencontre
        un caractère retour à la ligne nous le supprimons. 
        Nous transformons chaque ligne en liste"""
        lines = file.readline()
        while lines != '':
            lines = list(lines)
            if '\n' in lines:
                lines.remove('\n')
            array_graph.append(lines)
            lines = file.readline()
        file.close()

        new_array_graph = []
        for i in range(len(array_graph)):
            element_graph = ""
            element_new_array_graph = []
            for l in range(len(array_graph[i])):
                if array_graph[i][l] != '-' and array_graph[i][l] not in array_number:
                    element_new_array_graph.append(int(element_graph))
                    element_graph = ""
                if array_graph[i][l] == '-' or array_graph[i][l] in array_number:
                    element_graph += array_graph[i][l]
            element_new_array_graph.append(int(element_graph))
            new_array_graph.append(element_new_array_graph)

        # Stockage du nombre de sommets, d'arcs et des transitions dans notre class Graph
        RepresentationGraph.number_vertices = new_array_graph[0][0]
        RepresentationGraph.number_arcs = new_array_graph[1][0]

        # Suppression du conteneur du nombre de sommets
        del new_array_graph[0]
        # Suppression du conteneur du nombre d'arcs
        del new_array_graph[0]

        RepresentationGraph.array_transitions = new_array_graph

        return RepresentationGraph

    except:
        return None


def write_graph():
    keep_going = True
    while keep_going:
        print(
            "\nAfin d'entrer le nom de votre fichier, vous devez respecter la syntaxe suivante : G1-Graphe[numéro de votre fichier]")
        print("Exemple : G1-Graphe2\n")
        file_name = input("Entrez le nom du fichier, sans l'extension, dans lequel vous voulez écrire votre graphe : ")
        pattern = "^G1-Graphe[1-9]$"
        result = re.match(pattern, file_name)
        if (result):
            entry_file = []
            input_number_vertices = input("Entrez le nombre de sommets de votre graphe : ")
            array_number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            index = 0
            verification_input = True
            # Suppression des espaces de l'entrée utilisateur
            input_number_vertices = re.sub(" ", "", input_number_vertices)
            while index < len(input_number_vertices):
                # Si l'utilisateur a entré un caractère autre qu'un chiffre
                if (input_number_vertices[index] not in input_number_vertices):
                    print("Vous n'avez pas entré un nombre !\nImpossible d'écrire cela dans le fichier")
                    verification_input = False
                    index = len(input_number_vertices)
                index += 1
            if verification_input == False:
                input_user = input("Tapez 1 pour continuer, ou quelque chose d'autre sinon : ")
                input_user = re.sub(" ", "", input_user)
                if input_user != '1':
                    keep_going = False
            input_number_vertices += "\n"
            entry_file.append(input_number_vertices)
            if keep_going and verification_input:
                input_number_arcs = input("Entrez le nombre d'arcs de votre graphe : ")
                input_number_arcs = re.sub(" ", "", input_number_arcs)
                index = 0
                while index < int(input_number_arcs):
                    # Si l'utilisateur a entré un caractère autre qu'un chiffre
                    if (input_number_arcs[index] not in input_number_arcs):
                        print("Vous n'avez pas entré un nombre !\nImpossible d'écrire cela dans le fichier")
                        verification_input = False
                        index = len(input_number_arcs)
                    index += 1
                if verification_input == False:
                    input_user = input("Tapez 1 pour continuer, ou quelque chose d'autre sinon : ")
                    input_user = re.sub(" ", "", input_user)
                    if (input_user != '1'):
                        keep_going = False
            input_number_arcs += "\n"
            entry_file.append(input_number_arcs)
            # liste comprenant la numérotation des sommets du graphe
            list_vertices = []
            for vertices in range(len(input_number_vertices)):
                list_vertices.append(str(vertices))
            if keep_going and verification_input:
                number_vertices = 0
                pattern_vertice = "^[0-9]$"
                while int(number_vertices) < int(input_number_vertices):
                    print("Arc numéro ", number_vertices + 1)
                    initial_state = input("Entrez le sommet initial de cet arc : ")
                    initial_state = re.sub(" ", "", initial_state)
                    result = re.match(pattern_vertice, initial_state)
                    while (not result or initial_state not in list_vertices):
                        print("Votre sommet doit être un nombre entier compris dans la liste : ", list_vertices)
                        initial_state = input("Entrez le sommet initial de cet arc : ")
                        initial_state = re.sub(" ", "", initial_state)
                        result = re.match(pattern_vertice, initial_state)
                    number_vertices += 1
                    final_state = input("Entrez le sommet final de cet arc : ")
                    final_state = re.sub(" ", "", final_state)
                    result = re.match(pattern_vertice, final_state)
                    while not result or final_state not in list_vertices:
                        print("Votre sommet doit être un nombre entier compris dans la liste : ", list_vertices)
                        final_state = input("Entrez le sommet initial de cet arc : ")
                        final_state = re.sub(" ", "", final_state)
                        result = re.match(pattern_vertice, final_state)
                    weight = input("Entrez le poids de votre arc : ")
                    weight = re.sub(" ", "", weight)
                    pattern_weight = "^?-[0-9]$"
                    result = re.match(pattern_weight, weight)
                    while not result:
                        print("Votre poids doit être un nombre.")
                        weight = input("Entrez le sommet initial de cet arc : ")
                        print("weight : ", weight)
                        weight = re.sub(" ", "", weight)
                        result = re.match(pattern_weight, weight)
                    arc = initial_state
                    arc += " "
                    arc += final_state
                    arc += " "
                    arc += weight
                    arc += "\n"
                    entry_file.append(arc)
            print(entry_file)

        else:
            print("\nVotre nom de fichier ne respecte pas la syntaxe indiqué.")
            input_user = input("Tapez 1 pour écrire dans un autre fichier, ou quelque chose d'autre pour quitter : ")
            input_user = re.sub(" ", "", input_user)
            if input_user != '1':
                keep_going = False


def write_graph_trace(Graph, file_name):
    # Graph.number_vertices = " ".join(str(elem) for elem in Graph.number_vertices)
    # Graph.number_arcs = " ".join(str(elem) for elem in Graph.number_arcs)

    file = open("../traces/G1_Graphe" + file_name + "_result.txt", "w+", encoding="UTF-8")

    file.write("\n                                       -----------------------------------------------\n")
    file.write("                                       |           Caractéristiques du graphe        |\n")
    file.write("                                       -----------------------------------------------\n\n")
    file.write("        Ce graphe contient " + str(Graph.number_vertices) + " sommets " + "et  " + str(
        Graph.number_arcs) + " arcs.\n\n")

    file.write("                                       -----------------------------------------------\n")
    file.write("                                       |             Affichage du graphe             |\n")
    file.write("                                       -----------------------------------------------\n")
    array_display_graph = create_array_display_graph(Graph.array_transitions)
    for i in range(len(array_display_graph)):
        file.write("\n                                      ")
        file.write(array_display_graph[i])

    file.write("\n\n         ********** Matrice d'adjacence **********\n")
    matrice_adjacence = get_matrice_adjacence(Graph)
    for line in matrice_adjacence:
        file.write('         ')
        cpt = 0
        for element in line:
            file.write(str(element) + "        |      ")
            cpt = cpt + 1
        file.write("\n         ----------" + (cpt - 1) * "----------------" + '\n')

    file.write('\n\n')

    file.write("\n\n                                     --------------------------------------------------\n")
    file.write("                                     |   Affichage des plus court chemins du graphe   |\n")
    file.write("                                     --------------------------------------------------\n\n")

    file.write("------------------------------ FLOYD WARSHALL ------------------------------\n")

    array_distance, array_path, interm_result = floyd_warshall(Graph)
    file.write("********** Etapes intermediaires **********\n")
    for line in interm_result:
        file.write(line + '\n')

    file.write("********** Solution **********\n")
    if array_distance is None:
        file.write("Il y a un circuit absorbant")
    else:
        solutions = get_solution_floyd_warshall(array_path, array_distance)
        for line in solutions:
            file.write(line + '\n')

    # BELLMAN
    file.write("\n\n------------------------------ BELLMAN ------------------------------\n")
    distances, predecesseurs, interm_result = bellman(Graph, get_init_sommet(Graph.array_transitions))
    file.write("********** Etapes intermediaires **********\n")
    for line in interm_result:
        file.write(line + '\n')


    file.write("********** Solution **********\n")
    if distances is None:
        file.write("Il y a un circuit absorbant")
    else:
        solutions = get_solution_bellman(distances, predecesseurs, get_init_sommet(Graph.array_transitions))
        for line in solutions:
            file.write(line + '\n')

    print("\nLa trace du graphe " + file_name + " a ete ecrite dans le fichier /traces/G1_Graphe" + file_name + "_result.txt.\n")
    file.close()
