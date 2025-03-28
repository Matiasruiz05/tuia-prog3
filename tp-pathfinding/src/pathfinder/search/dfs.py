from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

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

        frontier = StackFrontier()
        frontier.add(node)

        i = 0

        if node.state == grid.end:
            return Solution(node , explored)    

        while not frontier.is_empty():

            node = frontier.remove()

            if i:
                if node.state in explored.keys():
                    continue
            
            i = 1

            for accion , estado in grid.get_neighbours(node.state).items() :                                #iteramos los estados a los que podemos llegar con sus respectivas acciones
                if estado not in explored :


                    N = Node( "" , estado , node.cost + grid.get_cost(estado) , node , accion)    #Si un estado destino no está en explorados creamos un nodo con el respectivo estado

                    explored[N.state] = True                                                                                                            
                    
                    if N.state == grid.end:                                                                 #Revisamos si ese nuevo nodo es solución, de serlo devolvemos
                        return Solution(N , explored)
                    

                    frontier.add(N)



        return NoSolution(explored)
