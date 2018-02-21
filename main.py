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

gameboard = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

crosses_placed = 0
is_selecting = True
# gameboard[y][x]
running = True
while running:
    # Event loop, hämtar input 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                gameboard_x = x // 200
                gameboard_y = y // 200
                if crosses_placed < 3:
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


#TODO: Fixa så computer och x inte kan placera spelare på varandra (while loop kolla tills man hittar o)
#TODO: Fixa så när man vinner börjar den om och en ruta kommer upp som visar att man har vunnit
#TODO: Fixa svårighetsgrader och även ett inteface för att välja (enkel- random, mellan- och svår- )
                        

    screen.fill(BLACK)
    screen.blit(grid, (0,0))
    for y, row in enumerate(gameboard):
        for x, value in enumerate(row):
            if value == "x":
                screen.blit(cross, (x * 200 + 10, y * 200 + 10))
            elif value == "o":
                screen.blit(circle, (x * 200 + 10, y * 200 + 10))
    #TODO: Välja vilken man vill flytta och även flytta motståndaren 
    pg.display.flip()