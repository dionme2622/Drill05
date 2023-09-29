from pico2d import *
import random
WIDTH, HEIGHT = 1280, 1024
open_canvas(WIDTH, HEIGHT)

hand = load_image('hand_arrow.png')
character = load_image('run_animation.png')
tuk_ground = load_image('TUK_GROUND.png')
mx1, my1 = WIDTH // 2, HEIGHT // 2
running = True
frame = 0
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
def character_move(x , y):
    global frame, x1, x2
    tuk_ground.draw(WIDTH // 2, HEIGHT // 2)
    if(x1 > x2):
        character.clip_composite_draw(frame * 100, 0, 100, 100, 0, 'h', x, y,100, 100)
    else:
        character.clip_draw(frame * 100, 0, 100, 102, x, y)
    frame = (frame + 1) % 8

while running:
    mx2 = random.randint(0, WIDTH + 1)
    my2 = random.randint(0, HEIGHT + 1)
    x1, y1 = mx1, my1
    x2, y2 = mx2, my2

    for i in range(0, 100 + 1, 1):
        t = i / 100
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2
        character_move(x, y)
        hand.clip_draw(0, 0, 50, 52, mx2, my2)
        update_canvas()
        handle_events()
        delay(0.01)

    mx1, my1 = mx2, my2

close_canvas()



