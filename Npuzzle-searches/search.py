#Hugo Izquierdo
#10/12/2022
#Artificial Intelligence

from helpers import Node, NPuzzle, LEFT, RIGHT, UP, DOWN



def moveSwap(currentRow, currentColumn, move):
    if move == UP:
        nextRow = currentRow+1
        nextColumn = currentColumn
    elif move == DOWN:
        nextRow = currentRow-1
        nextColumn = currentColumn
    elif move == LEFT:
        nextRow = currentRow
        nextColumn = currentColumn+1
    elif move == RIGHT:
        nextRow = currentRow
        nextColumn = currentColumn-1
    return nextRow, nextColumn

def movesAvailable(previousMove):
        moveQ = []
        if previousMove == UP:
            moveQ = [UP, LEFT, RIGHT]
        elif previousMove == DOWN:
            moveQ = [DOWN, RIGHT, LEFT]
        elif previousMove == LEFT:
            moveQ = [UP, DOWN, LEFT]
        elif previousMove == RIGHT:
            moveQ = [UP, DOWN, RIGHT]
        elif previousMove == 'Initial':
            moveQ = [UP, LEFT, DOWN, RIGHT]
        return moveQ
    
def initialMove(currentState, currentRow, currentColumn, move):
        #isValid = False
        if currentState == 3:
            if currentRow == 0 and move == DOWN:
                return False
            elif currentColumn == 0 and move == RIGHT:
                return False
            elif currentRow == 2 and move == UP:
                return False
            elif currentColumn == 2 and move == LEFT:
                return False
            else:
                return True
            
        elif currentState == 4:
            if currentRow == 0 and move == DOWN:
                return False
            elif currentColumn == 0 and move == RIGHT:
                return False
            elif currentRow == 3 and move == UP:
                return False
            elif currentColumn == 3 and move == LEFT:
                return False
            else:
                #isValid = True
                return True
        else:
            return True
def misplaced(puzzle, puzzleSize):
    count = 0
    check = 1
    for row in range(puzzleSize):
        for col in range(puzzleSize):
            if puzzle[row][col] != check:
                if puzzle[row][col] != 0:
                    count += 1
            check += 1
            
    return count

def goalState(puzzleSize):
    goalState = NPuzzle(puzzleSize)
    return goalState

def manhattan(currentState, puzzleSize):
    goalState = NPuzzle(puzzleSize).puzzle
    currentState1 = [j for sub in currentState for j in sub]
    manhattanSum = 0
    for i, j in enumerate(currentState1):
        currentRow, currentColumn = int(i/puzzleSize), i % puzzleSize
        if j == 0:
            continue 
        else:
            for row in range(puzzleSize):
                for column in range(puzzleSize):
                    if goalState[row][column] == j:
                        goalRow, goalColumn = row, column
            manhattanSum += abs(currentRow - goalRow) + abs(currentColumn - goalColumn)
    return manhattanSum   

def BFS(puzzle):
    """
    Breadth-First Search.

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    states_searched: An ordered list of all states searched.
    final_solution: An ordered list of moves representing the final solution.
    """
    
    states_searched = [Node(puzzle)]
    final_solution = []
    
    visited = set()
    nodeQ = []
    moveQ = [UP, DOWN, LEFT, RIGHT]
    parent = Node(puzzle)
    
    visited.add(parent.state)
    currentState = states_searched[0].state
    currentRow, currentColumn = currentState.zero
    
    while moveQ:
        move = moveQ.pop(0)
        if initialMove(currentState.size, currentRow, currentColumn, move):
            newNode = Node(parent.state, parent, move)
            nextRow, nextColumn = moveSwap(currentRow, currentColumn, move)
            newNode.state.swap(currentRow, currentColumn, nextRow, nextColumn)
            nodeQ.append(newNode)
            visited.add(newNode.state)
                    
    while nodeQ:
        if final_solution:
            break
            
        parent = nodeQ.pop(0)
        states_searched.append(parent)
        moveSize = len(parent.moves)
        prevMove = parent.moves[moveSize-1]
        currentRow, currentColumn = parent.state.zero
        moveQ = movesAvailable(prevMove)
   
        while moveQ:
            move = moveQ.pop(0)
            if initialMove(currentState.size, currentRow, currentColumn, move):
                nextRow, nextColumn = moveSwap(currentRow, currentColumn, move)
                newNode = Node(parent.state, parent, move)
                newNode.state.swap(currentRow, currentColumn, nextRow, nextColumn)
                if newNode.state.check_puzzle():
                    final_solution = newNode.moves
                    states_searched.append(newNode)
                    break
                elif newNode.state in visited:
                    continue
                else:
                    nodeQ.append(newNode)
                    visited.add(newNode)
                    states_searched.append(newNode)

    return states_searched, final_solution


