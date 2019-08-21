#Jordan Covo
#7/19
#Cee-Lo

import random

greeting= 'Hello, welcome to Cee-Lo simulator! If you are unfamiliar with the rules then please read instructions doc'
#The game is played with 3 dice and various outcomes dependent on number combinations
print(greeting)

player_balance=5
computer_balance=5

player_score=0
enemy_score=0

#this is how the game will start; each player starts with 5 in the bank and a score of 0

player_bet=0
enemy_bet=0

again= True

IsPlayerTurn= True

while True:
    response=input('Ready to Roll Em Dice?: ')
    #continue if user enters yes
    if response=='yes' or response=='y' :
        print('You have $' + str(player_balance))
        break
    elif response=='no' or response=='n' :
        exit()
    else:
        print("Wow scared money dont make no money!")

def SetPlayerBet(bal):
    global player_bet

    #this runs while the condition is true, wont stop until "break" is called

    while True:
        player_bet= int(input('Enter your bet: '))
        print('.')
        # try loop is accounting for ValueError - in case the user inputs something besides a number
        try:
            if int(player_bet) <= 5:
                print('Your bet is $' + str(player_bet))
                bal -= int(player_bet)
                break
            elif int(player_bet) < 1:
                print('You have to bet something!')
            else:
                print("You can't bet that much.")
        except ValueError:
            print('Enter a number please.')

        print('You have $' + str(bal) + ' left')
        print('.')

def SetEnemyBet(bal):
    global enemy_bet

    enemy_bet = random.randint(0,5)
    bal-=enemy_bet
    print('Your opponent bet $' + str(enemy_bet) + '.')
    print('They have $' + str(bal) + ' left.')
    print('.')

#creating dice roll function now

def diceroll():
    return [random.randint(1, 6) for _ in range(3)]

#analyze roll

def AnalyzeRoll(inputRoll):
    global player_score
    global enemy_score

    inputRoll.sort()
    if IsPlayerTurn:
        print('Your roll is: ' + str(inputRoll))
    else:
        print("Your opponent's roll is: " + str(inputRoll))
    if inputRoll == [4, 5, 6] or len(set(inputRoll)) == 1:
        # 456 or triple - auto win
        return (-1)
    elif inputRoll[0] == inputRoll[1] or inputRoll[1] == inputRoll[2]:
        if inputRoll[2] == 6 and inputRoll[1] != inputRoll[2]:
            # pair of non 6 and 6 - auto win
            return (-1)
        elif inputRoll[0] == 1 and inputRoll[0] != inputRoll[1]:
            # pair of non 1 and 1 - auto lose
            return (-2)
        elif inputRoll[1] != inputRoll[2]:
            # left pair
            if IsPlayerTurn:
                player_score = inputRoll[2]
                print('Your score is: ' + str(player_score))
            else:
                enemy_score = inputRoll[2]
                print("Your opponent's score is: " + str(enemy_score))
            again = False
            return (inputRoll[2])
        elif inputRoll[0] != inputRoll[1]:
            # right pair
            if IsPlayerTurn:
                player_score = inputRoll[0]
                print('Your score is: ' + str(inputRoll[0]))
            else:
                enemy_score = inputRoll[0]
                print("Your opponent's score is: " + str(inputRoll[0]))
            again = False
            return (inputRoll[0])
    elif inputRoll == [1, 2, 3]:
        # auto lose 123
        return (-2)
    else:
        # special case code - no valid roll
        return (-3)

def UpdateScore(score):
    global again
    global playerRoll
    global enemyRoll

    if score == -1:
        if IsPlayerTurn:
            print('You win everything!')
        else:
            print('Your opponent takes it all!')
        again = False
    elif score == -2:
        if IsPlayerTurn:
            print('You lose everything!')
        else:
            print('You take it all!')
        again = False
    elif score == -3:
        print('Rolling...')
        if IsPlayerTurn:
            playerRoll = diceroll()
        else:
            enemyRoll = diceroll()
    else:
        again = False


def CompareScores(p,e):
    global player_balance
    global computer_balance

    if p>e:
        player_balance+=player_bet+enemy_bet
    elif e>p:
        computer_balance+=enemy_bet+player_bet
    else:
        print('A tie?')
    print('Your new total is $' + str(player_balance))
    print("Your opponent's new total is $" + str(computer_balance))


SetPlayerBet(player_balance)
SetEnemyBet(computer_balance)
playerRoll = diceroll()
while again is True:
    scorecode = AnalyzeRoll(playerRoll)
    UpdateScore(scorecode)

IsPlayerTurn = False
again = True
enemyRoll = diceroll()
while again is True:
    scorecode = AnalyzeRoll(enemyRoll)
    UpdateScore(scorecode)

#comparison not working properly - probably something to do with
#the scope of the score or balance variables
CompareScores(player_score, enemy_score)

