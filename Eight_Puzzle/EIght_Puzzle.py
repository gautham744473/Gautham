from copy import deepcopy
import numpy as np
import time

# takes the input of current states and evaluates the best path to goal state
def Optimal_solution(state):
    Optimal = np.array([], int).reshape(-1, 9)
    count = len(state) - 1
    while count != -1:
        Optimal = np.insert(Optimal, 0, state[count]['puzzle'], 0)
        count = (state[count]['parent'])
    return Optimal.reshape(-1, 3, 3)


# this function checks for the uniqueness of the iteration(it) state, weather it has been previously traversed or not.
def all(check_array):
    set=[]
    for it in set:
        for check_array in it:
            return 1
        else:
            return 0

#############################################################################################


# calculate Manhattan distance cost between each digit of puzzle(start state) and the goal state
def manhattan_distance(puzzle, goal):
    l = abs(puzzle // 3 - goal // 3)
    m = abs(puzzle % 3 - goal % 3)
    manhattan_cost = l + m
    return sum(manhattan_cost[1:])




# will calcuates the number of misplaced tiles in the current state as compared to the goal state
def misplaced_tiles(puzzle,goal):
    misplaced_cost = np.sum(puzzle != goal) - 1
    return misplaced_cost if misplaced_cost > 0 else 0



#3[on_true] if [expression] else [on_false]


# will indentify the coordinates of each of goal or initial state values
def coordinates(puzzle):
    position = np.array(range(9))
    for a, b in enumerate(puzzle):
        position[b] = a
    return position



# start of 8 puzzle evaluvation, using Manhattan heuristics


def Manhattan_evaluate(puzzle, goal):
    steps = np.array([('up', [0, 1, 2], -3),('down', [6, 7, 8],  3),('left', [0, 3, 6], -1),('right', [2, 5, 8],  1)],
                dtype =  [('move',  str, 1),('position', list),('head', int)])

    dtstate = [('puzzle',  list),('parent', int),('gn',  int),('hn',  int)]

     # initializing the parent, gn and hn, where hn is manhattan distance function call
    step_cost = coordinates(goal)
    parent = -1
    gn = 0
    hn = manhattan_distance(coordinates(puzzle), step_cost)
    state = np.array([(puzzle, parent, gn, hn)], dtstate)

# We make use of priority queues with position as keys and fn as value.
    dtpriority = [('position', int),('fn', int)]
    priority = np.array( [(0, hn)], dtpriority)



    while True:
        priority = np.sort(priority, kind='mergesort', order=['fn', 'position'])
        position, fn = priority[0]
        priority = np.delete(priority, 0, 0)
        # sort priority queue using merge sort,the first element is picked for exploring remove from queue what we are exploring
        puzzle, parent, gn, hn = state[position]
        puzzle = np.array(puzzle)
        # Identify the blank square in input
        blank = int(np.where(puzzle == 0)[0])
        gn = gn + 1
        c = 1
        start_time = time.time()
        for s in steps:
            c = c + 1
            if blank not in s['position']:
                # generate new state as copy of current
                openstates = deepcopy(puzzle)
                openstates[blank], openstates[blank + s['head']] = openstates[blank + s['head']], openstates[blank]
                # The all function is called, if the node has been previously explored or not
                if ~(np.all(list(state['puzzle']) == openstates, 1)).any():
                    end_time = time.time()
                    if (( end_time - start_time ) > 2):
                        print(" The 8 puzzle is unsolvable ! \n")
                        exit
                    # calls the manhattan function to calcuate the cost
                    hn = manhattan_distance(coordinates(openstates), step_cost)
                     # generate and add new state in the list
                    b = np.array([(openstates, position, gn, hn)], dtstate)
                    state = np.append(state, b, 0)
                    # f(n) is the sum of cost to reach node and the cost to rech fromt he node to the goal state
                    fn = gn + hn

                    b = np.array([(len(state) - 1, fn)], dtpriority)
                    priority = np.append(priority, b, 0)
                      # Checking if the node in openstates are matching the goal state.
                    if np.array_equal(openstates, goal):
                        print(' The 8 puzzle is solvable ! \n')
                        return state, len(priority)


    return state, len(priority)


# start of 8 puzzle evaluvation, using Misplaced tiles heuristics
def Misplaced_evaluate(puzzle, goal):
    steps = np.array([('up', [0, 1, 2], -3),('down', [6, 7, 8],  3),('left', [0, 3, 6], -1),('right', [2, 5, 8],  1)],
                dtype =  [('move',  str, 1),('position', list),('head', int)])

    dtstate = [('puzzle',  list),('parent', int),('gn',  int),('hn',  int)]

    costg = coordinates(goal)
    # initializing the parent, gn and hn, where hn is misplaced_tiles  function call
    parent = -1
    gn = 0
    hn = misplaced_tiles(coordinates(puzzle), costg)
    state = np.array([(puzzle, parent, gn, hn)], dtstate)

   # We make use of priority queues with position as keys and fn as value.
    dtpriority = [('position', int),('fn', int)]

    priority = np.array([(0, hn)], dtpriority)

    while True:
        priority = np.sort(priority, kind='mergesort', order=['fn', 'position'])
        position, fn = priority[0]
        # sort priority queue using merge sort,the first element is picked for exploring.
        priority = np.delete(priority, 0, 0)
        puzzle, parent, gn, hn = state[position]
        puzzle = np.array(puzzle)
         # Identify the blank square in input
        blank = int(np.where(puzzle == 0)[0])
        # Increase cost g(n) by 1
        gn = gn + 1
        c = 1
        start_time = time.time()
        for s in steps:
            c = c + 1
            if blank not in s['position']:
                 # generate new state as copy of current
                openstates = deepcopy(puzzle)
                openstates[blank], openstates[blank + s['head']] = openstates[blank + s['head']], openstates[blank]
                # The check function is called, if the node has been previously explored or not.
                if ~(np.all(list(state['puzzle']) == openstates, 1)).any():
                    end_time = time.time()
                    if (( end_time - start_time ) > 2):
                        print(" The 8 puzzle is unsolvable \n")
                        break
                    # calls the Misplaced_tiles function to calcuate the cost
                    hn = misplaced_tiles(coordinates(openstates), costg)
                    # generate and add new state in the list
                    b = np.array([(openstates, position, gn, hn)], dtstate)
                    state = np.append(state, b, 0)
                    # f(n) is the sum of cost to reach node and the cost to rech fromt he node to the goal state
                    fn = gn + hn

                    b = np.array([(len(state) - 1, fn)], dtpriority)
                    priority = np.append(priority, b, 0)
                    # Checking if the node in openstates are matching the goal state.
                    if np.array_equal(openstates, goal):
                        print('  8 puzzle is solvable \n')
                        return state, len(priority)

    return state, len(priority)

class Execution:

    def heuristic_method(self,puzzle,goal):
        n = int(input("1. Manhattan distance \n \t 2. Misplaced tiles \t"))

        if(n ==1):
            state, Expanded = Manhattan_evaluate(puzzle, goal)
            Optimal_path = Optimal_solution(state)
            print(str(Optimal_path).replace('[', ' ').replace(']', ''))
            expand = len(state) - Expanded
            print('Total nodes Expanded: ',expand, "\n")
            print('Total nodes Generated:', len(state))

        if(n == 2):
            state, Expanded = Misplaced_evaluate(puzzle, goal)
            Optimal_path = Optimal_solution(state)
            print(str(Optimal_path).replace('[', ' ').replace(']', ''))
            expand = len(state) - Expanded
            print('Total nodes Expanded: ',expand, "\n")
            print('Total nodes Generated:', len(state))


# ----------  Program Execution Starts  -----------------

def main():

# User input for initial state
    puzzle = []
    print("Enter Input values from 0-8 for Initial/Start state ")
    for i in range(0,9):
        x = int(input(f"Enter {i+1 } values : "))
        puzzle.append(x)

 # User input of goal state
    goal = []
    print("Enter Input values from 0-8 for Goal/Final state ")
    for i in range(0,9):
        x = int(input(f"Enter {i+1 }  values : "))
        goal.append(x)


    object1=Execution()    #Object Creation
    object1.heuristic_method(puzzle,goal)

if __name__ == main():
    main()
