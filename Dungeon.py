print("test")
# Creating Empty 3x5 List
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
print(Dungeon)