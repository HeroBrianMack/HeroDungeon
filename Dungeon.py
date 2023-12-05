def setup() :
    # Creating Empty 3x5 List
    # Note: Possibly make 3D (WIP)
    # To Do: Fix List
    global Dungeon
    Dungeon = [[[0 for i in range(3)] for j in range(3)] for k in range(5)]
    global inventory
    inventory = ["Empty", "Empty"]
    # Player Location
    global Floor
    Floor = 0
    global Room
    Room = 0
    global Retreat
    Retreat = ""
    global Win
    Win = False
    # Filling List
    # Floor 1
    Dungeon[0][0][0] = "Empty"
    Dungeon[0][1][0] = "Sword"
    Dungeon[0][2][0] = "Monster"
    Dungeon[0][3][0] = "LadderUp"
    Dungeon[0][4][0] = "Sword"
    # Floor[0] 2
    Dungeon[0][0][1] = "LadderUp"
    Dungeon[0][1][1] = "Monster"
    Dungeon[0][2][1] = "Empty"
    Dungeon[0][3][1] = "LadderDown"
    Dungeon[0][4][1] = "Stone"
    # Floor[0] 3
    Dungeon[0][0][2] = "LadderDown"
    Dungeon[0][1][2] = "Sword"
    Dungeon[0][2][2] = "Gate"
    Dungeon[0][3][2] = "Boss"
    Dungeon[0][4][2] = "End"
def continue_enter() :
    input("Press enter to continue")
def options() :
    print("Choose an action:\n"
          "1. Search\n"
          "2. Fight\n"
          "3. Move\n"
          "4. Give up")
    #choice = 
    return input("Choose an option (1-4): ")
def pickup(choice) :
    global Room
    global Floor
    global Dungeon
    global inventory
    if (choice == "1"):
        if inventory[0] == "Empty" :
            inventory.insert(0, Dungeon[0][Room][Floor])
            print("You now own your very own rusty sword!")
        elif inventory[1] == "Empty":
            inventory.insert(1, Dungeon[0][Room][Floor])
            print("You now own your very own rusty sword!")
        else :
            print("Your greed has caught up to you and your hands are now too full!\n"
                "Will you discard an item to pick up the '" + Dungeon[0][Room][Floor] + "'?\n"
                "1. Pick up\n"
                "2. Refuse\n")
            choice = input("Choose an option (1-2): ")
            if (choice == "1") :
                print("What item will you remove?\n"
                    "1. " + inventory[0] + "\n"
                    "2. " + inventory[1] + "\n")
                choice = input("Choose an option (1-2): ")
                if (choice == 1 or 2) :
                    temp = inventory[int(choice)]
                    inventory.insert(int(choice), Dungeon[0][Room][Floor])
                    print("You discard your " + temp 
                          + " for the vastly superior " 
                          + Dungeon[0][Room][Floor] + "!" )
                    Dungeon[0][Room][Floor] = temp
    elif (choice == "2") :
        if (Dungeon[0][Room][Floor] == "Sword") :
            print("Bah! Who needs a sword when I have my fists!\n"
                "I am sure you are above the 99th percentile in intelligence.")
        elif (Dungeon[0][Room][Floor] == "Stone") :
            print("Only fools would grab a shiny stone in a dungeon, but you clearly know better.\n"
                "You must be at least in the 95th percentile of intelligence.")
    else :
        print("Your reading abilities truly shock me.\n"
            "Congratulations on getting this far while being illiterate.")
        interact()
                    
