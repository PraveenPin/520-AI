"""
Compute the value brought by a given move by placing a new token for player
at (row, column). The value is the number of opponent pieces getting flipped
by the move. 

A move is valid if for the player, the location specified by (row, column) is
(1) empty and (2) will cause some pieces from the other player to flip. The
return value for the function should be the number of pieces hat will be moved.
If the move is not valid, then the value 0 (zero) should be returned. Note
here that row and column both start with index 0. 
"""
import copy,math


def get_move_value(state, player, row, column):
    flipped = 0
    if row == -1 or column == -1 or row >= len(state) or column >= len(state):
        return flipped
    # Your implementation goes here
    opp_player = "W" if player == "B" else "B"
    i = row - 1
    j=column
    while(i>=0):
        if(state[i][j] == opp_player):
            i-=1
        elif (state[i][j] == player):
            flipped += row - i-1
            break
        else:
            break

    i = row + 1
    while(i< len(state)):
        if(state[i][j] == opp_player):
            i+=1
        elif (state[i][j] == player):
            flipped += i-row-1
            break
        else:
            break

    i = row
    j = column - 1
    while (j >= 0):
        if (state[i][j] == opp_player):
            j -= 1
        elif (state[i][j] == player):
            flipped += column - j-1
            break
        else:
            break

    j = column + 1
    while (j < len(state)):
        if (state[i][j] == opp_player):
            j += 1
        elif (state[i][j] == player):
            flipped += j - column-1
            break
        else:
            break

    i = row - 1
    j = column - 1
    while(i>=0 and j>=0):
        if( state[i][j] == opp_player):
            i-=1
            j-=1
        elif (state[i][j] == player):
            flipped += row - i-1
            break
        else:
            break

    i = row + 1
    j = column + 1
    while(i < len(state) and j< len(state)):
        if(state[i][j] == opp_player):
            i+=1
            j+=1
        elif(state[i][j] == player):
            flipped += i - row-1
            break
        else:
            break

    i = row + 1
    j = column - 1
    while(i < len(state) and j>=0):
        if( state[i][j] == opp_player):
            i+=1
            j-=1
        elif (state[i][j] == player):
            flipped += i-row-1
            break
        else:
            break

    i = row - 1
    j = column + 1
    while(i >=0 and j< len(state)):
        if(state[i][j] == opp_player):
            i-=1
            j+=1
        elif(state[i][j] == player):
            flipped += row-i-1
            break
        else:
            break

    return flipped


"""
Execute a move that updates the state. A new state should be crated. The move
must be valid. Note that the new state should be a clone of the old state and
in particular, should not share memory with the old state. 
"""
def execute_move(state, player, row, column):
    # Your implementation goes here
    new_state = copy.deepcopy(state)
    new_state[row][column] = player

    opp_player = "W" if player == "B" else "B"
    if row == -1 or column == -1 or row >= len(state) or column >= len(state):
        return state
    flipped = 0
    i = row - 1
    j=column
    while(i>=0):
        if(state[i][j] == opp_player):
            i-=1
        elif (state[i][j] == player):
            flipped += row - i-1
            break
        else:
            break

    if not flipped == 0:
        k = row
        while k >= i:
            new_state[k][j] = player
            k-=1

    flipped = 0
    i = row + 1
    while(i< len(state)):
        if(state[i][j] == opp_player):
            i+=1
        elif (state[i][j] == player):
            flipped += i-row-1
            break
        else:
            break

    if not flipped == 0:
        k = i
        while k >= row:
            new_state[k][j] = player
            k-=1

    i = row
    j = column - 1
    flipped = 0
    while (j >= 0):
        if (state[i][j] == opp_player):
            j -= 1
        elif (state[i][j] == player):
            flipped += column - j-1
            break
        else:
            break

    if not flipped == 0:
        k = column
        while k >= j:
            new_state[i][k] = player
            k-=1

    flipped=0
    j = column + 1
    while (j < len(state)):
        if (state[i][j] == opp_player):
            j += 1
        elif (state[i][j] == player):
            flipped += j - column-1
            break
        else:
            break

    if not flipped == 0:
        k = j
        while k >= column:
            new_state[i][k] = player
            k-=1

    flipped=0
    i = row - 1
    j = column - 1
    while(i>=0 and j>=0):
        if( state[i][j] == opp_player):
            i-=1
            j-=1
        elif (state[i][j] == player):
            flipped += row - i-1
            break
        else:
            break

    if not flipped == 0:
        p,q = row,column
        while q >= j and p >= i:
            new_state[p][q] = player
            p-=1
            q-=1

    flipped=0
    i = row + 1
    j = column + 1
    while(i < len(state) and j< len(state)):
        if(state[i][j] == opp_player):
            i+=1
            j+=1
        elif(state[i][j] == player):
            flipped += i - row-1
            break
        else:
            break

    if not flipped == 0:
        p,q = i,j
        while q >= column and p >= row:
            new_state[p][q] = player
            p-=1
            q-=1

    flipped=0
    i = row + 1
    j = column - 1
    while(i < len(state) and j>=0):
        if( state[i][j] == opp_player):
            i+=1
            j-=1
        elif (state[i][j] == player):
            flipped += i-row-1
            break
        else:
            break

    if not flipped == 0:
        p,q = i,j
        while q >= j and p >= row:
            new_state[p][q] = player
            p-=1
            q+=1

    flipped=0
    i = row - 1
    j = column + 1
    while(i >=0 and j< len(state)):
        if(state[i][j] == opp_player):
            i-=1
            j+=1
        elif(state[i][j] == player):
            flipped += row-i-1
            break
        else:
            break

    if not flipped == 0:
        p,q = i,j
        while q >= column and p >= i:
            new_state[p][q] = player
            p+=1
            q-=1

    return new_state


