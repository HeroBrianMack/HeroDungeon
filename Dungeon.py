print("test")
# Creating Empty 3x5 List
# Note: Possibly make 3D for future mapping
Dungeon = [[0] * 5] * 3
# Filling List
# Floor 1
Dungeon[0][0] = "Empty"
Dungeon[0][1] = "Sword"
Dungeon[0][2] = "Monster"
Dungeon[0][3] = "Ladder"
Dungeon[0][4] = "Empty"
# Floor 2
Dungeon[1][0] = "Ladder"
Dungeon[1][1] = "Monster"
Dungeon[1][2] = "Stone"
Dungeon[1][3] = "Ladder"
Dungeon[1][4] = "Sword"
# Floor 3
Dungeon[2][0] = "Ladder"
Dungeon[2][1] = "Sword"
Dungeon[2][2] = "Gate"
Dungeon[2][3] = "Boss"
Dungeon[2][4] = "End"

def game_run() : 
    gameEnd = False
    while not gameEnd:
        gameEnd = True
def game_start() :
    print("You wake up disoriented.")
    input("Press enter to continue")
    print("The last thing you remember was some aggressive marketing from Truck-kun.\n")
    game_run()
game_start()