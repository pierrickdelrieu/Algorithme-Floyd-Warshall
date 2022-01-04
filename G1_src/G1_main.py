from G1_read_files import *
from G1_algo_floyd_warshall import *
from G1_algo_bellman import *
from G1_class_graph import *
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
            print("Vous avez choisit le graphe", file_name, "\n\n")
            display_array_graph(Graph.array_transitions)

            print("\n         ********** Matrice d'adjacence **********")
            matrice_adjacence = get_matrice_adjacence(Graph)
            for line in matrice_adjacence:
                print('         ', end="")
                cpt = 0
                for element in line:
                    print(element, end="        |      ")
                    cpt = cpt + 1
                print("\n         ----------" + (cpt-1) * "----------------")

            print('\n\n')

            print(
                "                                     -------------------------------------------------------------------")
            print(
                "                                     |       Tapez 1 pour choisir l'algorithme de Floyd Warshall       |")
            print(
                "                                     |       Tapez 2 pour choisir l'algorithme de Dijkstra             |")
            print(
                "                                     |       Tapez 3 pour choisir l'algorithme de Bellman              |")
            print(
                "                                     |       Tapez 4 pour ecrire la trace du graphe                    |")
            print(
                "                                     |       Tapez autre chose pour quitter                            |")
            print(
                "                                     -------------------------------------------------------------------")
            input_user = input("Faites votre choix : ")

            # FLOYD WARSHALL
            if input_user == '1':
                print("--------------------------------------------------")
                print("|        Affichage des plus courts chemins       |")
                print("|                  Floyd Warshall                |")
                print("--------------------------------------------------\n")

                array_distance, array_path, interm_result = floyd_warshall(Graph)
                print("********** Etapes intermediaires **********\n")
                for line in interm_result:
                    print(line + '\n')

                print("********** Solution **********\n")
                if array_distance is None:
                    print("Il y a un circuit absorbant\n\n")
                else:
                    solutions = get_solution_floyd_warshall(array_path, array_distance)
                    for line in solutions:
                        print(line)
                    print('\n\n')

            # DIKSTRA
            elif input_user == '2':
                print("Vous allez utiliser l'algorithme de Dikstra \n\n")

            # BELLMAN
            elif input_user == '3':
                print("--------------------------------------------------")
                print("|        Affichage des plus courts chemins       |")
                print("|                     Bellman                    |")
                print("--------------------------------------------------\n")

                distances, predecesseurs, interm_result = bellman(Graph, get_init_sommet(Graph.array_transitions))
                print("********** Etapes intermediaires **********\n")
                for line in interm_result:
                    print(line)

                print("\n\n********** Solution **********\n")
                if distances is None:
                    print("Il y a un circuit absorbant")
                else:
                    solutions = get_solution_bellman(distances, predecesseurs, get_init_sommet(Graph.array_transitions))
                    for line in solutions:
                        print(line)

                    print('\n\n')

            # TRACE
            elif input_user == '4':
                # # Ecriture des traces pour tous les graphes
                # for i in range(1, 14):
                #     Graph = read_graph(str(i))
                #     write_graph_trace(Graph, str(i))

                write_graph_trace(Graph, file_name)

            else:
                keep_going = False

clear()
print("Au revoir :)")
