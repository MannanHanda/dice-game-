import random
while True:
    winners=[]
    player1=input("Enter the name of player 1- ")
    player2=input("Enter the name of player 2- ")
    print("")

    player1Score=0
    player2Score=0

    for i in range(1,6):
        print(f"Round {i}")
        print("")

        #Player1
        player1Dice1=random.randint(1,6)
        player1Dice2=random.randint(1,6)
        player1Score+=player1Dice1+player1Dice2
        print("Player 1")
        print(f"Roll 1- {player1Dice1}")
        print(f"Roll 2- {player1Dice2}")
        
        if (player1Dice1+player1Dice2)%2==0:
            print(f"Bonus- 10pts")
            player1Score+=10
            print("")
        elif (player1Dice1+player1Dice2)%2!=0:
            print("Penalty- 5pts")
            player1Score-=5
            print("")
            
        if player1Dice1==player1Dice2:
            for y in range(1):
                print("Player 1 Bonus Round")
                print("")
                player1Dice1=random.randint(1,6)
                player1Dice2=random.randint(1,6)
                player1Score+=player1Dice1+player1Dice2
                print("Player 1")
                print(f"Roll 1- {player1Dice1}")
                print(f"Roll 2- {player1Dice2}")
                if (player1Dice1+player1Dice2)%2==0:
                    print(f"Bonus- 10pts")
                    player1Score+=10
                    print("")
                elif (player1Dice1+player1Dice2)%2!=0:
                    print("Penalty- 5pts")
                    player1Score-=5
                    print("")
                

        #Player2
        player2Dice1=random.randint(1,6)
        player2Dice2=random.randint(1,6)
        player2Score+=player2Dice1+player2Dice2
        print("Player 2")
        print(f"Roll 1- {player2Dice1}")
        print(f"Roll 2- {player2Dice2}")
        
        if (player2Dice1+player2Dice2)%2==0:
            print(f"Bonus- 10pts")
            player2Score+=10
            print("")
        elif (player2Dice1+player2Dice2)%2!=0:
            print("Penalty- 5pts")
            player2Score-=5
            print("")

        if player2Dice1==player2Dice2:
            for y in range(1):
                print("Player 2 Bonus Round")
                print("")
                player2Dice1=random.randint(1,6)
                player2Dice2=random.randint(1,6)
                player2Score+=player2Dice1+player2Dice2
                print("Player 1")
                print(f"Roll 1- {player2Dice1}")
                print(f"Roll 2- {player2Dice2}")
                if (player2Dice1+player2Dice2)%2==0:
                    print(f"Bonus- 10pts")
                    player2Score+=10
                    print("")
                elif (player2Dice1+player2Dice2)%2!=0:
                    print("Penalty- 5pts")
                    player2Score-=5
                    print("")


        #Decision
        if i==5 and player1Score>player2Score:
            print(f"{player1}'s score- {player1Score}")
            print(f"{player2}'s score- {player2Score}")
            print(f"{player1} Wins!")
            print("")
            winners.append(f"{player1}'s score- {player1Score} \n")
            f=open("test.txt",'a')
            f.writelines(winners)
            f.close()
        elif i==5 and player2Score>player1Score:
            print(f"{player1}'s score- {player1Score}")
            print(f"{player2}'s score- {player2Score}")
            print(f"{player2} Wins!")
            print("")
            winners.append(f"{player2}'s score- {player2Score} \n")
            f=open("test.txt",'a')
            f.writelines(winners)
            f.close()
        elif i==5 and player2Score==player1Score:
            while True:
                finalRoll1=random.randint(1,6)
                finalRoll2=random.randint(1,6)
                print("Sudden Death")
                print("")
                print(f"Player1- {finalRoll1}")
                print(f"Player2- {finalRoll2}")
                if finalRoll1>finalRoll2:
                    print(f"{player1}'s score- {player1Score}")
                    print(f"{player2}'s score- {player2Score}")
                    print(f"{player1} Wins!")
                    print("")
                    winners.append(f"{player1}'s score- {player1Score} \n")
                    f=open("test.txt",'a')
                    f.writelines(winners)
                    f.close()
                    break
                elif finalRoll2>finalRoll1:
                    print(f"{player1}'s score- {player1Score}")
                    print(f"{player2}'s score- {player2Score}")
                    print(f"{player2} Wins!")
                    print("")
                    winners.append(f"{player2}'s score- {player2Score} \n")
                    f=open("test.txt",'a')
                    f.writelines(winners)
                    f.close()
                    break