"""
A method for counting the pieces owned by the two players for a given state. The
return value should be two tuple in the format of (blackpeices, white pieces), e.g.,

    return (4, 3)

"""


def count_pieces(state):
    blackpieces = 0
    whitepieces = 0
    # Your implementation goes here
    for i in range(len(state)):
        for j in range(len(state)):
            if( state[i][j] == "B"):
                blackpieces+=1
            elif state[i][j] == "W":
                whitepieces+=1

    return (blackpieces, whitepieces)


"""
Check whether a state is a terminal state. 
"""


def is_terminal_state(state, state_list=None):
    terminal = True
    # Your implementation goes here
    for i in range(len(state)):
        for j in range(len(state)):
            if(state[i][j] == ' ' and (get_move_value(state, "B", i, j) !=0 or get_move_value(state,"W",i,j) !=0 )):
                terminal = False
                break
    return terminal

def getSuccessorMoves(state,player):
    successors = []
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == " " and get_move_value(state,player,i,j) !=0:
                successors.append([i,j])
    return successors
"""
The minimax algorithm. Your implementation should return the best value for the
given state and player, as well as the next immediate move to take for the player. 
"""
top_level = 0
terminal_state_count = 0
total_terminal_state_count = 0
def minimax_value(state,turn,player):
    global top_level,terminal_state_count,total_terminal_state_count
    opp_player = "W" if player == "B" else "B"
    # Your implementation goes here
    (blacks, whites) = count_pieces(state)
    value = blacks-whites
    if is_terminal_state(state):
        if top_level:
            terminal_state_count+=1
        total_terminal_state_count+=1
        # heuristic
        return value if turn == "B" else -value
    value = math.inf if turn != player else -math.inf
    children = getSuccessorMoves(state,player)
    if len(children) == 0:
        return minimax_value(state,turn,opp_player)
    else:
        for child in children:
            temp_val = minimax_value(execute_move(state,player,child[0],child[1]),turn,opp_player)
            if turn == player:
                if temp_val > value:
                    value = temp_val
            else:
                if temp_val < value:
                    value = temp_val

    return value

def minimax(state,player):
    global top_level,terminal_state_count,total_terminal_state_count
    value = -math.inf
    row = -1
    column = -1
    opp_player = "W" if player == "B" else "B"
    # Your implementation goes here
    children = getSuccessorMoves(state,player)
    if len(children)!=0:
        row = children[0][0]
        column = children[0][1]
        for child in children:
           temp_val = minimax_value(execute_move(state,player,child[0],child[1]),player,opp_player)
           if value < temp_val:
               value = temp_val
               row = child[0]
               column = child[1]
    else:
        if top_level:
            terminal_state_count = 1
        total_terminal_state_count = 1
    if player == "B":
        return value, row, column
    else:
        return -value, row, column

