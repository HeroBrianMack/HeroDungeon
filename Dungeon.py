# Creating Empty 3x5 List
# Note: Possibly make 3D for future mapping
# To Do: Fix List
Dungeon = [[0 for i in range(3)] for j in range(5)]
# Player Location
Floor = 0
Room = 0
Retreat = ""
# Filling List
# Floor 1
Dungeon[0][0] = "Empty"
Dungeon[1][0] = "Sword"
Dungeon[2][0] = "Monster"
Dungeon[3][0] = "LadderUp"
Dungeon[4][0] = "Sword"
# Floor 2
Dungeon[0][1] = "LadderUp"
Dungeon[1][1] = "Monster"
Dungeon[2][1] = "Empty"
Dungeon[3][1] = "LadderDown"
Dungeon[4][1] = "Stone"
# Floor 3
Dungeon[0][2] = "LadderDown"
Dungeon[1][2] = "Sword"
Dungeon[2][2] = "Gate"
Dungeon[3][2] = "Boss"
Dungeon[4][2] = "End"

print(Dungeon[4][0])
#
print(Dungeon[Room][Floor])
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
def room_move(move) :
    global Room
    global Retreat
    global Floor
    global Dungeon
    # Left
    if (move == "1") :
        if (Room <= 0) :
            print("You walk left and hit a wall, very smooth.")
        elif(Dungeon[Room][Floor] == "Monster" and not Retreat == "Left") :
            print("You begin to walk— when you remember there is an angry monster in the way")
        else :
            print("You move to the next room.")    
            Room -= 1
            if (Dungeon[Room][Floor] == "Monster") :
                Retreat = "Right"
    # Right
    elif (move == "2") :
        if (Room >= 4) :
            print("You valiantly continue forward, and then hit a wall.")
        elif(Dungeon[Room][Floor] == "Monster" and not Retreat == "Right") :
            print("You begin to walk— when you remember there is an angry monster in the way")
        else :
            print("You move to the next room.")
            print(Dungeon[Room][Floor])
            Room += 1
            print(Room)
            if (Dungeon[Room][Floor] == "Monster") :
                Retreat = "Left"
    # Up
    elif (move == "3") :
        if (Dungeon[Room][Floor] == "LadderUp") :
            print("You successfully climb the ladder.")
            Floor += 1
        elif(Dungeon[Room][Floor] == "LadderDown") :
            print("You climb into the floor, congrats")
        else :
            print("You try to climb a ladder made of air, you fall flat on your face.")
    # Down
    elif (move == "4"):    
        if (Dungeon[Room][Floor] == "LadderDown") :
            print("You successfully climb down the ladder.")
            Floor -= 1
        elif(Dungeon[Room][Floor] == "LadderUp") :
            print("You attempt to climb down the ladder going up, and you are now on the floor.")
        else :
            print("You try to climb down ladder made of air into the floor, you are now laying on the ground.")
    input("Press enter to continue")   
def game_run() : 
    global Room
    global Floor
    Room = 0
    Floor = 0
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
def game_start() :
    print("You wake up disoriented.")
    continue_enter()
    print("The last thing you remember was experiencing aggressive marketing from Truck-kun.\n")
    game_run()
game_start()
