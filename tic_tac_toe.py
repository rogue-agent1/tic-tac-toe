#!/usr/bin/env python3
"""Terminal tic-tac-toe with AI opponent."""
import sys, random

def new_board(): return [' ']*9

def show(b):
    for i in range(3):
        print(f" {b[i*3]} │ {b[i*3+1]} │ {b[i*3+2]} ")
        if i < 2: print("───┼───┼───")

def winner(b):
    lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,c,d in lines:
        if b[a] == b[c] == b[d] != ' ': return b[a]
    return None

def minimax(b, is_max):
    w = winner(b)
    if w == 'O': return 1
    if w == 'X': return -1
    if ' ' not in b: return 0
    best = -2 if is_max else 2
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O' if is_max else 'X'
            score = minimax(b, not is_max)
            b[i] = ' '
            best = max(best, score) if is_max else min(best, score)
    return best

def ai_move(b):
    best_score, best_move = -2, 0
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O'
            score = minimax(b, False)
            b[i] = ' '
            if score > best_score: best_score, best_move = score, i
    return best_move

def play():
    b = new_board()
    print("You are X. Enter 1-9:\n")
    show(b)
    while True:
        try: move = int(input("\nYour move: ")) - 1
        except (ValueError, EOFError): continue
        if not (0 <= move < 9) or b[move] != ' ': print("Invalid!"); continue
        b[move] = 'X'
        if winner(b): show(b); print("\nYou win! 🎉"); return
        if ' ' not in b: show(b); print("\nDraw!"); return
        b[ai_move(b)] = 'O'
        show(b)
        if winner(b): print("\nAI wins! 🤖"); return
        if ' ' not in b: print("\nDraw!"); return

if __name__ == '__main__':
    play()
