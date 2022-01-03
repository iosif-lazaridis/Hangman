import random
import string


def word_selection(file_name):
    """
    file_name: string, the file which contains the words
    returns: a random word from words.txt file
    """
    with open(file_name, 'r') as f:
        words_list = f.read().splitlines()
        random_word = random.choice(words_list)
    return random_word


def display_word(hidden_word, guessed_letters):
    """
    hidden_word: string, the hidden word to guess
    guessed_letters: list, letters user have used
    """
    for letter in hidden_word:
        if letter in guessed_letters:
            print(letter, end='')
        else:
            print('_', end='')
    print('\n')


def win_check(hidden_word, guessed_letters):
    """
    hidden_word: string, the hidden word to guess
    guessed_letters: list, with all letters user have used
    return: boolean, True if all letters of hidden_word exist in guessed_letters otherwise False
    """
    for letter in hidden_word:
        if letter not in guessed_letters:
            return False
    return True


def letter_check(letter_guessed, guessed_letters):
    """
    letter_guessed: string, letter user have just guessed
    guessed_letters: list, with all letters user have used
    return: boolean, True if letter_guessed already exists in guessed_letters otherwise False
    """
    if letter_guessed in guessed_letters:
        return True
    return False


def is_letter_correct(letter_guessed, hidden_word):
    """
    letter_guessed: string, letter user have guessed
    hidden_word: string, the hidden word to guess
    returns: boolean, True if letter_guessed doesn't exist in hidden_word, otherwise False
    """
    if letter_guessed not in hidden_word:
        return True
    return False


def check_user_input(letter_guessed):
    """
    letter_guessed: string, letter user have guessed
    returns: boolean, True if user's input is in the correct form, otherwise False
    """
    if len(letter_guessed) != 1:  # check if input length is greater than 1
        print('Error. Please type only one letter at a time.')
        flag = False
    elif not letter_guessed.isalpha():  # check if input is a letter
        print('Error. Please type only letters.')
        flag = False
    else:
        flag = True
    return flag


def main():
    guessed_letters = []
    letters_list = list(string.ascii_lowercase)
    attempts = 8
    hidden_word = word_selection('words.txt')
    print('Welcome to Hangman game.')
    print(f'You have {attempts} lives in total.')
    print(f'The hidden word has {len(hidden_word)} letters.')
    print('-' * len(hidden_word))

    while attempts > 0:
        letter_guessed = str(input('Guess a letter: ')).lower()

        # Check user input
        while not check_user_input(letter_guessed):
            letter_guessed = str(input('Guess a letter: ')).lower()

        # Check if the letter that user guessed doesn't exist in the hidden word, and they haven't guessed it already
        if is_letter_correct(letter_guessed, hidden_word) & (not letter_check(letter_guessed, guessed_letters)):
            attempts -= 1
            print(f'Wrong letter. Guess again.You have {attempts} lives in total.')

        # Check if the letter that user guessed already exists in the guessed_letters list
        if letter_check(letter_guessed, guessed_letters):
            print('You\'ve already guessed this letter. Try another one.')
        else:
            guessed_letters.append(letter_guessed)
            letters_list.remove(letter_guessed)
            print(f'Letter {letter_guessed} exists {hidden_word.count(letter_guessed)} times in the hidden word.')

        print(f'Letters guessed: {guessed_letters}')
        print(f'Letters you can use: {letters_list}')

        # Check if the user has won
        if win_check(hidden_word, guessed_letters):
            print(f'Congratulations, you\'ve found all letters!')
            break

        display_word(hidden_word, guessed_letters)

    else:
        print(f'You lost. You ran out of lives. The word was {hidden_word}')


main()
