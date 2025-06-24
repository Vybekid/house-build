import turtle as t

# --- Setup ---
t.setup(800, 600)  # 1. A good, standard screen size
t.speed(0)         # 2. Draw instantly
t.hideturtle()     # 3. Hide the arrow for a clean look

# --- A single, powerful helper to draw any filled rectangle ---
def draw_box(x, y, width, height, color): # 4.
    t.penup() # 5.
    t.goto(x, y) # 6.
    t.pendown() # 7.
    t.fillcolor(color); t.begin_fill() # 8.
    for _ in range(2): t.forward(width); t.left(90); t.forward(height); t.left(90) # 9.
    t.end_fill() # 10.

# --- House Body & Door (using our helper) ---
draw_box(-200, -150, 200, 180, "white") # 11. Main house section
draw_box(0, -150, 150, 130, "white")    # 12. Side section (creates the L-shape)
draw_box(-40, -150, 60, 100, "red")     # 13. The red door

# --- Roof (custom shape, just like the video) ---
t.penup(); t.goto(-200, 30); t.pendown(); t.fillcolor("#A0522D"); t.begin_fill() # 14.
t.goto(0, 130); t.goto(150, -20); t.goto(0, -20); t.goto(-200, 30) # 15.
t.end_fill() # 16.

# --- Windows & Text (in a loop for efficiency) ---
for x_coord in [-150, 50, 50, 100]: # 17. Loop for the four windows
    y_coord = -10 if x_coord > 0 else -60 # A clever trick to set y-coordinates
    draw_box(x_coord, y_coord, 40, 40, "#ADD8E6") # Light blue fill
    t.penup(); t.goto(x_coord + 20, y_coord); t.pendown(); t.goto(x_coord + 20, y_coord + 40) # Vertical cross
    t.penup(); t.goto(x_coord, y_coord + 20); t.pendown(); t.goto(x_coord + 40, y_coord + 20) # Horizontal cross

t.penup(); t.goto(-150, 200); t.color("green"); t.pendown() # 18.
t.write("Please subscribe to our channel\n   Coding With Karthik", font=("Verdana", 16, "bold")) # 19.

t.done() # Keeps the window open