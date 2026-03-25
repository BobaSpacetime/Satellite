import pgzrun
import random

WIDTH= 450
HEIGHT= 450

sat = []
for i in range(10):
    s = Actor("satellite")
    s.x = random.randint(50, 409)
    s.y = random.randint(50, 409)
    sat.append(s)
no = 1

def draw():
    screen.blit("background", (0,0))
    for s in sat:
        s.draw()
        screen.draw.text(str(no), (s.x, s.y))

pgzrun.go()