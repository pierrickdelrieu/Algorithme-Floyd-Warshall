from class_graph import *

#Fonction nous permettant de lire un graphe sous forme de fichier texte
def read_graph(file_name):
    RepresentationGraph = Graph(0,0,[])
    array_number = ["0","1","2","3","4","5","6","7","8","9"]
    array_graph = []
    file = open("graph_files/" + file_name + ".txt","r")
    """Nous allons lire le fichier ligne par ligne. Lorsque l'on rencontre
    un caractère retour à la lligne nous le supprimons. Pour ce faire, nous transformons
    la ligne en liste"""
    lines = file.readline()
    while(lines != ''):
        lines = list(lines)
        if('\n' in lines):
            lines.remove('\n')
        array_graph.append(lines)
        lines = file.readline()
    file.close()
    new_array_graph = []
    for i in range(len(array_graph)):
        element_graph = ""
        element_new_array_graph = []
        for l in range(len(array_graph[i])):
            if(array_graph[i][l] != '-' and array_graph[i][l] not in array_number):
                element_new_array_graph.append(int(element_graph))
                element_graph = ""
            if(array_graph[i][l] == '-' or array_graph[i][l] in array_number):
                element_graph+=array_graph[i][l]
        element_new_array_graph.append(int(element_graph))
        new_array_graph.append(element_new_array_graph)
    #Stockage du nombre de sommets, d'arcs et des transitions dans notre class Graph
    RepresentationGraph.number_vertices = new_array_graph[0]
    RepresentationGraph.number_arcs = new_array_graph[1]
    #Suppression du conteneur du nombre de sommets
    del new_array_graph[0]
    #Suppression du conteneur du nombre d'arcs
    del new_array_graph[0]
    RepresentationGraph.array_transitions = new_array_graph
    return RepresentationGraph