#!/usr/bin/python

def draw_game_board(size):
    vert = "|   "
    horz = " ---"

    for i in range(size):
        print horz * size
        print vert * (size + 1)
    print horz * size

if __name__ == "__main__":
    while True:
        s = raw_input("How big is your game board?")
        if s.isdigit():
            draw_game_board(int(s))
        else:
            exit()