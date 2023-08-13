def nuevo_puzzle_mover_0(move, matriz_puzzle):
    size_puzzle = 4
    if move == 1:
        p_0 = matriz_puzzle.index(0)
        p_new_0 = p_0 + 1
        p_new_num = p_0
        num_move = matriz_puzzle[p_new_0]
        matriz_puzzle[p_new_0] = 0
        matriz_puzzle[p_new_num] = num_move
        return matriz_puzzle
    elif move == -1:
        p_0 = matriz_puzzle.index(0)
        p_new_0 = p_0 - 1
        p_new_num = p_0
        num_move = matriz_puzzle[p_new_0]
        matriz_puzzle[p_new_0] = 0
        matriz_puzzle[p_new_num] = num_move
        return matriz_puzzle
    elif move == 2:
        p_0 = matriz_puzzle.index(0)
        p_new_0 = p_0 + size_puzzle if p_0 + size_puzzle > len(matriz_puzzle) else p_0 - size_puzzle
        p_new_num = p_0
        num_move = matriz_puzzle[p_new_0]
        matriz_puzzle[p_new_0] = 0
        matriz_puzzle[p_new_num] = num_move
        return matriz_puzzle
    elif move == -2:
        p_0 = matriz_puzzle.index(0)
        p_new_0 = p_0 - size_puzzle if p_0 - size_puzzle < 0 else p_0 + size_puzzle
        p_new_num = p_0
        num_move = matriz_puzzle[p_new_0]
        matriz_puzzle[p_new_0] = 0
        matriz_puzzle[p_new_num] = num_move
        return matriz_puzzle

def resolve_puzzle_n(matriz_puzzle=[], g_n=0, size_puzzle=0, target=[]):


    size_list = len(matriz_puzzle)

    if not target:
        target = list(range(1, size_list)) + [0]

    p_0 = matriz_puzzle.index(0)

    right_move = 1 if p_0 not in list(range(size_puzzle - 1, size_puzzle ** 2 + 1, size_puzzle)) else 0
    left_move = -1 if p_0 not in list(range(0, size_puzzle ** 2, size_puzzle)) else 0
    up_move = 2 if p_0 not in list(range(0, size_puzzle)) else 0
    down_move = -2 if p_0 not in list(range(size_puzzle * 3, size_puzzle ** 2)) else 0

    grafo_movimientos = {}
    for i in [left_move, right_move, up_move, down_move]:
        if i != 0:

            move_puzzle_h = nuevo_puzzle_mover_0(i, matriz_puzzle.copy())
            h_n = sum([0 if (e1 - e2) == 0 else 1 for e1, e2 in zip(target, move_puzzle_h)])
            g_n = g_n
            f_n = g_n + h_n
            grafo_movimientos.update({f_n: move_puzzle_h})
            if h_n == 0:
                break
    g_n += 1
    new_puzzle = grafo_movimientos[min(grafo_movimientos.keys())]
    print("movimiento del espacio\n", new_puzzle, "profundidad del arbol\n", g_n)
    if h_n == 0:
        return new_puzzle, g_n
    else:
      #recursion
        resolve_puzzle_n(new_puzzle, g_n=g_n, size_puzzle=size_puzzle, target=target)

if __name__ == "__main__":

    puzzle = [1,2,3,4,
              5,6,0,8,
              9,10,7,11
              ,13,14,15,12]
    print("movimiento del espacio\n", puzzle, "profundidad del arbol\n", 0)
    target = [1, 2, 3, 4,
              5, 6, 7, 8,
              9, 10, 11, 12,
              13, 14, 15, 0]
    resolve_puzzle_n(puzzle, g_n=0, size_puzzle=4,target=target)