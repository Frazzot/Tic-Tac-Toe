import pygame as pg

pg.init()

WHITE = (255,255,255)
BLACK = (0,0,0)

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
                pos[0] = 
                pos[1] = 
#TODO: Kolla musens koordinater, därefter kolla om något är ritat i rutan
        
# floordiv av koordinat y och x med 200 separat (if value == 0, 1 eller 2 sätt i olika rutor)

    # Utför beräkningar
    # Uppdatera positioner
    
    screen.fill(BLACK)
    screen.blit(grid, (0,0))
    pg.display.flip()