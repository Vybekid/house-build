import turtle as t

t.setup(400, 600); t.speed('normal')
t.hideturtle(); t.pensize(3)

def go(x, y):
    t.penup()
    t.goto(x, y); t.pendown()

def draw_box(width, height, color):
    t.fillcolor(color); t.begin_fill()

    for _ in range(2):
        t.forward(width); t.left(90)
        t.forward(height); t.left(90)
    t.end_fill()

go(-160, -150); draw_box(160, 180, "white")
go(0, -150); draw_box(120, 130, "white")    

go(-160, 30); t.fillcolor("#A0522D")
t.begin_fill()
t.goto(-80, 130)   
t.goto(0, 30)
t.goto(120, 30)    
t.goto(120, -20)   
t.goto(0, -20)
t.goto(0, 30)
t.end_fill()

go(-50, -150); draw_box(50, 110, "red")    
go(-40, -100); t.dot(10, "gold")             
for x, y in [(-120, -50), (25, -80), (75, -80)]: 
    go(x, y); draw_box(35, 35, "#ADD8E6") 
    go(x+17.5, y); t.goto(x+17.5, y+35)
    go(x, y+17.5); t.goto(x+35, y+17.5)

t.done()