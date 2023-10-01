import os
import random
from pico2d import*
os.chdir(os.path.dirname(os.path.abspath(__file__)))

TUK_WIDTH,TUK_HEIGHT=1280,1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
hand=load_image("hand_arrow.png")
ch=load_image("animation_sheet.png")
TUK_GROUND=load_image("TUK_GROUND.png")
x,y=TUK_WIDTH//2,TUK_HEIGHT//2
x0,y0=x,y
hand_x,hand_y=TUK_WIDTH//2,TUK_HEIGHT//2
clicks=[]
running=True
frame,num_of_moves,t=0,20,0
direction=0
def handle_events():
    global running,hand_x,hand_y,TUK_HEIGHT,clicks
    events=get_events()
    for event in events:
        if event.type==SDL_KEYDOWN:
            if event.key==SDLK_ESCAPE:
                running=False
        elif event.type==SDL_MOUSEMOTION:
            hand_x,hand_y=event.x,TUK_HEIGHT-event.y-1
        elif event.type==SDL_MOUSEBUTTONDOWN:
            clicks.append((event.x,TUK_HEIGHT-event.y-1))
            
while(running):
    clear_canvas()
    TUK_GROUND.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    ch.clip_draw(frame*100,direction*100,100,100,x,y)
    hand.draw(hand_x,hand_y)
    for click in clicks:
        hand.draw(click[0],click[1])
    handle_events()
    update_canvas()
    delay(0.03)
close_canvas()