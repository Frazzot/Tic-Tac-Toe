import pygame as pg

pg.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255, 0, 0)

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
pg.draw.line(cross, RED, (0, 0), (180, 180), 5)
pg.draw.line(cross, RED, (180, 0), (0, 180), 5)

gameboard = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
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
                if gameboard[gameboard_y][gameboard_x] == " ":
                    #pg.draw.line(cross, RED, (gameboard_x * 200, gameboard_y * 200), (gameboard_x * 200 + 200, gameboard_y * 200 + 200), 5)
                    gameboard[gameboard_y][gameboard_x] = "x"
                    print(gameboard)
#TODO: Kolla musens koordinater, därefter kolla om något är ritat i rutan
        
# floordiv av koordinat y och x med 200 separat (if value == 0, 1 eller 2 sätt i olika rutor)
    screen.fill(BLACK)
    screen.blit(grid, (0,0))
    for y, row in enumerate(gameboard):
        for x, value in enumerate(row):
            if value == "x":
                screen.blit(cross, (x * 200 + 10, y * 200 + 10))


    # Utför beräkningar
    # Uppdatera positioner
    pg.display.flip()