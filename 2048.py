import random 
import pygame
import math

pygame.init()
FPS = 120

WIDTH, HEIGHT = 800, 800

ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH =  WIDTH // COLS

OUTLINES_COLOR = (187,173,160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205,192,180)
FONT_COLOR = (119,110,101)


FONT = pygame.font.SysFont("comicsans", 80, bold = True)
MOVE_VEL = 20

ERROR_CHECK = 0

MOVED = False

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

class Tile:
    COLORS = [
        (237,229,218),
        (28,225,201),
        (243,178,122),
        (246,150,101),
        (237,124,95),
        (237,209,115),
        (237,209,99),
        (237,209,80)
    ]

    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = col*RECT_WIDTH
        self.y = row* RECT_HEIGHT

    def get_colour(self):
        colour_index= int(math.log2(self.value)-1)
        colour = self.COLORS[colour_index]
        return colour

    def draw(self,window):
        colour = self.get_colour()
        pygame.draw.rect(window,colour,(self.x,self.y,RECT_WIDTH,RECT_HEIGHT))

        text = FONT.render(str(self.value),1,FONT_COLOR)
        window.blit(
            text, 
            (
                self.x+RECT_WIDTH/2-text.get_width()/2,
                self.y+RECT_HEIGHT/2-text.get_height()/2
            )
            )

    def move(self,delta):
        self.x += delta[0]
        self.y += delta[1]

    def set_pos(self, ceil = False):
        if ceil:
            self.row = math.ceil(self.y / RECT_HEIGHT)
            self.col = math.ceil(self.x/RECT_WIDTH)
        else:
            self.row = math.floor(self.y / RECT_HEIGHT)
            self.col = math.floor(self.x/RECT_WIDTH)

        






def draw_grid(window):
    for row in range(1,ROWS):
        Y = row * RECT_HEIGHT
        pygame.draw.line(window, OUTLINES_COLOR,(0,Y),(WIDTH,Y), OUTLINE_THICKNESS)
    for col in range(1,COLS):
        X = col *RECT_WIDTH
        pygame.draw.line(window, OUTLINES_COLOR,(X,0),(X,HEIGHT), OUTLINE_THICKNESS)
    
    pygame.draw.rect(window, OUTLINES_COLOR, (0,0, WIDTH, HEIGHT), OUTLINE_THICKNESS)





def draw(window, tiles):
    window.fill(BACKGROUND_COLOR)

    for tile in tiles.values():
        tile.draw(window)

    draw_grid(window)
    


    pygame.display.update()


def get_random_pos(tiles):
    row = None
    col = None
    while True:
        row = random.randrange(0, ROWS)
        col = random.randrange(0,COLS)

        if f"{row}{col}" not in tiles:
            break

    return row, col

def move_tiles(window, tiles, clock, direction):
    updated = True
    global MOVED
    MOVED = False

    blocks = set()

    if direction == "left":
        sort_func = lambda x: x.col
        reverse = False
        delta = (-MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col-1}")
        merge_check = lambda tile, next_tile: tile.x > next_tile.x + MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.x > next_tile.x + RECT_WIDTH + MOVE_VEL
        )
        ceil = True


    elif direction == "right":
        sort_func = lambda x: x.col
        reverse = True
        delta = (MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == COLS - 1
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col+1}")
        merge_check = lambda tile, next_tile: tile.x < next_tile.x - MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.x+ RECT_WIDTH + MOVE_VEL < next_tile.x 
        )
        ceil = False
    elif direction == "up":
        sort_func = lambda x: x.row
        reverse = False
        delta = (0, -MOVE_VEL)
        boundary_check = lambda tile: tile.row == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row-1}{tile.col}")
        merge_check = lambda tile, next_tile: tile.y > next_tile.y + MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.y > next_tile.y + RECT_WIDTH + MOVE_VEL
        )
        ceil = True
    elif direction == "down":
        sort_func = lambda x: x.row
        reverse = True
        delta = (0, MOVE_VEL)
        boundary_check = lambda tile: tile.row == ROWS - 1
        get_next_tile = lambda tile: tiles.get(f"{tile.row+1}{tile.col}")
        merge_check = lambda tile, next_tile: tile.y < next_tile.y - MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.y + RECT_WIDTH + MOVE_VEL< next_tile.y 
        )
        ceil = False

    while updated:
        clock.tick(FPS)
        updated = False
        sorted_tiles = sorted(tiles.values(), key = sort_func, reverse=reverse)

        for i, tile in enumerate(sorted_tiles):
            if boundary_check(tile):
                continue
            next_tile = get_next_tile(tile)

            if not next_tile:
                tile.move(delta)
                MOVED = True

            elif tile.value == next_tile.value and tile not in blocks and next_tile not in blocks:
                MOVED = True
                if merge_check(tile,next_tile):
                    tile.move(delta)
                    
                else:
                    next_tile.value *= 2
                    sorted_tiles.pop(i)
                    blocks.add(next_tile)

            elif move_check(tile, next_tile):
                tile.move(delta)
                MOVED = True
            else:
                continue

            tile.set_pos(ceil)
            updated = True
        update_tiles(window, tiles, sorted_tiles)
    end_move(tiles)

def end_move(tiles):
    if len(tiles) == 16:
        return "lost"
    
    if MOVED == True:
        row, col = get_random_pos(tiles)
        tiles[f"{row}{col}"] = Tile(random.choice([2,4]), row, col)



def update_tiles(window, tiles, sorted_tiles):
    tiles.clear()
    for tile in sorted_tiles:
        tiles[f"{tile.row}{tile.col}"] = tile  

    draw(window, tiles)  


def generate_tiles():
    tiles = {}
    for _ in range(2):
        row, col = get_random_pos(tiles)
        tiles[f"{row}{col}"] = Tile(2, row, col)
    return tiles

def main(window):
    clock = pygame.time.Clock()
    run = True

    #make dictionary because it's more handy for index finding
    tiles = generate_tiles()

    while run:
        #Tick FPS is used to level out computer speed: without fast computers would run code faster and slow slower
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    move_tiles(window,tiles,clock,"left")
                if event.key == pygame.K_RIGHT:
                    move_tiles(window,tiles,clock,"right")
                if event.key == pygame.K_UP:
                    move_tiles(window,tiles,clock,"up")              
                if event.key == pygame.K_DOWN:
                    move_tiles(window,tiles,clock,"down")
        


        draw(window, tiles)

    pygame.quit()








if __name__ == "__main__":
    main(WINDOW)
