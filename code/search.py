# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from custom_types import Direction
from pacman import GameState
from typing import Any, Tuple,List
import util

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self)->Any:
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state:Any)->bool:
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state:Any)->List[Tuple[Any,Direction,int]]:
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions:List[Direction])->int:
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()



def tinyMazeSearch(problem:SearchProblem)->List[Direction]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem:SearchProblem)->List[Direction]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 1 ICI
    '''
    
    # print("Start:", problem.getStartState())
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))   
    
    L = util.Stack()    # Initialisation LIFO
    L.push((problem.getStartState(), []))   # Ajout du premier état dans la LIFO, comment y aller depuis l'élément d'avant
    visited = [] # La memoire qui permet de retenir ou on est allés pour pas y retourner
    path = []   # Solution finale
        
    while not L.isEmpty():
        # print("\n******** New round *********\nL avant pop", L.list )
        state, path = L.pop() # Exploration du dernier état et on l'enleve de la LIFO
        # print("current state", state)
        
        # On regarde si on est dans un état final. Si oui GAGNEEEEEE
        if (problem.isGoalState(state) == True ):
            # print("\nSolution finale: ", path)
            return path
        
        # Si non : on continue la recherche
        else :
            visited.append(state)   # On ajoute notre état dans la liste des états visités
            # print("visited", visited)
            for successor, action, _ in problem.getSuccessors(state):
                if successor not in visited:
                    L.push((successor, path + [action]))    # On ajoute tous les successeurs dans la LIFO
                 
    util.raiseNotDefined()


def breadthFirstSearch(problem:SearchProblem)->List[Direction]:
    """Search the shallowest nodes in the search tree first."""


    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 2 ICI
    '''
    # C'est le meme code que pour le DFS mais avec une queue a la place de la stack
    
    L = util.Queue()    # Initialisation FIFO
    L.push((problem.getStartState(), []))   # Ajout du premier état dans la FIFO, comment y aller depuis l'élément d'avant
    visited = [] # La memoire qui permet de retenir ou on est allés pour pas y retourner
    path = []   # Solution finale
    visited.append(problem.getStartState())   # On ajoute le premier état dans la liste des états visités

        
    while not L.isEmpty():
        state, path = L.pop() 
        
        # On regarde si on est dans un état final. Si oui GAGNEEEEEE
        if (problem.isGoalState(state) == True ):
            # print("\nSolution finale: ", path)
            return path
        
        # Si non : on continue la recherche
        else :
            
            for successor, action, _ in problem.getSuccessors(state):
                if successor not in visited:
                    L.push((successor, path + [action]))    # On ajoute tous les successeurs dans la FIFO
                    visited.append(successor)   # On ajoute notre état dans la liste des états visités

    util.raiseNotDefined()

def uniformCostSearch(problem:SearchProblem)->List[Direction]:
    """Search the node of least total cost first."""


    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 3 ICI
    '''
    L = util.PriorityQueue() #Initialisation Priority Queue
    L.push((problem.getStartState(), [], 0),  0)
    visited = []
    path = []
    visited.append(problem.getStartState())   # On ajoute le premier état dans la liste des états visités

    while not L.isEmpty():
        state, path, cost = L.pop()
        if (problem.isGoalState(state)==True):
            return path
        else : 
            
            for successor, action, cost_tr in problem.getSuccessors(state):
                if successor not in visited : 
                    L.update((successor, path + [action], cost + cost_tr), cost+cost_tr)
                    visited.append(successor)

    util.raiseNotDefined()

def nullHeuristic(state:GameState, problem:SearchProblem=None)->List[Direction]:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem:SearchProblem, heuristic=nullHeuristic)->List[Direction]:
    """Search the node that has the lowest combined cost and heuristic first."""
    '''
        INSÉREZ VOTRE SOLUTION À LA QUESTION 4 ICI
    '''

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
