import pgzrun
import random
import time

WIDTH= 450
HEIGHT= 450
next = 0
lines = []
sat = []
start = time.time()
gameover = False
win = False
for i in range(10):
    s = Actor("satellite")
    s.x = random.randint(50, 409)
    s.y = random.randint(50, 409)
    sat.append(s)

def draw():
    global total
    screen.blit("background", (0,0))
    no = 1
    for s in sat:
        s.draw()
        screen.draw.text(str(no), (s.x - 10, s.y - 30), color="white")
        no += 1
    for l in lines:
        screen.draw.line(l[0],l[1], "#FF0000")
    if next < 10:
        total = time.time() - start
        screen.draw.text(str(round(total, 2)), (10,30), color="white")
    else:
        screen.draw.text(str(round(total, 2)), (10,30), color="white")
    if win == True:
        screen.fill("#A7FFA7")
        screen.draw.text("TIME'S UP and you WIN!", center = (225,255), color = "black")
    if gameover == True:
        screen.fill("#FF9999")
        screen.draw.text("TIME'S UP and you LOSE!", center = (225,225), color = "black")

def on_mouse_down(pos):
    global next, lines, win
    if sat[next].collidepoint(pos):
        if next > 0:
            lines.append((sat[next-1].pos, sat[next].pos))
        next+=1
        if next == len(sat):
            win = True
    else:
        lines = []
        next = 0

def update():
    pass

def timesup():
    global gameover
    gameover = True

clock.schedule(timesup, 30.0)
pgzrun.go()