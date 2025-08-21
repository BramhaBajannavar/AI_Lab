# Define room size
ROWS, COLS = 5, 5
room = [["." for _ in range(COLS)] for _ in range(ROWS)]

# Robot starts at top-left corner
robot_pos = [0, 0]

# Movement functions
def move(direction):
    r, c = robot_pos
    if direction == "up" and r > 0:
        robot_pos[0] -= 1
    elif direction == "down" and r < ROWS - 1:
        robot_pos[0] += 1
    elif direction == "left" and c > 0:
        robot_pos[1] -= 1
    elif direction == "right" and c < COLS - 1:
        robot_pos[1] += 1
    # Clean the tile
    room[robot_pos[0]][robot_pos[1]] = "C"

# Clean starting tile
room[robot_pos[0]][robot_pos[1]] = "C"

# Zigzag cleaning pattern
for r in range(ROWS):
    if r % 2 == 0:
        # Move right across the row
        for _ in range(1, COLS):
            move("right")
    else:
        # Move left across the row
        for _ in range(1, COLS):
            move("left")
    # Move down to next row if not last
    if r < ROWS - 1:
        move("down")

# Print cleaned room
print("🧹 Room after cleaning:")
for row in room:
    print(" ".join(row))
