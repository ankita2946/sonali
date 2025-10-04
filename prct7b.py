board=[ ' ' for _ in range (9)]
player='X'
def show_board():
    print(f' | {board[0]} | {board[1]} | {board[2]} | ')
    print("------------------------")
    print(f' | {board[3]} | {board[4]} | {board[5]}| ')
    print("------------------------")
    print(f' | {board[6]} | {board[7]} | {board[8]} | ')
    print("------------------------")

def is_Winner(p):
    return(
        (board[0]==p and board[1]==p and board[2]==p) or
        (board[3]==p and board[4]==p and board[5]==p) or
        (board[6]==p and board[7]==p and board[8]==p) or
        (board[0]==p and board[3]==p and board[6]==p) or
        (board[1]==p and board[4]==p and board[7]==p) or
        (board[2]==p and board[5]==p and board[8]==p) or
        (board[0]==p and board[4]==p and board[8]==p) or
        (board[2]==p and board[4]==p and board[6]==p) )
def is_tie():
    return ' ' not in board
def game():
    global player
    while True:
        show_board()
        try:
            move=int(input(f"Player{player} Enter 0-8:"))
            if 0<=move<=8 and board[move]==' ':
                board[move]=player
                if is_Winner(player):
                    show_board()
                    print(f"Player {player} Wins!")
                    break
                elif is_tie():
                    show_board()
                    print("It's a tie!")
                    break
                else:
                    if player=="X":
                        player="O"
                    else:
                        player="X"
            else:
                print("Invalid Move")
        except(ValueError,IndexError):
            print("Invalid input . Enter a Number 0-8")
game()               
                         
                      











        
