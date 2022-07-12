def find_next_empty(puzzle):
    # まだ埋められていない位置(-1)をボードから見つけてきて、その座標を返す
    for  r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    # 空欄がなかった場合
    return None, None

def is_valid(puzzle, guess, row, col):
    # 選んだ位置が有効かを判定する(同じ数字がないか、)

    # 行のバリデーション
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # 列のバリデーション
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # 
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    # ここまで来ればTrue
    return True

    
def solve_sudoku(puzzle):
    # パズルを進めるために場所を選ぶ
    row, col = find_next_empty(puzzle)
    # 空欄がなければ、終了
    if row is None:
        return True

    # 空欄があれば、1~9 の間で推測する。
    for guess in range(1, 10):
        # これが有効な推測かを判定
        if is_valid(puzzle, guess, row, col):
            # 有効ならその場所をその数字で埋める
            puzzle[row][col] = guess
            # 再帰
            if solve_sudoku(puzzle):
                return True

        # is_valid() が False、もしくは guess が 正しくなかった場合、やり直す
        puzzle[row][col] = -1

    # 数字がなくなった場合、解けませんでした〜
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)