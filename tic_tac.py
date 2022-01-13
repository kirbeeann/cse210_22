def main():
    
    
    

        player = next_player("")
        the_board = create_board()
        while not (winner(the_board) or tie(the_board)):
            display_board(the_board)
            make_move(player, the_board)
            player = next_player(player)
        display_board(the_board)
        print("Good game fellas.")
        print()
        

        
def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

    
def tie(board):
    for i in range(9):
        if board[i] != "x" and board[i] != "o":
            return False
    return True 




def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('____')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('____')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()
    
def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"
    

    
           
   
main()   
    
    
if __name__ == "__main__":
    main