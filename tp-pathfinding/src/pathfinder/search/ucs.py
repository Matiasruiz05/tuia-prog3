from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

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
        explored[node.state] = node.cost
        
        frontier = PriorityQueueFrontier()
        frontier.add(node , node.cost)

        while not frontier.is_empty():
            
            node = frontier.pop()

            if node.state == grid.end:
                return Solution(node , explored)
            
            for accion , estado in grid.get_neighbours(node.state).items():

                c = node.cost + grid.get_cost(node.state)

                if estado not in explored.keys() or c < explored[estado]:

                    N = Node("", estado, node.cost + grid.get_cost(estado), node, accion)
                    explored[estado]=c
                    frontier.add(N,c)

        
        return NoSolution(explored)
