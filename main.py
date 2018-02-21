import pygame as pg
import random

pg.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)

WIDTH = 600
HEIGHT = 600

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Tic-Tac-Toe")
clock = pg.time.Clock()

grid = pg.Surface((WIDTH, HEIGHT))
pg.draw.line(grid, WHITE, (200, 0), (200, 600), 5)
pg.draw.line(grid, WHITE, (400, 0), (400, 600), 5)
pg.draw.line(grid, WHITE, (0, 200), (600, 200), 5)
pg.draw.line(grid, WHITE, (0, 400), (600, 400), 5)

cross = pg.Surface((180, 180))
pg.draw.line(cross, GREEN, (0, 0), (180, 180), 5)
pg.draw.line(cross, GREEN, (180, 0), (0, 180), 5)

circle = pg.Surface((180, 180))
pg.draw.circle(circle, RED, (90, 90), 90, 5)

menu = pg.Surface((400, 400))
pg.draw.rect(menu, WHITE, pg.Rect(0, 0, 400, 400), 0)

# gameboard[y][x]
gameboard = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

crosses_placed = 0
menu_open = False
is_selecting = True
running = True
while running:
    # Event loop, hämtar input 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                menu_open = True
        elif event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                gameboard_x = x // 200
                gameboard_y = y // 200
                if crosses_placed < 3:
                    # kolla om man vunnit (3 i rad)
                    if gameboard[gameboard_y][gameboard_x] == " ":
                        gameboard[gameboard_y][gameboard_x] = "x"
                        crosses_placed += 1
                        placed = False
                        while not placed:
                            computer_x = random.randint(0, 2)
                            computer_y = random.randint(0, 2)
                            if gameboard[computer_y][computer_x] == " ":
                                gameboard[computer_y][computer_x] = "o"
                                placed = True
                        print(gameboard)
                # FLyttar, tar bort och ändrar position på spelare
                else:
                    if is_selecting:
                        if gameboard[gameboard_y][gameboard_x] == "x":
                            gameboard[gameboard_y][gameboard_x] = " "
                            is_selecting = False
                    else:
                        if gameboard[gameboard_y][gameboard_x] != " ":
                            continue
                        gameboard[gameboard_y][gameboard_x] = "x"
                        is_selecting = True
                        while gameboard[computer_y][computer_x] != "o":
                            computer_x = random.randint(0, 2)
                            computer_y = random.randint(0, 2)
                        gameboard[computer_y][computer_x] = " "
                        c_x_NEW = random.randint(0, 2)
                        c_y_NEW = random.randint(0, 2)
                        while gameboard[c_y_NEW][c_x_NEW] != " " or (c_x_NEW == computer_x and c_y_NEW == computer_y):
                            # if x och o är på samma plats
                            c_x_NEW = random.randint(0, 2)
                            c_y_NEW = random.randint(0, 2)
                        gameboard[c_y_NEW][c_x_NEW] = "o"
                        print(gameboard)

                vert_gameboard = [[gameboard[0][0], gameboard[1][0], gameboard[2][0]],
                                  [gameboard[0][1], gameboard[1][1], gameboard[2][1]],
                                  [gameboard[0][2], gameboard[1][2], gameboard[2][2]]]

                diagonal_gameboard = [[gameboard[0][0], gameboard[1][1], gameboard[2][2]],
                                      [gameboard[0][2], gameboard[1][1], gameboard[2][0]]]

                for row in gameboard:
                    if row == ["x", "x", "x"]:
                        print("You won")
                    elif row == ["o", "o", "o"]:
                            print("Enemy won")
                for column in vert_gameboard:
                    if column == ["x", "x", "x"]:
                        print("You won")
                    elif column == ["o", "o", "o"]:
                        print("Enemy won")
                for diagonal in diagonal_gameboard:
                    if diagonal == ["x", "x", "x"]:
                        print("You won")
                    elif diagonal == ["o", "o", "o"]:
                        print("Enemy won")

    screen.fill(BLACK)
    screen.blit(grid, (0,0))
    for y, row in enumerate(gameboard):
        for x, value in enumerate(row):
            if value == "x":
                screen.blit(cross, (x * 200 + 10, y * 200 + 10))
            elif value == "o":
                screen.blit(circle, (x * 200 + 10, y * 200 + 10))
    if menu_open == True:
        screen.blit(menu, (100, 100))

    pg.display.flip()

#TODO: Fixa så när man vinner börjar den om och en ruta kommer upp som visar att man har vunnit
#TODO: Fixa svårighetsgrader och även ett inteface för att välja (enkel- random, mellan- och svår- )