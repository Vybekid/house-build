import turtle as tur
import colorsys as csys

tur.bgcolor('black')
tur.setup(1200, 800)
tur.width(2)
tur.speed(0)
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
    size = 150
    for i in range(6):
        tur.forward(size)
        tur.right(60)
        cur_pos = tur.pos()
        positions.append((cur_pos, tur.heading()))

    step = 4
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

go_to((-100, 150))
drawDesign()
tur.hideturtle()
tur.done()