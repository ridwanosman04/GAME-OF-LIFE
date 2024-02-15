import random

player1={"bank account": 1000, "position": 0}
player2={"bank account": 1000, "position": 0}

def generateCareer(playernum,playerdict):
    '''It takes in a string with player number and a player.Generates a random career
     and salary. Adds salary amount to player's bank account.
    Print out info about career and salary for player to know.'''
    careers = ["Engineer", "Doctor", "Artist", "Teacher","Mechanic"]
    career = random.choice(careers)
    salary = random.randrange(3000, 8000)
    playerdict["career"]=salary
    playerdict["bank account"]=playerdict.get("bank account") + salary
    print(playernum,":\nYou are a ", career, "\nYour salary  is $", salary)

def getNumber():
    '''Generates a random number from range 1 to 8.'''
    num=random.randrange(1,8)
    return num

def movePlayer(playerdict):
    '''Takes is a player and gets the player's position. It takes in the current position of player
    and uses get num to generate a random number and adds that number to current position as long as
     position does not exceed board space. Updates value for position key. '''
    num=playerdict.get("position")
    movement=getNumber()
    print("You rolled a",movement,"!")
    playerdict["position"] = num + movement
    playerdict["position"] = min(num + movement, 30)
    print("Position:",playerdict.get("position"))
def greenSpace(playerdict):
    '''Takes in a player. Gets value associated with career key
    and adds it to the bank account value. Updates the bank account key.'''
    salary = playerdict.get("career")
    playerdict["bank account"]=playerdict.get("bank account") + salary
    print("You passed a green space! \n $",salary,"added to your bank account.")
    print("Bank Account:",playerdict.get("bank account"))
def redSpace(playerdict):
    '''Takes in player and generates a random inconvenience and cost.
      Subtracts cost from given players bank account value.
      Prints the inconvenience, cost and new bank account balance for user to see.'''
    inconveniences = ["Car Repairs","Plumbing Issues","Vet trip","Accident"]
    inconvenience = random.choice(inconveniences)
    loss = random.randrange(500, 2000)
    playerdict["bank account"]=playerdict["bank account"] - loss
    print("You landed on a red space!",inconvenience, "cost you $",loss,".")
    print("Bank Account:", playerdict.get("bank account"))
def marry(playerdict):
    '''Takes in player and generates a random spouse, career for spouse, and their salary.
    Adds new key into players dictionary associated with spouse.'''
    spouseName =["Mary","Maurice","Josh","Karly","Pedro","Eli"]
    spouseCareers = ["Engineer", "Doctor", "Artist", "Teacher"]
    name=random.choice(spouseName)
    spouseCareer = random.choice(spouseCareers)
    spouseSalary = random.randrange(1000,8000)
    playerdict["spouse"]=spouseSalary
    print("Congratulations! You got married to",name,"!\nThey have a job as a",spouseCareer,
    "and make",spouseSalary,"!")
def haveKids(playerdict):
    '''Takes in player and generates a random amount of kids. For each kid,
    user is allowed to input names. If key kids is in player dictionary
    aa value of 1000 is added to the key, if not a new key 'kids' is added.
    Player pays hospital fees. The total kids and updated bank account is displayed to player.'''
    numKids = random.randrange(1, 5)
    for i in range(numKids):
        kidName = input("Enter your kid's name: ")
        if "kids" in playerdict:
            playerdict["kids"]= playerdict["kids"] + 1000
        else:
            playerdict["kids"] = 1000
        playerdict["bank account"] = playerdict["bank account"] - 700
        print("You named your",i+1,"kid",kidName,"!")
    print("You have", numKids,"kid/s!\nThe hospital charged you $",i*700)
    print("Bank Account:", playerdict.get("bank account"))

def properties(playerdict):
    '''Takes in a player, and asks if they want to purchase a property. If yes, a
    random property and value is generated, added as a key into player's dictionary
    and subtracted from bank account. If no, function goes on. If invalid, will restate
    question.'''
    print("Bank Account:", playerdict.get("bank account"))
    ans=input("Do you want to buy a property? (yes or no): ")
    if ans == "yes":
        prop=["Beach house","Mansion","House","Condo","Apartment","Town home"]
        propchoice = random.choice(prop)
        price = random.randrange(5000, 10000)
        playerdict["bank account"] = playerdict["bank account"] - price
        playerdict["properties"]=price
        print("Congrats on your new",propchoice,"\nSold at the price of $",price)
        print("Bank Account:", playerdict.get("bank account"))
    elif ans == "no":
        print("Okay!")
    else:
        print("Invalid answer!")
        properties(playerdict)

