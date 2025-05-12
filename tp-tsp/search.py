"""Este modulo define la clase LocalSearch.

LocalSearch representa un algoritmo de busqueda local general.

Las subclases que se encuentran en este modulo son:

* HillClimbing: algoritmo de ascension de colinas. Se mueve al sucesor con
mejor valor objetivo. Ya viene implementado.

* HillClimbingReset: algoritmo de ascension de colinas de reinicio aleatorio.
No viene implementado, se debe completar.

* Tabu: algoritmo de busqueda tabu.
No viene implementado, se debe completar.
"""


from __future__ import annotations
from time import time
from problem import OptProblem
from problem import colaTabu


class LocalSearch:
    """Clase que representa un algoritmo de busqueda local general."""

    def __init__(self) -> None:
        """Construye una instancia de la clase."""
        self.niters = 0  # Numero de iteraciones totales
        self.time = 0  # Tiempo de ejecucion
        self.tour = []  # Solucion, inicialmente vacia
        self.value = None  # Valor objetivo de la solucion

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion."""
        self.tour = problem.init
        self.value = problem.obj_val(problem.init)


class HillClimbing(LocalSearch):
    """Clase que representa un algoritmo de ascension de colinas.

    En cada iteracion se mueve al estado sucesor con mejor valor objetivo.
    El criterio de parada es alcanzar un optimo local.
    """

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        value = problem.obj_val(problem.init)

        while True:

            # Buscamos la acción que genera el sucesor con mayor valor objetivo
            act, succ_val = problem.max_action(actual)

            # Retornar si estamos en un maximo local:
            # el valor objetivo del sucesor es menor o igual al del estado actual
            if succ_val <= value:

                self.tour = actual
                self.value = value
                end = time()
                self.time = end-start
                return

            # Sino, nos movemos al sucesor
            actual = problem.result(actual, act)
            value = succ_val
            self.niters += 1


class HillClimbingReset(LocalSearch):
    """Algoritmo de ascension de colinas con reinicio aleatorio."""

    def __init__(self, reinicios:int =100):
        super().__init__()
        self.reinicios = reinicios

    def solve(self, problem: OptProblem):

        # Inicio del reloj
        start = time()

        # Arrancamos desde el estado inicial
        mejor_tour = problem.init
        mejor_value = problem.obj_val(problem.init)

        actual = problem.init
        value = problem.obj_val(problem.init)

        for i in range(self.reinicios + 1):

            #Esta condicion nos garantiza que evaluemos el caso base. Luego comenzaremos a evaluar casos con comienzos aleatorios
            if i == 0:
                actual = problem.init
            else:
                actual = problem.random_reset()
                
            value = problem.obj_val(actual)

            while True:

                # Buscamos la acción que genera el sucesor con mayor valor objetivo
                act, succ_val = problem.max_action(actual)

                #Si el valor objetivo del sucesor es menor o igual al del estado actual salimos del while porque significa que estamos en un maximo local
                if succ_val <= value:
                    break

                # Sino, nos movemos al sucesor
                actual = problem.result(actual, act)
                value = succ_val
                self.niters += 1
            
            #Si el estado al que llegamos tiene un mejor valor que el mejor que habiamos encontrado hasta el momento lo registramos como el mejor
            if value > mejor_value:
                mejor_tour = actual
                mejor_value = value

        self.tour = mejor_tour
        self.value = mejor_value
        self.time = time() - start





class Tabu(LocalSearch):
    """Algoritmo de busqueda tabu."""

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con búsqueda tabú

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial y lo definimos como el mejor
        actual = problem.init
        value = problem.obj_val(problem.init)
        self.tour = actual
        self.value = value

        # Inicializamos la lista tabú vacía y el criterio de parada
        tabu_list = colaTabu()
        contador = 0


        # Iniciamos un bucle que no para hasta cumplir el criterio de parada
        while contador < 15:

            # Buscamos la acción que genera el sucesor con mayor valor objetivo.
            # max_action gestiona la lista tabú
            act, succ_val = problem.max_actionTabu(actual, tabu_list)

            # Revisamos si este estado es mejor al mejor histórico para reiniciar el contador
            if succ_val <= value :
                self.tour = actual # Si lo es, reiniciamos el contador y reasignamos el mejor histórico junto con su valor
                self.value = value
                contador = 0
            # Si no lo es, modificamos el contador para evitar ejecución infinita
            else:
                contador += 1
            # Avanzamos al estado sucesor
            actual = problem.result(actual, act)
            value = succ_val
            self.niters += 1

        # Terminado el bucle, terminamos la ejecución de la búsqueda
        end = time()
        self.time = end-start
            


"""
            # Retornar si estamos en un maximo local:
            # el valor objetivo del sucesor es menor o igual al del estado actual
            if succ_val <= value:

                self.tour = actual
                self.value = value
                end = time()
                self.time = end-start
                return

            # Sino, nos movemos al sucesor
            actual = problem.result(actual, act)
            value = succ_val
            self.niters += 1



"""