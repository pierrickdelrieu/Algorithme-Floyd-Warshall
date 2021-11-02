from read_files import *
from algo_floyd_warshall import *
graph = read_graph("graphe_2")
array_distance, array_path = floyd_warshall(graph)
display_solution(array_path)