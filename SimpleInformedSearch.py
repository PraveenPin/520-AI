import random

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For Search Algorithms 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''

'''
BFS add to queue 
'''
bfs_queue = []
def add_to_queue_BFS(node_id, parent_node_id, cost, initialize=False):
    global bfs_queue
    if initialize:
        bfs_queue.append((node_id, parent_node_id))
    else:
        bfs_queue.append((node_id, parent_node_id))
    return bfs_queue

'''
BFS add to queue 
'''
def is_queue_empty_BFS():
    return len(bfs_queue) == 0

'''
BFS pop from queue
'''
def pop_front_BFS():
    (node_id, parent_node_id) = bfs_queue.pop(0)
    return (node_id, parent_node_id)

'''
DFS add to queue 
'''
dfs_queue = []
def add_to_queue_DFS(node_id, parent_node_id, cost, initialize=False):
    global dfs_queue
    if initialize:
        dfs_queue.append((node_id, parent_node_id))
    else:
        dfs_queue.append((node_id, parent_node_id))

    return dfs_queue

'''
DFS add to queue 
'''
def is_queue_empty_DFS():
    return len(dfs_queue) == 0

'''
DFS pop from queue
'''
def pop_front_DFS():
    (node_id, parent_node_id) = dfs_queue.pop()
    return (node_id, parent_node_id)

'''
UC add to queue 
'''
uc_queue = []
def add_to_queue_UC(node_id, parent_node_id, cost, initialize=False):
    global uc_queue
    start_queue = []
    end_queue = []

    if initialize:
        uc_queue.append((node_id, parent_node_id,0))
    else:
        for node_tuple in uc_queue:
            if cost > node_tuple[2]:
                start_queue.append(node_tuple)
            else:
                end_queue.append(node_tuple)

    uc_queue.clear()
    uc_queue.extend(start_queue)
    uc_queue.append((node_id, parent_node_id, cost))
    uc_queue.extend(end_queue)
    return uc_queue

'''
UC add to queue 
'''
def is_queue_empty_UC():
    return len(uc_queue) == 0

'''
UC pop from queue
'''
def pop_front_UC():
    (node_id, parent_node_id, cost) = uc_queue.pop(0)
    return (node_id, parent_node_id)

'''
A* add to queue 
'''
a_star_queue = []
def add_to_queue_ASTAR(node_id, parent_node_id, cost, initialize=False):
    global a_star_queue
    if initialize:
        a_star_queue.append((node_id, parent_node_id, 0))
    else:
        a_star_queue.append((node_id, parent_node_id, cost))
    a_star_queue.sort(key = lambda node: node[2])

    return a_star_queue


'''
A* add to queue 
'''
def is_queue_empty_ASTAR():
    return len(a_star_queue) == 0

'''
A* pop from queue
'''
def pop_front_ASTAR():
    (node_id, parent_node_id, cost) = a_star_queue.pop(0)
    return (node_id, parent_node_id)

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For n-queens problem 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''


'''
Compute a random state 
'''
def get_random_state(n):
    state = []
    for i in range(n):
        state.append(random.randint(1,n))
    return state

'''
Compute pairs of queens in conflict 
'''
def compute_attacking_pairs(state):
    number_attacking_pairs = 0
    for i in range(len(state)-1):
        for j in range(i+1,len(state)):
            if ((state[i] == state[j]) or (abs(i - j) == abs(state[i] - state[j]))):
                number_attacking_pairs+=1
    return number_attacking_pairs

'''
The basic hill-climing algorithm for n queens
'''
def hill_descending_n_queens(state, comp_att_pairs):
    final_state = state.copy()
    temp_state = state.copy()
    h = comp_att_pairs(temp_state)
    best_col_row_pair = [0,state[0]]
    for i in range(len(temp_state)):
        for j in range(1,len(temp_state)+1):
            if state[i] != j:
                temp_state[i] = j
                new_h_value = comp_att_pairs(temp_state)
                if new_h_value < h:
                    best_col_row_pair = [i, temp_state[i]]
                    h = new_h_value
        temp_state[i] = state[i]
    final_state[best_col_row_pair[0]] = best_col_row_pair[1]

    return final_state

'''
Hill-climing algorithm for n queens with restart
'''
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
    state = get_rand_st(n)
    heuristic = comp_att_pairs(state)
    while heuristic != 0:
        prev_heuristic = heuristic
        state = hill_descending(state,comp_att_pairs)
        heuristic = comp_att_pairs(state)
        if heuristic == 0:
            break
        elif(heuristic >= prev_heuristic):
            state = get_rand_st(n)
            heuristic = comp_att_pairs(state)
    return state






