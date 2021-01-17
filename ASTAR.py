# Each child nodes of every parent and the distance cost between them.
tree = {'S': [['A', 1], ['B', 5], ['C', 8]],
        'A': [['S', 1], ['D', 3], ['E', 7], ['G', 9]],
        'B': [['S', 5], ['G', 4]],
        'C': [['S', 8], ['G', 5]],
        'D': [['A', 3]],
        'E': [['A', 7]]}

# Heuristic function of each node
heuristic = {'S': 8, 'A': 8, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'G': 0}

cost = {'S': 0}             # total cost for nodes visited


def AStarSearch():
    global tree, heuristic

    frontier = [['S', 8]]     # nodes in frontier
    explored = []             # explored nodes

    # find the explored nodes
    while True:
        fn = [i[1] for i in frontier]            # fn = g(n) + h(n)
        chosen_index = fn.index(min(fn))
        node = frontier[chosen_index][0]  # current node
        explored.append(frontier[chosen_index])
        del frontier[chosen_index]

        if explored[-1][0] == 'G':
            break

        for item in tree[node]:
            if item[0] in [explored_item[0] for explored_item in explored]:
                continue
            # add nodes to cost dictionary
            cost.update({item[0]: cost[node] + item[1]})
            fn_node = cost[node] + heuristic[item[0]] + \
                item[1]  # f(n) of current node
            temp = [item[0], fn_node]
            frontier.append(temp)

    # find optimal sequence
    goal_node = 'G'
    optimal_sequence = ['G']               # optimal node sequence
    for i in range(len(explored)-2, -1, -1):
        check_node = explored[i][0]           # current node
        if goal_node in [children[0] for children in tree[check_node]]:
            children_costs = [temp[1] for temp in tree[check_node]]
            children_nodes = [temp[0] for temp in tree[check_node]]

            # check whether h(s) + g(s) = f(s). If so, append current node to optimal sequence, change the correct optimal tracing node to current node
            if cost[check_node] + children_costs[children_nodes.index(goal_node)] == cost[goal_node]:
                optimal_sequence.append(check_node)
                goal_node = check_node
    optimal_sequence.reverse()              # reverse the optimal sequence
    return explored, optimal_sequence


if __name__ == '__main__':
    explored_nodes, optimal_nodes = AStarSearch()
    print('Explored Nodes: ' + str(explored_nodes))
    print('Optimal Nodes Sequence: ' + str(optimal_nodes))
    print('Optimal Cost to reach every node: ' + str(cost))
