def display_board(board):
    '''
    DESCRIPTION: This function prints the board with format
    INPUTS: A list which represents the board
    RETURNS: None
    '''

    print('\n' * 100)
    i = 1
    while i < len(board):
        # Board format
        print('   *   *   ')
        print(f' {board[i]} * {board[i+1]} * {board[i+2]} ')
        print('   *   *   ')
        if i < 7:
            print('************')
        
        # Index counter
        i += 3


def player_input():
    '''
    DESCRIPTION: This function assigns a marker to each player
    INPUTS: None
    RETURNS: Tuple with a marker for each player
    '''
    player1_marker = ''

    # Get a value of X or O for the player 1
    while player1_marker != 'X' and player1_marker != 'O':
        player1_marker = input('Player 1 choose between X and O: ').upper()
    
    # Assign the other value for player 2
    if player1_marker == 'X':
        player2_marker = 'O'
    else:
        player2_marker = 'X'

    # Return as a tuple for unpacking
    return (player1_marker, player2_marker)


def place_marker(board, marker, position):
    '''
    DESCRIPTION: This function takes a marker and puts it in a specified position in the board
    INPUTS: A list that represents the board, a player marker and a position
    RETURNS: None
    '''
    board[position] = marker


def win_check(board, mark):
    '''
    DESCRIPTION: This function takes a a board and a marker and checks if the player with that marker won
    INPUTS: A list that represents the board and a marker
    RETURNS: Boolean to check if a player won
    '''
    i = 1 # Rows
    j = 1 # Columns

    #----------Check main diagonal---------|-------Check inverse diagonal-------
    if board[1]==board[5]==board[9]==mark or board[3]==board[5]==board[7]==mark:
        return True
        
    while i < len(board):
        #------------------Check rows--------------|-------------Check columns--------------
        if board[i]==board[i+1]==board[i+2]==mark or board[j]==board[j+3]==board[j+6]==mark:
            return True
    
        # Update counters
        i += 3
        j += 1
    
    return False


import random

def choose_first():
    '''
    DESCRIPTION: Randomly picks a player to start the game
    INPUTS: None
    RETURNS: String representing the player who will start.
    '''

    # List of strings for each player
    player_list = ['Player 1', 'Player 2']

    # Picks one at random and returns it
    first = random.randrange(0,2)

    return player_list[first]


def space_check(board, position):
    '''
    DESCRIPTION: This function checks if there is a free space in the board comparing with a space string ' '
    INPUTS: A list that represents the board, a position
    RETURNS: Boolean value (True if space is free, False if not)
    '''
    return board[position] == ' '


def full_board_check(board):
    '''
    DESCRIPTION: This function takes a board and checks if it is full
    INPUTS: A list that represents the board
    RETURNS: Boolean value (True if full, False if not full)
    '''
    return not(' ' in board)


def player_choice(board):
    '''
    DESCRIPTION: This function takes a board and asks for player input and checks for position and free space
    INPUTS: A list that represents the board
    RETURNS: position given by player
    '''

    position = 0

    while position not in range(1,10) or not space_check(board,position):
        position = int(input('Chose your next position (1-9): '))
   
    return position


def replay():
    '''
    DESCRIPTION: This function asks user if they want to keep playing or stop the game
    INPUTS: None
    RETURNS: Boolean vale (True if input == 'Yes', False if not)
    '''

    play = ''
    while play.lower() != 'yes' and play.lower() != 'no':
        play = input('Do you want to play again? Enter Yes or No:  ')

    return play.lower() == 'yes'


def result(board, player_marker, player_name, ongoing):
    '''
    DESCRIPTION: Checks if a player won or if it is a draw and prints the results
    INPUTS: Board (as a list), Player maerker (string), Player Name (string), Ongoing (bool)
    RETURNS: Bool to check if game finished (False as a default, is a player won or if it is a draw it becomes true)
    '''

    evaluated = False
    
    # Final Result, checks if won or draw
    if win_check(board,player_marker):
        display_board(board)
        print(player_name, " wins !")
        evaluated = True
        ongoing = False


    elif full_board_check(board) and not win_check(board, player_marker):
        display_board(board)
        print("Draw !")
        evaluated = True
        ongoing = False

    return evaluated

############################# GAME ##################################
print('Welcome to Tic Tac Toe!')

while True:
    # Set up game 
    game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1, player2 = player_input()
    game_on = True
    turn = choose_first()

    while game_on:

        # Display board and the player who starts
        display_board(game_board)
        print(f'{turn}, will go first')

        # Player 1 Turn
        if turn == 'Player 1':
            # Ask for the position to put the marker
            movement = player_choice(game_board)
            # Put the marker in that position
            place_marker(game_board,player1,movement)
            # Refresh board
            display_board(game_board)
            
            # Check if won or draw
            if result(game_board,player1,'Player 1', game_on):
                break
            else:
                turn = 'Player 2'

        #  Player 2 Turn
        else:
            # Ask for the position to put the marker
            movement = player_choice(game_board)
            # Put the marker in that position
            place_marker(game_board,player2,movement)
            # Refresh board 
            display_board(game_board)

            # Check if won or draw
            if result(game_board,player2,'Player 2', game_on):
                break
            else:
                turn = 'Player 1'

    # Ask players if they want to keep playing
    if not replay():
        break
#####################################################################