def winner(play1dict,play2dict):
    '''Calcualtes total assets in both player dictionaries and sees who has more
    total assets to declare them the winner.'''
    print("Game Over!")
    print("Player One:\nYour assets are:")
    for key, value in play1dict.items():
        print(key,value)
    print("Player Two:\nYour assets are:")
    for key,value in play2dict.items():
        print(key,value)
    play1=int(play1dict.get("bank account"))+int(play1dict.get("spouse",0))+(int(play1dict.get("properties",0))*1.5)+int(play1dict.get("kids",0))
    play2=int(play2dict.get("bank account"))+int(play2dict.get("spouse",0))+int(play2dict.get("properties",0))+int(play2dict.get("kids",0))
    if play1 > play2:
        print("Player 1 wins with a net worth of $",play1)
    elif play2 > play1:
        print("Player 2 wins with a net worth of $",play2)
    else:
        print("It's a tie!")

def checkNegative(player,oppplayer,playerdict):
    '''If bank account goes negative, the other player will win
    and game will end.'''
    if playerdict["bank account"] < 0:
        print("Game Over!\n",oppplayer," wins!")
        exit()
def playGame():
    '''Runs the entire game by setting the space type associated with space number.
    Ask for return to run the generateCareer and movePlayer function.
    Begins with boolean statements to make sure marriage
    and kid functions only run once for each player. Once both players are past 30,
    it will run the winner function and end game.'''
    input("Player 1:\nPress Enter to reveal career: ")
    generateCareer("Player 1",player1)
    input("Player 2:\nPress Enter to reveal career: ")
    generateCareer("Player 2",player2)
    player1Married = False
    player2Married = False
    player1Kids = False
    player2Kids = False
    while player1["position"] < 30 or player2["position"] < 30:
        input("Player 1's turn:\nPress enter to roll dice: ")
        movePlayer(player1)
        if player1["position"] == 3:
            greenSpace(player1)
        elif player1["position"] == 5:
            greenSpace(player1)
        elif player1["position"] == 13:
            greenSpace(player1)
        elif player1["position"] == 15:
            greenSpace(player1)
        elif player1["position"] == 21:
            greenSpace(player1)
        elif player1["position"] == 25:
            greenSpace(player1)
        elif player1["position"] == 4:
            redSpace(player1)
        elif player1["position"] == 8:
            redSpace(player1)
        elif player1["position"] == 16:
            redSpace(player1)
        elif player1["position"] == 22:
            redSpace(player1)
        elif player1["position"] == 27:
            redSpace(player1)
        elif player1["position"] > 5 and not player1Married:
            marry(player1)
            player1Married = True
        elif player1["position"] > 16 and not player1Kids:
            haveKids(player1)
            player1Kids = True
        elif player1["position"] == 7:
            properties(player1)
        elif player1["position"] == 11:
            properties(player1)
        elif player1["position"] == 23:
            properties(player1)
        elif player1["position"] == 28:
            properties(player1)
        checkNegative("Player 1", "Player 2", player1)
        input("Player 2's turn:\nPress enter to roll dice: ")
        movePlayer(player2)
        if player2["position"] == 3:
            greenSpace(player2)
        elif player2["position"] == 5:
            greenSpace(player2)
        elif player2["position"] == 13:
            greenSpace(player2)
        elif player2["position"] == 15:
            greenSpace(player2)
        elif player2["position"] == 21:
            greenSpace(player2)
        elif player2["position"] == 25:
            greenSpace(player2)
        elif player2["position"] == 4:
            redSpace(player2)
        elif player2["position"] == 8:
            redSpace(player2)
        elif player2["position"] == 16:
            redSpace(player2)
        elif player2["position"] == 22:
            redSpace(player2)
        elif player2["position"] == 27:
            redSpace(player2)
        if player1["position"] > 5 and not player2Married:
            marry(player2)
            player2Married = True
        elif player2["position"] > 16 and not player2Kids:
            haveKids(player2)
            player2Kids = True
        elif player2["position"] == 7:
            properties(player2)
        elif player2["position"] == 11:
            properties(player2)
        elif player2["position"] == 23:
            properties(player2)
        elif player2["position"] == 28:
            properties(player2)
        checkNegative("Player 2", "Player 1", player2)

    player1["position"] = 30
    player2["position"] = 30
    if player1["position"]==30 and player2["position"]==30:
        winner(player1,player2)

if __name__ == '__main__':
    print("My tests:")
    #playGame()