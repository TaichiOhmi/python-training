import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    # print(word, word_letters, alphabet, used_letters)

    lives = 6
    
    while len(word_letters) > 0 and lives > 0:
        print('LIFE: ', '♡ ' * lives)
        print('使用済み文字: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('ターゲット: ', ' '.join(word_list))

        user_letter = input('あなたのチョイス: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('その文字は使われていません。')
        elif user_letter in used_letters:
            print('その文字は既に使用済みです。')
        else:
            print('使用不可能な文字です。')
    if lives == 0:
        print('LIFEがなくなっちゃった。。答えは「', word, '」でした！')
    else:
        print('おめでとう!!\n答えは「', word, '」でした！')

hangman()