def room_move(move) :
    global Room
    global Retreat
    global Floor
    global Dungeon
    # Left
    if (move == "1") :
        if (Room <= 0) :
            print("You walk left and hit a wall, smooth.")
        elif (Dungeon[0][Room][Floor] == "Monster" and not Retreat == "Left") :
            print("You begin to walk— there is an angry monster in the way.")
        else :
            print("You move to the next room.")    
            Room -= 1
            if (Dungeon[0][Room][Floor] == "Monster") :
                Retreat = "Right"
    # Right
    elif (move == "2") :
        if (Room >= 4) :
            print("You valiantly continue forward, and then hit a wall.")
        elif (Dungeon[0][Room][Floor] == "Monster" and not Retreat == "Right") :
            print("You begin to walk— there is an angry monster in the way.")
        else :
            print("You move to the next room.")
            Room += 1
            if (Dungeon[0][Room][Floor] == "Monster") :
                Retreat = "Left"
    # Up
    elif (move == "3") :
        if (Dungeon[0][Room][Floor] == "LadderUp") :
            print("You successfully climb the ladder.")
            Floor += 1
        elif(Dungeon[0][Room][Floor] == "LadderDown") :
            print("You climb into the floor, congrats")
        else :
            print("You try to climb a ladder made of air, you fall flat on your face.")
    # Down
    elif (move == "4"):    
        if (Dungeon[0][Room][Floor] == "LadderDown") :
            print("You successfully climb down the ladder.")
            Floor -= 1
        elif(Dungeon[0][Room][Floor] == "LadderUp") :
            print("You attempt to climb down the ladder going up, and you are now on the floor.")
        else :
            print("You try to climb down ladder made of air into the floor, you are now laying on the ground.")
    continue_enter()

def interact() :
    global Room
    global Floor
    global Dungeon
    global Inventory
    if Dungeon[0][Room][Floor] == "Sword" :
        print("You see a nearly broken sword, do you grab it?\n"
              "1. Grab\n"
              "2. Refuse\n")
        choice = input("Choose an option (1-2): ")
        pickup(choice)
    elif Dungeon[0][Room][Floor] == "Stone" :
        print("You see a shiny stone, do you grab it?\n"
              "1. Grab\n"
              "2. Refuse\n")
        choice = input("Choose an option (1-2): ")
        pickup(choice)
    elif Dungeon[0][Room][Floor] == "Monster" :
        print("You see a large monster, unfortunately it seems unfriendly")
    elif Dungeon[0][Room][Floor] == "Gate" :
        print("You see a foreboding gate in front of you.\n"
              "To the side you see a lever, do you pull it?\n"
              "1. Yes\n"
              "2. No")
        choice = input("Choose an option (1-2): ")
        if choice == "1" :
            print("You pull the lever and as the gate opens you hear breathing, very loud breathing.")
            Dungeon[2][Room][Floor] = "Open"
        elif choice == "2" :
            print("You are scared and decide you quite like the dungeon.")
        else :
            print("You can't read very well, but you managed to get this far so congrats!")
    elif Dungeon[0][Room][Floor] == "LadderUp" :
        print("You see a ladder going upwards, but you can't see where it goes.")
    elif Dungeon[0][Room][Floor] == "LadderDown" :
        print("You see a ladder going downwards, but you can't see how far it goes down.")
    elif Dungeon[0][Room][Floor] == "Boss" :
        print("If you thought previous monsters were large, this one makes them look like toys.")
        if (Inventory[0] == "Sword" or Inventory[1] == "Sword") and (Inventory[0] or Inventory[0] == "Stone") :
            print("You feel prepared to face this enemy!")
        else :
            print("You feel far too weak to face this threat.")
    elif Dungeon[0][Room][Floor] == "End" :
        print("It's time for this wonderful and absolutely non-sarcastic experience to end.")
    elif Dungeon[0][Room][Floor] == "Empty" :
        print("You use all of your brain power and realize the room is empty!")
    continue_enter()
    
def game_run() :
    global Room
    global Floor
    Room = 0
    Floor = 0
    setup()
    gameEnd = False
    while not gameEnd:
        choice = options()
        if (choice == "4"):
            gameEnd = True
        elif (choice == "3"):
            room_move(input("Where do you want to move?\n"
                            "1. Left\n"
                            "2. Right\n"
                            "3. Up\n"
                            "4. Down\n"
                            "Choose an option (1-4): "))
        elif (choice == "1"):
            interact()

def game_start() :
    global Win
    print("You wake up disoriented.")
    continue_enter()
    print("The last thing you remember was experiencing aggressive marketing from Truck-kun.\n")
    game_run()
    if not Win :
        choice = input("Would you like to try again?\n"
            "1. Yes\n"
            "2. No\n")
    if Win :
        print("Congrats on winning my game!\n"
              "Have feedback or found bugs?\n"
              "Message me on discord, my tag is 'nonhero'.\n"
              "Now...")
        choice = input("Would you like to play again?\n"
            "1. Yes\n"
            "2. No\n")
    if choice == "1" :
        game_start()
game_start()