"""
This method should call the minimax algorithm to compute an optimal move sequence
that leads to an end game. 
"""

def full_minimax(state, player):
    value = 0
    move_sequence = []
    turn = player
    is_optimal = 0
    global top_level,terminal_state_count,total_terminal_state_count
    top_level = 1
    terminal_state_count = 0
    total_terminal_state_count = 0
    # Your implementation goes here
    while not is_terminal_state(state):
        (val, row, column) = minimax(state,turn)
        if top_level:
            top_level = 0
        if not (row == -1 and column == -1):
            move_sequence.append((turn, row, column))
        state = execute_move(state, turn, row, column)
        if not is_optimal:
            value = val
            is_optimal = 1
        turn = "W" if turn == "B" else "B"
    # move_sequence.append([turn,-1,-1])
    return (value, move_sequence)


"""
The minimax algorithm with alpha-beta pruning. Your implementation should return the
best value for the given state and player, as well as the next immediate move to take
for the player. 
"""

top_level_ab = 0
terminal_state_count_ab= 0
total_terminal_state_count_ab = 0
truncation = 0
def minimax_value_ab(state,turn,player,alpha,beta):
    global top_level_ab,terminal_state_count_ab,total_terminal_state_count_ab,truncation
    opp_player = "W" if player == "B" else "B"
    # Your implementation goes here
    (blacks, whites) = count_pieces(state)
    value = blacks-whites
    if is_terminal_state(state):
        # heuristic
        if top_level_ab :
            terminal_state_count_ab+= 1
        total_terminal_state_count_ab+=1
        return value if turn == "B" else -value
    value = math.inf if turn != player else -math.inf
    children = getSuccessorMoves(state,player)
    if len(children) == 0:
        return minimax_value_ab(state,turn,opp_player,alpha,beta)
    else:
        for child in children:
            temp_val = minimax_value_ab(execute_move(state,player,child[0],child[1]),turn,opp_player,alpha,beta)
            if turn == player:
                if temp_val > value:
                    value = temp_val
                    if value >= beta:
                        truncation+=1
                        return value
                    if alpha < value:
                        alpha = value
            else:
                if temp_val < value:
                    value = temp_val
                    if value <= alpha:
                        truncation+=1
                        return value
                    if beta > value:
                        beta = value

    return value


def minimax_ab(state, player, alpha=-10000000, beta=10000000):
    global top_level_ab, terminal_state_count_ab, total_terminal_state_count_ab
    value = -math.inf
    row = -1
    column = -1
    opp_player = "W" if player == "B" else "B"
    # Your implementation goes here
    children = getSuccessorMoves(state,player)
    if len(children)!=0:
        row = children[0][0]
        column = children[0][1]
        for child in children:
           temp_val = minimax_value_ab(execute_move(state,player,child[0],child[1]),player,opp_player,alpha,beta)
           if value < temp_val:
                value = temp_val
                row = child[0]
                column = child[1]
    else:
        if top_level_ab: terminal_state_count_ab=1
        total_terminal_state_count_ab=1
    if player == "B":
        return value, row, column
    else:
        return -value, row, column

"""
This method should call the minimax_ab algorithm to compute an optimal move sequence
that leads to an end game, using alpha-beta pruning.
"""


def full_minimax_ab(state, player):
    value = 0
    is_optimal = 0
    move_sequence = []
    turn = player
    global top_level_ab,terminal_state_count_ab,total_terminal_state_count_ab,truncation
    # Your implementation goes here
    top_level_ab = 1
    terminal_state_count_ab=0
    total_terminal_state_count_ab = 0
    truncation = 0
    while not is_terminal_state(state):
        (val, row, column) = minimax_ab(state,turn)
        top_level_ab = 0
        if not (row == -1 and column == -1):
            move_sequence.append((turn, row, column))
        state = execute_move(state,turn,row,column)
        if not is_optimal:
            is_optimal = 1
            value = val
        turn = "W" if turn == "B" else "B"
    return (value, move_sequence)
