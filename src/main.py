from read_files import *
from algo_floyd_warshall import *
from algo_bellman import *
import os


def clear():
    os.system('clear')


clear()
print(
    "                                 ----------------------------------------------------------------------------------------------")
print(
    "                                 | Bienvenue dans notre application dediée aux algorithmes de plus court chemin d'un graphe ! |")
print(
    "                                 ----------------------------------------------------------------------------------------------")
print(
    "\n               Au sein de cette application, vous aurez la possibilité de renseigner un graphique sous forme de format text")
print("               Nous vous renverrons dans un premier temps l'affichage de votre graphique")
print(
    "               Ensuite, nous nous chargerons d'affecter l'algorithme de votre choix à votre graphe afin \n               de vous renvoyer les plus court chemins associés à vos sommets\n\n")
keep_going = True
while keep_going:
    file_name = input(
        "Entrez le numero du graphe ou taper 0 pour écrire un graphe dans un fichier texte (taper -1 pour quitter) : ")
    Graph = read_graph(file_name)

    if file_name == '0':
        write_graph()
    elif file_name == '-1':
        keep_going = False
    else:
        if not Graph:
            print("fichier introuvable !")

        else:
            clear()
            print("Vous avez choisit le graphe", file_name)
            display_array_graph(Graph.array_transitions)
            print(
                "                                     -------------------------------------------------------------------")
            print(
                "                                     |       Tapez 1 pour choisir l'algorithme de Floyd Warshall       |")
            print(
                "                                     |       Tapez 2 pour choisir l'algorithme de Dijkstra             |")
            print(
                "                                     |       Tapez 3 pour choisir l'algorithme de Bellman              |")
            print(
                "                                     |       Tapez autre chose pour quitter                            |")
            print(
                "                                     -------------------------------------------------------------------")
            input_user = input("Faites votre choix : ")

            # FLOYD WARSHALL
            if input_user == '1':
                Graph = read_graph(file_name)
                array_distance, array_path = floyd_warshall(Graph)
                tuple_result = display_solution(array_path, array_distance)
                # array_shortest_path = tuple_result[0]
                # array_display_graph = create_array_display_graph(Graph.array_transitions)
                # write_graph_Floyd_Warshall(file_name, array_shortest_path, array_display_graph, Graph)

            # DIKSTRA
            elif input_user == '2':
                print("Vous allez utiliser l'algorithme de Dikstra")

            # BELLMAN
            elif input_user == '3':
                distances, predecesseurs = bellman(Graph, get_init_sommet(Graph.array_transitions))
                if distances is None:
                    print("Il y a un circuit absorbant")
                else:
                    display_solution_bellman(distances, Graph)

            else:
                keep_going = False

clear()
print("Au revoir :)")