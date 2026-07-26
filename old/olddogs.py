import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hex Road Builder")

WHITE = (240,240,240)
BLACK = (20,20,20)
GREEN = (50,150,80)
BLUE = (50,100,200)
RED = (220,50,50)
GRAY = (160,160,160)

clock = pygame.time.Clock()
won=False

# ---------- HEX HELPERS ----------

HEX_SIZE = 40

def hex_points(x,y):
    pts=[]
    for i in range(6):
        angle = math.radians(60*i)
        pts.append((
            x + HEX_SIZE*math.cos(angle),
            y + HEX_SIZE*math.sin(angle)
        ))
    return pts


def hex_center(col,row):
    x = 150 + col*HEX_SIZE*1.5
    y = 150 + row*HEX_SIZE*math.sqrt(3)

    if col % 2:
        y += HEX_SIZE*math.sqrt(3)/2

    return x,y


def edge_point(cx,cy,edge):
    a1 = math.radians(60*edge)
    a2 = math.radians(60*(edge+1))

    p1=(cx+HEX_SIZE*math.cos(a1),
        cy+HEX_SIZE*math.sin(a1))

    p2=(cx+HEX_SIZE*math.cos(a2),
        cy+HEX_SIZE*math.sin(a2))

    return (
        (p1[0]+p2[0])/2,
        (p1[1]+p2[1])/2
    )

def check_win():

    for city in cities:

        if len(city["roads"])==0:
            return False

    return True

# ---------- ROAD TOKENS ----------

tokens=[
    [0,3],       # straight
    [1,2],       # curve
    [0,2],       # curve
    [0,2,4],     # Y road
    [0,1,3],     # another Y
    [0,1,2,3],   # crossroads
    [0,2,4],
    [1,3],
    [0,3,5],
    [0,1,2,3,4,5] # peace sign / circle
]


def rotate(token):
    return [(x+1)%6 for x in token]


# ---------- BOARD ----------

cols=10
rows=8

board=[]

for c in range(cols):
    for r in range(rows):
        board.append({
            "col":c,
            "row":r,
            "roads":[],
            "city": random.random()<0.10
        })

cities = [tile for tile in board if tile["city"]]

current_token=random.choice(tokens)
score=0


def find_tile(mouse):
    mx,my=mouse

    for tile in board:
        cx,cy=hex_center(tile["col"],tile["row"])

        if math.dist((mx,my),(cx,cy)) < HEX_SIZE:
            return tile

    return None



# ---------- DRAW ----------

def draw():
    screen.fill(WHITE)

    for tile in board:

        cx,cy=hex_center(tile["col"],tile["row"])

        pygame.draw.polygon(
            screen,
            GREEN if tile["city"] else GRAY,
            hex_points(cx,cy)
        )

        pygame.draw.polygon(
            screen,
            BLACK,
            hex_points(cx,cy),
            2
        )

        # roads
        for edge in tile["roads"]:
            p=edge_point(cx,cy,edge)

            pygame.draw.circle(
                screen,
                RED,
                (int(p[0]),int(p[1])),
                7
            )

            # draw road from center to edge
            pygame.draw.line(
                screen,
                BLUE,
                (cx,cy),
                p,
                8
            )


    # current token preview

    pygame.draw.rect(
        screen,
        WHITE,
        (760,80,180,180)
    )

    pygame.draw.circle(
        screen,
        GRAY,
        (850,170),
        HEX_SIZE
    )

    for e in current_token:
        p=edge_point(850,170,e)
        pygame.draw.line(
            screen,
            BLUE,
            (850,170),
            p,
            8
        )

    font=pygame.font.SysFont(None,32)

    text=font.render(
        "R rotate | Click place",
        True,
        BLACK
    )

    screen.blit(text,(700,300))

    if won:

        font=pygame.font.SysFont(None,60)

        text=font.render(
            "YOU CONNECTED ALL CITIES!",
            True,
            (20,120,20)
        )

        screen.blit(text,(180,40))
    

    screen.blit(text,(180,40))

    pygame.display.flip()



# ---------- GAME LOOP ----------

running=True

while running:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False


        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_r:
                current_token=rotate(current_token)


        if event.type==pygame.MOUSEBUTTONDOWN:

            tile=find_tile(event.pos)

            if tile:

                # simple placement
               if not tile["roads"]:
                    tile["roads"]=current_token.copy()

                    current_token=random.choice(tokens)

                    if check_win():
                        won=True


    draw()
    clock.tick(60)


pygame.quit()
