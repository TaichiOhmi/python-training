"""
Tic-Tac-Toe players using inheritance implementation by Kylie YIng
YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import math
import random


class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (1-9): ')
            try:
                val = int(square)-1
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # 埋めることができるマスの数が９の時(1ターン目)はランダム
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        # それ以外の時はミニマックス法で決める
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # 前手が勝者かを確認
        if state.current_winner == other_player:
            # 前手が勝者なら、
            # 'position': None, 
            # 'score': other_playerとmax_playerが同じなら、(1*(ゲームボードの空欄の数+1))、そうでなければ、(-1*(ゲームボードの空白の数+1))
            return {'position': None, 
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
                    }
        # ゲームボードに空白がなければ、{'position': None, 'score': 0}を返す。
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        # player == max_player 時、bestは{'position': None, 'score': -math.inf(負の無限大)}
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        # player == max_player 時、bestは{'position': None, 'score': math.inf(正の無限大)}
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        # 置ける場所のリストから１つずつ出していき、
        for possible_move in state.available_moves():
            # 文字を置き換えてみて点数がどうなるか計算する
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # 置き換えた文字を元に戻し、勝者が決まった場合もやり直し、sim_scoreの'position'を今の位置にする。
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            # player == max_player の時、この位置のscoreがbest['score']より高ければ、best=sim_score
            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            # player == max_player ではない時、この位置のscoreがbest['score']より低ければ、best=sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best