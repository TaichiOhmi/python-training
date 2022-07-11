import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # ゲームボード作成
        self.board = self.make_new_board()
        self.assign_values_to_board()

        # (行, 列)の tuples を入れる
        self.dug = set()

    def make_new_board(self):
        # 新しいゲームボードを dim_size と num_bombs を基に作成。

        # dim_size x dim_size の list of lists を作成
        board = [[None for _ in range(self.dim_size)] for  _ in range(self.dim_size)]

        # 爆散を置く
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1) # 0以上, dim_sizeの二乗未満の整数を返す。
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue

            board[row][col] = '*'
            bombs_planted += 1
    
        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                # 既に爆弾が置いてある場合、はスルー
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row ,col):
        num_neighboring_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    # もともとの位置はスルー
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs

    def dig(self, row, col):
        # 成功すればTrue, 失敗すればFalse
        # 爆弾に当たればゲームオーバー
        # 爆弾の隣を掘ったら掘るのを止める
        # 爆弾の隣でなかったら掘り続ける

        self.dug.add((row, col)) # 掘った場所は記録

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row - 1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue # 既に掘ってあるところはスルー
                self.dig(r, c)
        
        return True

    def __str__(self):
        # magic function
        # print()をこのオブジェクト内で呼び出した時、この関数の出力が表示される
        # 今回はゲームボードを示す文字列を表示させる。

        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
            

def play(dim_size=10, num_bombs=10):
    # 手順１：ゲームボードを作成し、爆弾を埋める
    board = Board(dim_size, num_bombs)
    # 手順２：ゲームボードを表示し、どこを掘るかを聞く
    # 手順３_a：掘った場所に爆弾があれば、ゲームオーバー
    # 手順３_b：爆弾がなければ、再帰的に、少なくとも爆弾の隣にあるマスまで掘る
    # 手順４：手順２と手順３を繰り返す。掘る場所がなくなれば、勝利。
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        # 0,0 or 0, 0 or 0,   0
        user_input = re.split(',(\\s)*', input('どこを進む？(row, col): '))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print('Invalid location. Try again.')
            continue

        # if it's valid, we dig
        safe = board.dig(row, col)
        if not safe:
            break # ゲームオーバー

    if safe:
        print('ゲームクリア！')
    else:
        print('ゲームオーバー！')
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__=='__main__':
    play()


