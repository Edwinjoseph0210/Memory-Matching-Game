"""
Memory Matching Game (CLI)

Find matching pairs from a shuffled list.

Usage:
Run script and select card positions to match pairs.

"""

import random

def create_board():
    cards = list('AABBCCDDEEFF')
    random.shuffle(cards)
    return cards

def print_board(board, revealed):
    display = [c if revealed[i] else '*' for i,c in enumerate(board)]
    for i in range(0, len(display), 4):
        print(' '.join(display[i:i+4]))

def main():
    board = create_board()
    revealed = [False]*len(board)
    tries = 0
    pairs_found = 0

    while pairs_found < len(board)//2:
        print_board(board, revealed)
        try:
            pos1 = int(input("Select first card (0-11): "))
            pos2 = int(input("Select second card (0-11): "))
        except ValueError:
            print("Invalid input.")
            continue
        if pos1 == pos2 or not (0 <= pos1 < len(board)) or not (0 <= pos2 < len(board)):
            print("Invalid positions.")
            continue
        if revealed[pos1] or revealed[pos2]:
            print("Card already revealed.")
            continue

        tries += 1
        if board[pos1] == board[pos2]:
            print("Match found!")
            revealed[pos1] = revealed[pos2] = True
            pairs_found += 1
        else:
            print("Try again.")

    print(f"Congratulations! You found all pairs in {tries} tries.")

if __name__ == "__main__":
    main()
