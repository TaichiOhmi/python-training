"""
Tic Tac Toe class + game play implementation by Kylie Ying
YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import math
import time
from player import HumanPlayer, RandomComputerPlayer


class TicTacToe():
    def __init__(self):
        self.board = self.make_board() # 3x3のシンプルなゲームボードを作成する関数
        self.current_winner = None # 勝者を格納しておく

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]
        # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def print_board(self):
        # 行を取得
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            # row ==>>
            # self.board[0:3] = [' ', ' ', ' ']
            # self.board[3:6] = [' ', ' ', ' ']
            # self.board[6:9] = [' ', ' ', ' ']

            print('| ' + ' | '.join(row) + ' |')
            # print('| ' + ' | '.join(row) + ' |') ==>
            # |   |   |   |
            # |   |   |   |
            # |   |   |   |

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i+1) for i in range(j*3, (j+1)*3)] for j in range(3)]
        # (0*3,1*3), (1*3,2*3), (2*3, 3*3)
        # ==
        # (0,3), (3,6), (6,9)
        # ==> [['1','2','3'],['4','5','6'],['7','8','9']]

        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
            # | 1 | 2 | 3 |
            # | 4 | 5 | 6 |
            # | 7 | 8 | 9 |

    def make_move(self, square, letter):
        # もし、ゲームボードの選んだ場所が' 'なら、
        if self.board[square] == ' ':
            # 選んだ場所を プレイヤーの文字にする。
            self.board[square] = letter
            # もし、winner()が True なら、current_winner = letter(X or O) にする。
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # 行か列か斜めに３つ揃っているかを確認する

        # 行を判別する
        row_ind = math.floor(square / 3)
        # 確認する行の値のリストを取得。[' ', ' ', ' ']
        row = self.board[row_ind*3:(row_ind+1)*3]
        # その行の値が全て letter だったら、True を返す。
        # [s == ' ' for s in row] => [True, False, True]のようなリストを返す
        # all([]) で all() の引数のリスト内が全て True なら、 True を返す。
        if all([s == letter for s in row]):
            return True

        # 列を判別
        col_ind = square % 3
        # 確認する列の値のリストを取得。[' ', ' ', ' ']
        column = [self.board[col_ind+i*3] for i in range(3)]
        # その行が全て letter だったら True を返す.
        # [s == ' ' for s in col] => [True, False, True]のようなリストを返す
        # all([]) で all() の引数のリスト内が全て True なら、 True を返す。
        if all([s == letter for s in column]):
            return True

        # 斜めの判別
        # 斜めの位置に来るのは全て偶数なので、squareが偶数なら、
        if square % 2 == 0:
            # 左上から右下
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # 左上、真ん中、右下 が全て letter なら、True を返す
            if all([s == letter for s in diagonal1]):
                return True
            # 左下から右上
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # 左下、真ん中、右上 が全て letter なら、True を返す
            if all([s == letter for s in diagonal2]):
                return True
        return False

    # ゲームボードに埋まっていないマス(空白)があれば True を返す
    def empty_squares(self):
        return ' ' in self.board

    # ゲームボードに埋まっていないマス(空白)が何個あるかを返す
    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        # ゲームボードの中でまだXOではない(' ')場所のindexで構成されるリストを返す。
        return [i for i, x in enumerate(self.board) if x == " "]
        # moves = []
        # for (i, spot) in enumerate(self.board):
            # if spot == ' ':
                # moves.append(i)
        # return moves


def play(game, x_player, o_player, print_game=True):

    # print_game が True なら、ゲームボード(数字)を表示
    if print_game:
        game.print_board_nums()

    # 先行の文字
    letter = 'X'

    # ゲームボードに埋まっていないマス(空白)があれば、繰り返す
    while game.empty_squares():
        # 文字が「O」であれば、o_player.get_move(game)でプレイヤーOが埋めるマスを選択
        if letter == 'O':
            square = o_player.get_move(game)
        else:
        # 文字が「X]であれば、x_player.get_move(game)でプレイヤーXが埋めるマスを選択
            square = x_player.get_move(game)
        
        # game.make_move(場所, 文字)が Trueの時、
        if game.make_move(square, letter):
            # print_gameが True なら、
            if print_game:
                # どこを埋めるかを示し、
                print(letter + ' makes a move to square {}'.format(square+1))
                # 埋まったゲームボードを表示
                game.print_board()
                # 改行をprint()で入れる
                print('')

            # current_winner があれば(Noneじゃなければ)、
            if game.current_winner:
                # print_game が True なら、表示
                if print_game:
                    print(letter + ' の勝ち！')
                # ループ終了して、ゲームを終える
                return letter  # ends the loop and exits the game

            # ターンを交代
            letter = 'O' if letter == 'X' else 'X'  # switches player
            # if letter == 'X':
            #     letter = 'O'
            # else:
            #     letter = 'X'

        time.sleep(.8)

    # 勝者が決まることなく、ループが終わった時、
    # print_game　が　True なら、引き分け
    if print_game:
        print('引き分けでした。')



if __name__ == '__main__':
    x_player = RandomComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)