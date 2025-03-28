from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

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

        # Chequeamos que el estado inicial no sea solución antes de arrancar a expandir
        if node.state == grid.end:
            return Solution(node , explored)

        # Inicializamos frontera y encolamos el primer nodo
        frontier = QueueFrontier()
        frontier.add(node)          
        
        # Comenzamos a expandir en un ciclo que falle si la frontera está fallida
        
        while not frontier.is_empty():

            node = frontier.remove()                                                                        #tomamos el último nodo encolado

            for accion , estado in grid.get_neighbours(node.state).items() :                                #iteramos los estados a los que podemos llegar con sus respectivas acciones
                if estado not in explored :
                    
                    N = Node( "" , estado , node.cost + grid.get_cost(estado) , node , accion)    #Si un estado destino no está en explorados creamos un nodo con el respectivo estado
                    
                    explored[N.state] = True                                                                                                            
                    
                    if N.state == grid.end:                                                                 #Revisamos si ese nuevo nodo es solución, de serlo devolvemos
                        return Solution(N , explored)
                    

                    frontier.add(N)

        return NoSolution(explored)
