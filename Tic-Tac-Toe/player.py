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
        # letter は X か O が入る
        self.letter = letter

    # 次の動作を全てのプレーヤーが得られるように
    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            # 埋めたいマスを入力
            square = input(self.letter + '\'s turn. Input move (1-9): ')
            # 入力が選択可能なマスかを検証する
            try:
                val = int(square)-1
                # もし、入力した数値が available_moves() に入っていなければ、
                if val not in game.available_moves():
                    # ValueError
                    raise ValueError
                # loop を終了する
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        # 入力値を返す
        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # game.available_moves() は ゲームボードの中でまだ埋まってない場所のindexのリストを返す。
        # 埋まっていない場所のリストからランダムで場所の数字を返す。
        square = random.choice(game.available_moves())
        return square