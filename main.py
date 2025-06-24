import turtle as t

t.speed(0) # 1: Set fastest drawing speed

# 2: Helper function to move turtle without drawing
def go(x, y): t.penup(); t.goto(x, y); t.pendown()

# 3: Helper function to draw any filled rectangle
def rectangle(width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2): t.forward(width); t.left(90); t.forward(height); t.left(90)
    t.end_fill()

# 4: Main house structure (bottom floor)
go(-150, -150); rectangle(250, 180, "cyan")

# 5: Garage on the side
go(100, -150); rectangle(150, 130, "lightblue")

# 6: Second floor
go(-120, 30); rectangle(180, 100, "lightgreen")

# 7: Main Roof (a triangle, drawn manually)
go(-150, 30); t.fillcolor("maroon"); t.begin_fill()
t.goto(-20, 130) # 8: Go to roof peak
t.goto(100, 30) # 9: Go to other edge
t.end_fill() # 10: Finish roof

# 11: Garage Roof (flat)
go(100, -20); rectangle(150, 10, "gray")

# 12: Chimney
go(-90, 130); rectangle(30, 60, "brown")

# 13: Door
go(-40, -150); rectangle(60, 100, "brown")

# 14: Door knob (a tiny circle)
go(10, -100); t.fillcolor("yellow"); t.begin_fill(); t.circle(5); t.end_fill()

# 15: Bottom floor window
go(-110, -60); rectangle(50, 50, "white")

# 16: Garage window
go(150, -90); rectangle(50, 50, "white")

# 17: Top floor window 1
go(-90, 60); rectangle(50, 50, "white")

# 18: Top floor window 2
go(-10, 60); rectangle(50, 50, "white")

t.hideturtle() # 19: Hide the turtle arrow
t.done() # 20: Keep the window open