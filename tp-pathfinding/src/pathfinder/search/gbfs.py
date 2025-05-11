from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:

    @staticmethod
    def gbfsh(grid: Grid, node: Node) -> int:
        return abs(grid.end[0]-node.state[0]) + abs(grid.end[1]-node.state[1])

    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        # Add the node to the explored dictionary
        explored[node.state] = True
        

        frontier = PriorityQueueFrontier() # Creamos la frontera relacionada con la cola de prioridad que usa h
        frontier.add(node) # Añadimos el nodo inicial

        if node.state == grid.end: #Chequeamos que el inicio no sea la salida
            return Solution(node, explored) # Si lo es, devolvemos el nodo y los alcanzados
        
        # Si no lo es, expandimos la frontera

        while not frontier.is_empty(): 
            
            node = frontier.pop() #Sacamos el primero en orden de prioridades, pop se encarga

            for accion , estado in grid.get_neighbours(node.state).items() : #Inicio un bucle para agregar a frontera a todos los vecinos, pop se encargará de elegir el de menor valor eurístico
                C = node.cost + grid.get_cost(estado)
                if estado not in explored or C < explored[estado]: # Chequeno que no sea un estado ya alcanzado
                    N = Node( "" , estado , node.cost + grid.get_cost(estado) , node, accion) #Creamos un nodo con el estado, el costo de la casilla + la accion de llegar a este estado, el padre y la accion que lo llevo hasta acá
                    explored[estado] = C
                    if N.state == grid.end: #Chequeamos que no sea el objetivo
                        return Solution(N, explored)
                    frontier.add(N, GreedyBestFirstSearch.gbfsh(grid, N))







        return NoSolution(explored)
