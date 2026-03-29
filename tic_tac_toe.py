#!/usr/bin/env python3
"""tic_tac_toe - Tic-tac-toe with AI."""
import sys,argparse,json
def check_win(b,p):
    lines=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[a]==b[bb]==b[c]==p for a,bb,c in lines)
def minimax(b,is_max):
    if check_win(b,"X"):return -1
    if check_win(b,"O"):return 1
    if " " not in b:return 0
    best=-2 if is_max else 2
    for i in range(9):
        if b[i]==" ":
            b[i]="O" if is_max else "X"
            val=minimax(b,not is_max)
            b[i]=" "
            best=max(best,val) if is_max else min(best,val)
    return best
def best_move(b):
    best_val=-2;best_i=0
    for i in range(9):
        if b[i]==" ":
            b[i]="O";val=minimax(b,False);b[i]=" "
            if val>best_val:best_val=val;best_i=i
    return best_i
def render(b):
    return f" {b[0]} | {b[1]} | {b[2]} \n---+---+---\n {b[3]} | {b[4]} | {b[5]} \n---+---+---\n {b[6]} | {b[7]} | {b[8]} "
def main():
    p=argparse.ArgumentParser(description="Tic-tac-toe")
    p.add_argument("--simulate",type=int,default=1)
    args=p.parse_args()
    import random;results={"X":0,"O":0,"draw":0}
    for _ in range(args.simulate):
        b=[" "]*9;turn="X"
        while " " in b:
            if turn=="O":i=best_move(b)
            else:empty=[i for i in range(9) if b[i]==" "];i=random.choice(empty)
            b[i]=turn
            if check_win(b,turn):results[turn]+=1;break
            turn="O" if turn=="X" else "X"
        else:results["draw"]+=1
    print(json.dumps({"games":args.simulate,"results":results},indent=2))
if __name__=="__main__":main()
