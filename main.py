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
                            computer_y  = random.randint(0, 2)
                            if gameboard[computer_y][computer_x] == " ":
                                gameboard[computer_y][computer_x] = "o"
                                placed = True
                        print(gameboard)
                else:
                    pass
    screen.fill(BLACK)
    screen.blit(grid, (0,0))
    for y, row in enumerate(gameboard):
        for x, value in enumerate(row):
            if value == "x":
                screen.blit(cross, (x * 200 + 10, y * 200 + 10))
            elif value == "o":
                screen.blit(circle, (x * 200 + 10, y * 200 + 10))
    #TODO: Add circle for computer and fix so that you only can place 3 
    pg.display.flip()