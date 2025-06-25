import turtle as tur
import colorsys as csys

# --- Screen and Speed Setup ---
tur.bgcolor('black')
tur.setup(400, 400)    # Slimmer and shorter window
tur.width(2)
tur.speed(3)           # Slower speed
tur.tracer(4)

def go_to(pos):
    tur.up()
    tur.goto(pos[0], pos[1])
    tur.down()

def draw_hexagon(size):
    for i in range(1,7):
        tur.forward(size)
        tur.right(60)

def drawDesign():
    positions = []
    # --- ADJUSTED DRAWING SIZE ---
    size = 50              # Scaled down from 150 (150 / 3) to fit the new window
    for i in range(6):
        tur.forward(size)
        tur.right(60)
        cur_pos = tur.pos()
        positions.append((cur_pos, tur.heading()))

    # --- ADJUSTED STEP FOR VISUAL DETAIL ---
    step = 2               # Reduced from 4 to keep the lines looking dense
    inner_list = range(step, int(size/2)+step, step)
    inner_list_len = len(inner_list)
    for j,v in enumerate(inner_list):
        for i, (pos, angle) in enumerate(positions):
            go_to(pos)
            hue = i*1/6
            tur.seth(angle)
            tur.color(csys.hsv_to_rgb(hue, 1-(j+1)/inner_list_len, 1))
            start_pos = tur.pos()
            tur.forward(v)
            tur.right(60)
            draw_hexagon(size+v*3/4)
            go_to(start_pos)
            tur.seth(angle)

# --- ADJUSTED STARTING POSITION ---
go_to((-33, 50))       # Scaled down from (-100, 150) to center the smaller drawing
drawDesign()
tur.hideturtle()
tur.done()