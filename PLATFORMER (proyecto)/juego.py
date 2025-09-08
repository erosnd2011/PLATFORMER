import pgzrun

size_w = 10
size_h = 10

WIDTH = size_w * 64
HEIGHT = size_h * 48

bunny = Actor("bunny", (320,200))
platform = Actor("platform")
button_play = Actor("button", (320, 200))
button_skins = Actor("button", (320, 250))
button_extra = Actor("button", (320, 150))
mode = "menu"

my_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1 ,0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
def map_draw():
    for i in range(len(my_map)):
        for j in range(len(my_map[0])):
            if my_map[i][j]==0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            if my_map[i][j]==1:
                cell1.left = cell.width*j
                cell1.top = cell.height*i
                cell1.draw()


def draw():
    if mode == "menu":
        screen.clear()
        screen.blit("menu", (0,0))
        button_play.draw()
        button_skins.draw()
        button_extra.draw()
        screen.draw.text( "PLAY", center=button_play.pos, fontsize=30, color="black")
        screen.draw.text( "SKINS", center=button_skins.pos, fontsize=30, color="black")
        screen.draw.text( "", center=button_extra.pos, fontsize=30, color="black")
    elif mode == "game":
        screen.clear()
        screen.blit("bg", (0,0))
    

        platform.draw()
    elif mode == "skins":
        screen.fill((20,35,20))
def on_mouse_down(pos):
    global mode
    if mode == "menu":
        if button_play.collidepoint(pos):
            mode = "game"
        elif button_skins.collidepoint(pos):
            mode = "skins"
pgzrun.go()