def DFS(puzzle):
    """
    Depth-First Search.

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    states_searched: An ordered list of all states searched.
    final_solution: An ordered list of moves representing the final solution.
    """

    states_searched = [Node(puzzle)]
    final_solution = []

    visited = set()
    nodeQ = []
    moveQ = [UP, DOWN, LEFT, RIGHT]
    parent = Node(puzzle)
    
    visited.add(parent.state)
    states_searched.append(parent.state)
    currentState = states_searched[0].state
    currentRow, currentColumn = currentState.zero
    
    while moveQ:
        move = moveQ.pop(0)
        if initialMove(currentState.size, currentRow, currentColumn, move):
            newNode = Node(parent.state, parent, move)
            nextRow, nextColumn = moveSwap(currentRow, currentColumn, move)
            newNode.state.swap(currentRow, currentColumn, nextRow, nextColumn)
            nodeQ.insert(0, newNode)
            visited.add(newNode.state)
            states_searched.append(newNode)
            
    while nodeQ: 
        if final_solution:
            break
        
        parent = nodeQ.pop()   
        moveSize = len(parent.moves)
        prevMove = parent.moves[moveSize-1]
        currentRow, currentColumn = parent.state.zero
        moveQ = movesAvailable(prevMove)
        while moveQ:
            move = moveQ.pop()
            if initialMove(currentState.size, currentRow, currentColumn, move):
                nextRow, nextColumn = moveSwap(currentRow, currentColumn, move)
                newNode = Node(parent.state, parent, move)
                newNode.state.swap(currentRow, currentColumn, nextRow, nextColumn)
                if newNode.state in visited:
                    continue
                elif newNode.depth > 50:
                    visited.add(newNode.state)
                    continue
                elif newNode.state.check_puzzle():
                    final_solution = newNode.moves
                    states_searched.append(newNode)
                    break
                else:
                    nodeQ.append(newNode)
                    visited.add(newNode.state)
                    states_searched.append(newNode)

    return states_searched, final_solution


def A_Star_H1(puzzle):
    """
    A-Star with Heuristic 1

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    states_searched: An ordered list of all states searched.
    final_solution: An ordered list of moves representing the final solution.
    """

    states_searched = [Node(puzzle)]
    final_solution = []
    
    nodeTup = []
    parent = Node(puzzle)
    puzzleSize = parent.state.size
    parentH = misplaced(parent.state.puzzle, puzzleSize)
    parentF = parentH + parent.depth
    parentTup = (parentF, parent)
    nodeTup.append(parentTup)
    visited = set()
    
    while nodeTup:

        if final_solution:
            break

        parent = nodeTup.pop(0)[1]
        states_searched.append(parent)
        visited.add(parent.state)
        moves_size = len(parent.moves)
        currentRow, currentColumn = parent.state.zero
        if moves_size == 0:
            moveQ = movesAvailable('Initial')
        else:
            prevMove = parent.moves[moves_size - 1]
            moveQ = movesAvailable(prevMove)

        while moveQ:
            move = moveQ.pop(0)
            if initialMove(puzzleSize, currentRow, currentColumn, move):
                nextRow, nextColumn = moveSwap(currentRow, currentColumn, move)
                newNode = Node(parent.state, parent, move)
                newNode.state.swap(currentRow, currentColumn, nextRow, nextColumn)
                HnewNode = misplaced(newNode.state.puzzle, puzzleSize)
                FnewNode = HnewNode + newNode.depth
                newNodeTup = (FnewNode, newNode)
                if newNode.state in visited:
                    continue
                elif puzzleSize > 3 and FnewNode > 10:
                    visited.add(newNode.state)
                    continue
                elif puzzleSize <= 3 and FnewNode > 20:
                    visited.add(newNode.state)
                    continue
                elif newNode.state.check_puzzle():
                    final_solution = newNode.moves
                    states_searched.append(newNode)
                    break
                else:
                    nodeTup.append(newNodeTup)
                    states_searched.append(newNode)
                    visited.add(newNode.state)
        nodeTup.sort(key = lambda x: x[0])

    return states_searched, final_solution


def A_Star_H2(puzzle):
    """
    A-Star with Heauristic 2

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    states_searched: An ordered list of all states searched.
    final_solution: An ordered list of moves representing the final solution.
    """

    states_searched = [Node(puzzle)]
    final_solution = []
    nodeTup = []
    parent = Node(puzzle)
    puzzleSize = parent.state.size
    parentH = manhattan(parent.state.puzzle, puzzleSize)
    parentF = parentH + parent.depth
    parentTup = (parentF, parent)
    nodeTup.append(parentTup)

    visited = set()
    
    while nodeTup:

        if final_solution:
            break

        parent = nodeTup.pop(0)[1]
        states_searched.append(parent)
        visited.add(parent.state)
        moves_size = len(parent.moves)
        currentRow, currentColumn = parent.state.zero
        if moves_size == 0:
            moveQ = movesAvailable('Initial')
        else:
            prevMove = parent.moves[moves_size - 1]
            moveQ = movesAvailable(prevMove)

        while moveQ:
            move = moveQ.pop(0)
            if initialMove(puzzleSize, currentRow, currentColumn, move):
                nextRow, nextColumn = moveSwap(currentRow, currentColumn, move)
                newNode = Node(parent.state, parent, move)
                newNode.state.swap(currentRow, currentColumn, nextRow, nextColumn)
                HnewNode = manhattan(parent.state.puzzle, puzzleSize)
                FnewNode = HnewNode + newNode.depth
                newNodeTup = (FnewNode, newNode)
                if newNode.state in visited:
                    continue
                elif puzzleSize > 3 and FnewNode > 10:
                    visited.add(newNode.state)
                    continue
                elif puzzleSize <= 3 and FnewNode > 20:
                    visited.add(newNode.state)
                    continue
                elif newNode.state.check_puzzle():
                    final_solution = newNode.moves
                    states_searched.append(newNode)
                    break
                else:
                    nodeTup.append(newNodeTup)
                    states_searched.append(newNode)
                    visited.add(newNode.state)

    return states_searched, final_solution

