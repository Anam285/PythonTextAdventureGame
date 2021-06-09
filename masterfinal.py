from random import randint
import random
import time ,os,sys
from time import sleep
# import playsound
import winsound

def print_slow(line_in):
    for x in line_in:
        # print(x, end='')
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.05)

def main_game():

    run = True 
    
    while run is True:
        print('')
        print ("                   The lost medallion of the ancient forest                          ")
        print( '  ')
        def quit():
            global run
            print(' \n GAME OVER. YOU LOSE \n')
            run = False
            
        def question_1():
        #start of queston2
            def question_2():
            #start of question three
                def question_3():
                #start of question4
                    def question_4():
                        print_slow("The troll lets you go... Better go that way! As you escape you spot a slightly dusty but sort of sparkling old chest half buried...\n")
                        print_slow(" 'Interesting. This looks promising. Now what was that code again?' \n")
                        print_slow("welcome to final challenge \n")
                        def check_pin():
                            tries=0
                            while tries <=3:
                                # print_slow("welcome to final challenge \n")
                                
                                print_slow("Please Enter You 4 digit To unlock the chest: \n")
                                print_slow("you get 3 Tries")
                                pin_enter = input("--->")
                                if pin_enter == '1234':
                                    print('Congratulations You Entered Them In The Correct Orderr!! \n\n')
                                    print_slow('now the pieces are in correctly, which way will you turn it to unlock the chest?\n\n')
                                    print_slow('Right or Left \n')
                                    left_right= input().lower().strip()
                                    if left_right == 'left':
                                        print_slow("That was correct!! The chest clicks and unlocks you have found your fathers medallion!! \n\n")
                                    else:
                                        print_slow("That wasn't the right way! a noise came from the chest and then it lowered into the ground! GAME OVER! \n\n")
                                        quit()
                                    break
                                # elif len(pin_enter) != 4:
                                #     print_slow('Must Be 4 Digits') 
                                #     print("Enter again")
                                #     tries+=1
                                #     if tries == 3:
                                #         print("You have run out of tries")
                                #         quit()
                                #         break
                                else:
                                    print("Enter again")
                                    tries+=1
                                    if tries == 3:
                                        print("You have run out of tries")
                                        quit()
                                        break
                        winsound.PlaySound('pokemonbattle.wav', winsound.SND_FILENAME)
                        check_pin()        
                    print_slow("Do you want to head to the river bank or the bridge? river bank/rope bridge \n ")
                    print_slow("river bank/rope bridge \n")
                    answer3=input("--->").lower()
                    def typingPrint(text):
                            for character in text:
                                sys.stdout.write(character)
                                sys.stdout.flush()
                                time.sleep(0.05)
                    def start():
                        typingPrint(" \n Well well well... You've made it this far but can you get past me and get the next part to the code?")
                        time.sleep(1)
                    def guess_game():
                        typingPrint(" \n What colour crystal am i holding?\nRed, Yellow, Pink, Green, Orange, Purple or Blue? \n")
                        colours = ["Red", "Yellow", "Pink", "Green", "Orange", "Purple", "Blue"]
                        value = random.choices(colours, k=2) 
                        
                        tries = 0
                        left = 4
                        gameon = True
                        while gameon is True:
                            while tries < 4:
                                user = input("--->").capitalize().strip()
                                
                                left -= 1
                                if user in value:
                                    typingPrint("Hm. Congratulations. Here is your part of the code... 2, 4, \n\n")
                                    gameon= False
                                    question_4()
                                    break
                                    
                                elif user not in value:
                                    tries += 1
                                    typingPrint("Nope...")
                                    typingPrint(f"{left} tries remaining. \n")

                        
                            if tries == 4:
                                typingPrint(f" \n Haha! Too bad you fool,\nthe colour was {value}! Back you go! \n \n \n")
                                time.sleep(2)
                                guess_game()
                                
                            break
                                
                        # start()
                        # guess_game()
                        
                    if answer3== ("rope bridge"):
                        print_slow("You take your time crossing the rope bridge, wooden panels are breaking when you step on them as you go further...\n")
                        print_slow("You finally reach the end of the bridge and an angry troll jumps out of a tree sees you and isn't happy that you're there\n")
                        time.sleep(2)
                        winsound.PlaySound('pokemonbattle.wav', winsound.SND_FILENAME)
                        start()
                        guess_game()

                    elif answer3== ("river bank"):
                        print_slow("You get down to the river bank and there is a chunk of wood and some tools. Looks like someone was going to build a raft!\n")
                        print_slow("You can build a raft or swim... the river is choppy so it might not be safe to swim\n")
                        # print_slow("Do you swim or build a raft? swim/build a raft \n")
                        print_slow("Build a raft or swim? \n")
                        answer4 = input("--->").lower().strip()
                        if answer4 == ("build a raft"):
                            print_slow("You finally cross the river and an angry troll jumps out from under a bridge and isn't happy that you're there\n")
                            time.sleep(0.02)
                            winsound.PlaySound('pokemonbattle.wav', winsound.SND_FILENAME)
                            start()
                            guess_game()
                        else:
                            # answer4 == ('swim')
                            print_slow("This water is way too deep! Why did i decide to swim when... I CAN'T SWIM! Aaaaa \n")
                            print_slow("Think again \n")
                            question_3()

                # from playsound import playsound
                # playsound('pokemonbattle.mp3')

                board =["0"," "," "," "," "," "," "," "," "," "]
                board_d=["","1","2","3","4","5","6","7","8","9"]

                # from random import randint
                # import random
                # import time ,os,sys

                def dis_board(board):

                    print('     |     |  ')
                    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
                    print('     |     |  ')
                    print('-----------------')
                    print('     |     |  ')
                    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
                    print('     |     |  ')
                    print('-----------------')
                    print('     |     |  ')
                    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
                    print('     |     |  ')



                


                def place_marker(board, marker, position):
                    board[position] = marker

                
                def player_marker():
                    marker=''
                    while marker != 'X' and marker != 'O':
                        
                        print_slow('you chose to play against the Gods\n')
                        print_slow('Choose a symbol X or O \n')
                        marker= input("--->").upper()

                        if marker == 'X':
                            return ('X','O')
                        elif marker =='O':
                            return ('O','X')
                        
                def who_go_first():
                    print_slow('Flip a coin to see who goes first\n')
                    print_slow('The Gods or you \n')
                    print_slow('You better pray to The Gods they let you go first\n')
                    print_slow(' Flipping the coin now....\n')

                    time.sleep(2)
                    marker = random.randint(1,2)
                    if marker == 1:
                        # print ('X goes first')
                        return ('X')
                        
                    else:
                        # print ('O goes first')
                        return ('O')
                        
                def check_win(board,mark ):
                    if (board[7] == board[8] == board [9] == mark)or(board[4] == board[5] == board [6] == mark) or(board[1] == board[2] == board [3] == mark) or(board[7] == board[5] == board [3] == mark) or(board[1] == board[5] == board [9] == mark) or (board[1] == board[4] == board [7] == mark) or (board[2] == board[5] == board [8] == mark)or (board[3] == board[6] == board [9] == mark):
                        
                        return True 
                    else:
                        return False
                    
                def check_used_num(board):
                
                    t=0
                    for i in range(len(board)):
                        if board[i] != ' ':
                            t+=1
                            # print(f'num of used sapace{t}')
                            # return(t)
                        else:
                            pass
                            # return(t)
                    return(t)

                def check_full_board(board):
                    
                    l= check_used_num(board)

                    if l ==10 :
                        
                        return True
                    elif l<10:
                        return False

                def game_choice():
                    print_slow('Are you ready to play: yes / no \n ')
                    choice = input("--->").lower()
                    if choice == 'yes':
                        return True
                    else:
                        return False

                   
                            
                def check_used_position_forplayer(position):
                    if board[position] ==' ':
                        return True 
                        

                def check_correct_input(position):
                    while position not in [1,2,3,4,5,6,7,8,9]:
                        print_slow('Enter the spot between 1-9 you want to play\n')
                        position = int(input("--->"))
                    return(position)



                def check_comp_position(position ):
                   
                        if board[position] == ' ':
                    
                            return True
                        else:
                            position = random.randint(1,9)
                            check_comp_position(position )
                    
                

                def check_who_won(player_1,computer ):
                    if check_win(board,player_1) == True :
                        # print_slow('You Won\n')
                        # print_slow('your code to next level is XYZ')
                        return (player_1)
                    elif check_win(board,computer) == True :
                        print_slow('The Gods won/n  ')
                        print_slow('Better luck next time /n')
                        return(computer)
                    # else:
                    #     print ('draw')

                def game_x_o():
                    i=1
                    print ('Complete The Temple ')
                    # game_on = game_choice()
                    
                    dis_board(board_d)
                    player_1, computer = player_marker()  # gives out (x,o) or( o,x)
                    turn = who_go_first()  # returns x or o
                    print(f'{turn} goes first ')
                    i = 0
                    game_on = game_choice()
                    
                    while game_on is True:
                        while i <= 9:
                            if turn == player_1:    
                                position1 = 0
                                position=check_correct_input(position1)
                                
                                while check_used_position_forplayer(position):
                                    place_marker(board, player_1, position)
                                    w_or_l = check_win(board, player_1)
                                    full_board=check_full_board(board)
                                    

                                    if w_or_l == False and full_board == True:
                                        time.sleep(1)
                                        dis_board(board)
                                        print("It's a Draw")
                                        game_on= False
                                        break

                                    elif w_or_l == True:
                                        time.sleep(1)
                                        dis_board(board)
                                        print(f'{ player_1} has won')
                                        game_on = False
                                        break
                                    
                                    else:
                                        i += 1
                                        # check_full_board(board)
                                        time.sleep(1)
                                        dis_board(board)
                                        
                                        turn = computer
                                        print ("Its The God's turn")
                                        game_on = True
                                    # break       
                                # game_on == False
                            elif turn == computer:
                            
                                position1 = random.randint(1,9)
                                # while check_full_board(board):
                                
                                while check_comp_position(position1):
                                
                                
                                    place_marker(board, computer, position1)

                                    time.sleep(1)
                                    w_or_l = check_win(board, computer)
                                    full_board=check_full_board(board)

                                    if w_or_l == False and full_board == True:
                                        time.sleep(1)
                                        dis_board(board)
                                        print("It's a Draw")
                                        # game_x_o()
                                        game_on= False
                                        break

                                    elif w_or_l == True:
                                        time.sleep(1)
                                        dis_board(board)
                                        print(f'{computer} have won')
                                        game_on = False
                                        break

                                    else:
                                        time.sleep(1)
                                        dis_board(board)
                                        i += 1
                                        turn = player_1
                                        game_on = True
                                    # break 
                                # game_on==False       
                            break
                    check_who_won(player_1, computer)
                    if check_who_won(player_1, computer) == computer:
                        print_slow('play again')
                        game_x_o()
                    elif check_who_won(player_1, computer)== player_1:
                        print( 'you won')
                        print_slow('You get a code. It says 1, 3. You should probably keep hold of that!\n\n \n')
                        question_3()
                    else:
                        question_2()
                    
                
                    time.sleep(1)
                    print_slow('\n GAME OVER ') 

                print_slow("Which route will you take? left / right? \n")
                answer = input("--->").lower().strip()
                if answer == ("left"):
                        
                    print_slow("You're walking along a path when you suddenly stumble over tree root, you begin to tumble down a hill. You land in a part of the forest you've never seen before.\n")
                    time.sleep(2)
                    print_slow( "There's a old ruined temple beyond the trees, you decide to explore it. The temple has roots coming up through the floors and large bricks that have fallen from walls. Theres is something strange in the middle, as you near you realise its a puzzle. Maybe this will help you find the medallion Father said this place had powers, you try to work out the puzzle.\n\n")
                    time.sleep(2)
                    winsound.PlaySound('pokemonbattle.wav', winsound.SND_FILENAME)
                    game_x_o()



                if answer == ("right"):
                        
                    print_slow("Something inside you is just telling you to go this way. You rememeber your father always used to wander off down this way. You're now in a part of the forest you've never seen before...\n")
                    time.sleep(2)
                    print_slow("There's an old ruined temple beyond the trees, you decide to explore it. The temple has roots coming up through the floors and large bricks that have fallen from walls. Theres is something strange in the middle, as you near you realise it's a puzzle. Maybe this will help you find the medallion, you try to work out the puzzle.\n")
                    winsound.PlaySound('pokemonbattle.wav', winsound.SND_FILENAME)
                    game_x_o()

                    # question_2()
            print_slow(" It's late morning when you wake. \n 'Strange. Im always an early riser' \n You start making breakfast and suddenly notice your prized possesion has gone from around your neck. That mysterious Medallion your father left you has been stolen! \n 'Father said the medallion was to never leave the forest, never mind my neck! I should go...'\n ")
            print_slow("Check the house! / maybe later?\n")
            answer = input("---> ").lower().strip()

            if answer == ("check the house"):
                print_slow("its not there, now what?! \n ")
                print_slow("Check the forest? yes / no \n")
                answer2 = input("---> ").lower().strip()
                if answer2== "no":
                    print("go home then.")
                    quit()
                elif answer2== "yes":
                    print_slow("You step outside your house and into the seemingly endless green forest that surrounds it, there are a few forest animals roaming. You head down the pathway to begin your forest search, it branches into two.\n")
                    question_2()
                else:
                    print_slow("wrong answer")
                    question_1() 
            elif answer == ("maybe later"):
                print_slow("'Welll, maybe i should fuel up first..?' \n")
                print_slow('Giving you second chance to check the forest! \n')
                answer2 = input("Check the forest? yes/no ").lower()
                if answer2 == "no":
                    print("go home then..")
                    question_1()
                    
                    
                elif answer2 == "yes":
                    print_slow("You step outside your house and into the seemingly endless green forest that surrounds it, there are a few forest animals roaming. You head down the pathway to begin your forest search, it branches into two.\n")
                    question_2()
                
        question_1()    # print ('the end')
        break    
        
    
main_game()

        