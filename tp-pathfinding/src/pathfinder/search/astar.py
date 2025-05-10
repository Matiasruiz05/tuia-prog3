from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:

    @staticmethod
    def manh(grid: Grid, node: Node) -> int:
        return abs(grid.end[0]-node.state[0]) + abs(grid.end[1]-node.state[1])
    
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        #Inicializamos la frontera como una cola de prioridad
        frontier = PriorityQueueFrontier()
        frontier.add(node, node.cost + AStarSearch.manh(grid, node))

        # Add the node to the explored dictionary
        explored[node.state] = node.cost

        while not frontier.is_empty():

            node = frontier.pop()
            
            if node.state == grid.end:
                return Solution(node, explored)
            
            for accion , estado in grid.get_neighbours(node.state).items():
                C = node.cost + grid.get_cost(estado)              
                
                if estado not in explored.keys() or C < explored[estado]:
                    N = Node( "" , estado , C , node , accion)
                    explored[estado] = C
                    frontier.add(N, N.cost + AStarSearch.manh(grid, N))

        return NoSolution(explored)
