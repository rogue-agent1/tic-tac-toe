#!/usr/bin/env python3
"""Tic-tac-toe with perfect minimax AI."""
def new_board(): return [" "]*9
def check_win(b,p):
    wins=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[a]==b[bb]==b[c]==p for a,bb,c in wins)
def is_full(b): return " " not in b
def minimax(b,is_max):
    if check_win(b,"X"): return 1
    if check_win(b,"O"): return -1
    if is_full(b): return 0
    if is_max:
        best=-2
        for i in range(9):
            if b[i]==" ": b[i]="X";best=max(best,minimax(b,False));b[i]=" "
        return best
    else:
        best=2
        for i in range(9):
            if b[i]==" ": b[i]="O";best=min(best,minimax(b,True));b[i]=" "
        return best
def best_move(b,player="X"):
    is_max=player=="X";best_val=-2 if is_max else 2;best_i=-1
    for i in range(9):
        if b[i]!=" ":continue
        b[i]=player;val=minimax(b,not is_max);b[i]=" "
        if (is_max and val>best_val) or (not is_max and val<best_val): best_val=val;best_i=i
    return best_i
if __name__=="__main__":
    b=new_board();b[4]="X"
    m=best_move(b,"O");print(f"O plays: {m} (corner expected)")
    assert m in [0,2,6,8]
    b=new_board()
    for turn in range(9):
        p="X" if turn%2==0 else "O"
        m=best_move(b,p);b[m]=p
    assert not check_win(b,"X") and not check_win(b,"O")
    print("Perfect play = draw"); print("Tic-tac-toe OK")
