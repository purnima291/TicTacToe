from IPython.display import clear_output
#Global list for new position and occupied postion
op = ['w']
b = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def tictac():
    instruction()
    global op
    while True:
        p, q = player_input()
        in_game(p, q)
        ans = 'x'
        while ans.upper() not in ['Y','N']:
            ans = input('Do you want to replay the game, press y if yes or n if no: ')
        if ans.upper() == 'Y':
            b[1:] = ' '*9
            op = ['w']
            continue
        else:
            b[1:] = ' '*9
            op = ['w']
            break

def instruction():
    print('!Welcome to TicTacToe Game!')
    print('\nThis is a two player game. Player 1 will select \'X\' or \'O\'.')
    print('To place the marker in nine respective positions of board, player has to press number from 1 to 9')
    print('Each number corresponds to each position on board as shown below:\n')
    print(' 7 | 8 | 9 ')
    print('-----------')
    print(' 4 | 5 | 6 ')
    print('-----------')
    print(' 1 | 2 | 3 ')

def player_input():
    #PLAYERS SHOULD SELECT EITHER 'X' OR 'O'
    player1 = ''
    while player1 !='X' and player1 != 'O':
        print('Select either \'X\' or\'O\' ')
        player1 = input('Player 1, select your marker: ')
        player1 = player1.upper()
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    print(f'\n Player 1 selected {player1}')
    print(f'\n player 2 selected {player2}\n')
    return player1, player2

def display_board(b):
    clear_output()
    print(b[7]+' | '+b[8]+' | '+b[9])
    print('----------')
    print(b[4]+' | '+b[5]+' | '+b[6])
    print('----------')
    print(b[1]+' | '+b[2]+' | '+b[3])
    
def in_game(player1, player2):
    display_board(b)
    i = 1
    game_end = False
    win = False
    while not game_end:
        x = 0
        if i == 9:
            game_end = True
            
        if i%2!=0:
            print(f'\nPlayer 1 place {player1} on board')
            while x not in range(1,10): #SELECTING A VALID POSITION FROM FOR PLAYER 1
                x = int(input('Select any empty place from board:'))
                if x in op:
                    x = 0
                else:
                    op.append(x)
            b[x] = player1
            display_board(b)
            i+=1
            if win_case(x):
                print('\nPlayer1 Won!')
                game_end = True
                win = True
        else:
            print(f'Player 2 place {player2} on board')
            while x not in range(1,10): #SELECTING A VALID POSITION FROM FOR PLAYER 1
                x = int(input('Select any empty place from board:'))
                if x in op:
                    x = 0
                else:
                    op.append(x)
            b[x] = player2
            display_board(b)
            i+=1
            if win_case(x):
                print('\nPlayer2 Won!')
                game_end = True
                win = True
                      
    if i==10 and win == False:
        print('\nNo One won the game, Game is Tie :D')
    
def win_case(x):
    list_of_tuple = [(1,2,3),(1,4,7),(1,5,9),(2,5,8),(3,6,9),(3,5,7),(4,5,6),(7,8,9)]
    for i in list_of_tuple:
        if x in i:
            if b[i[0]]==b[i[1]]==b[i[2]]:
                return True
    else:
        return False
if __name__ == "__main__" :
    tictac()

