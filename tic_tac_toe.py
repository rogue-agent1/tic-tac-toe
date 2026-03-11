#!/usr/bin/env python3
"""Tic-tac-toe — unbeatable AI using minimax."""
import sys
def check_win(b, p):
    lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[a]==b[c]==b[d]==p for a,c,d in lines)
def minimax(b, is_max):
    if check_win(b, 'X'): return 1
    if check_win(b, 'O'): return -1
    if ' ' not in b: return 0
    best = -2 if is_max else 2
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'X' if is_max else 'O'
            score = minimax(b, not is_max)
            b[i] = ' '
            best = max(best, score) if is_max else min(best, score)
    return best
def best_move(b):
    best = -2; move = -1
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'X'; score = minimax(b, False); b[i] = ' '
            if score > best: best = score; move = i
    return move
def render(b):
    for i in range(0, 9, 3):
        print(f"  {b[i]}|{b[i+1]}|{b[i+2]}")
        if i < 6: print("  -+-+-")
if __name__ == "__main__":
    b = [' ']*9
    print("Tic-tac-toe: You=O, AI=X")
    while True:
        m = best_move(b); b[m] = 'X'; render(b)
        if check_win(b, 'X'): print("AI wins!"); break
        if ' ' not in b: print("Draw!"); break
        while True:
            try: m = int(input("Your move (0-8): "))
            except (ValueError, EOFError): m = [i for i in range(9) if b[i]==' '][0]
            if 0 <= m < 9 and b[m] == ' ': break
        b[m] = 'O'
        if check_win(b, 'O'): render(b); print("You win!"); break
