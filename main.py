from read_files import *
from algo_floyd_warshall import *
print("                                 ----------------------------------------------------------------------------------------------")
print("                                 | Bienvenue dans notre application dediée aux algorithmes de plus court chemin d'un graphe ! |")
print("                                 ----------------------------------------------------------------------------------------------")
print("\n               Au sein de cette application, vous aurez la possibilité de renseigner un graphique sous forme de format text")
print("               Nous vous renverrons dans un premier temps l'affichage de votre graphique")
print("               Ensuite, nous nous chargerons d'affecter l'algorithme de votre choix à votre graphe afin \n               de vous renvoyer les plus court chemins associés à vos sommets\n\n")
keep_going = True
while(keep_going):
    print("                                     -------------------------------------------------------------------")
    print("                                     |       Tapez 1 pour écrire un graphe en fichier texte            |")
    print("                                     |       Tapez 2 pour choisir l'algorithme de Floyd Warshall       |")
    print("                                     |       Tapez 3 pour choisir l'algorithme de Dijkstra             |")
    print("                                     |       Tapez 4 pour choisir l'algorithme de Bellman              |")
    print("                                     |       Tapez autre chose pour quitter                            |")
    print("                                     -------------------------------------------------------------------")
    input_user = input("Faites votre choix : ")
    if(input_user == '1'):
        write_graph()
    elif(input_user == '2'):
        print("         -----------------------------------------------------------------------------------------------------------------------------------------")
        print("         | Tapez 1 pour afficher votre graphe et les plus court chemins    | Tapez 2 pour afficher votre graphe | Tapez autre chose pour quitter |")
        print("         -----------------------------------------------------------------------------------------------------------------------------------------\n")
        input_user = input("Faites votre choix : ")

        if(input_user != '1' and input_user != '2'):
            keep_going = False
        elif(input_user == '2'):
            file_name = input("Entrez le nom de votre fichier, sans l'extension : ")
            try:
                Graph = read_graph(file_name)
                display_array_graph(Graph.array_transitions)
            except:
                print("fichier introuvable !")
        else:
            file_name = input("Entrez le nom de votre fichier, sans l'extension : ")
            try:
                Graph = read_graph(file_name)
                display_array_graph(Graph.array_transitions)
                array_distance, array_path = floyd_warshall(Graph)
                tuple_result = display_solution(array_path, array_distance)
                array_shortest_path = tuple_result[0]
                array_display_graph = tuple_result[1]
                write_graph_Floyd_Warshall(file_name,array_shortest_path,array_display_graph,Graph)
            except:
                print("fichier introuvable !")
    elif(input_user=='3'):
        print("Vous allez utiliser l'algorithme de Dikstra")
    elif(input_user == '4'):
        print("Vous allez utiliser l'algorithme de Bellman")
    else:
        keep_going = False
