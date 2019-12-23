#gets a random number for monster attack
from random import randint

game_running = True 
#function for random number
def calculate_monster_attack():
    return randint(monster['attack_min'] , monster['attack_max'])
#code is being executed
while game_running == True:
   #a new round is being executed
    new_round = True

    player = {'name': 'Collo', 'heal': 16, 'attack': 15, 'health': 100}
    monster = {'name': 'Max', 'attack_min': 10, 'attack_max': 20, 'health': 100}
    #player enters name
    print('----' * 7)
    print('Enter player name')
    player['name'] = input()

    print('----' * 7)
    print(player['name'] + ' has ' + str(player['health']) + ' health ')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health ')
    
    while new_round == True:
    
            player_won = False
            monster_won = False
    
            print('Please select action. ')
            print('1) Attack. ')
            print('2) Heal. ')
            print('3) Exit Game. ')

            
            player_choice = input()
            #if player chooses attack, what happens
            if player_choice == '1':
                monster['health'] = monster['health'] - player['attack']
                if monster['health'] <= 0:
                    player_won = True
                
                else:
                    player['health'] = player['health'] - calculate_monster_attack() 
                    if player['health'] <= 0:
                        monster_won = True

                    print(player['health'])
                    print(monster['health'])
                    
            #if player chooses heal, what happens
            elif player_choice == '2':
                player['health'] = player['health'] + player['heal']

                monster_attack = randint(monster['attack_min'] , monster['attack_max'])
                player['health'] = player['health'] - monster_attack
                if player['health'] <= 0:
                    monster_won = True

            #when player chooses exit game
            elif player_choice == '3':
                new_round = False
                game_running = False


            else:
                print('Inavalid Input')
            #when either player or monster wins, what happens
            if player_won == False and monster_won == False:
                print(player['name'] + ' has ' + str(player['health'])  + ' left ')
                print(monster['name'] + ' has ' + str(monster['health']) + ' left ')

            #when player wins
            elif player_won:
                print(player['name'] + ' won ')
                new_round = False
               
            #when monster wins
            elif monster_won:
                print('The Monster won ')
                new_round = False

                
              