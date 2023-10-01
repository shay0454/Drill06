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
x1,y1=x,y
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
    hand.draw(hand_x,hand_y)
    if x==x1 and y==y1:
        if len(clicks)!=0:
            x1,y1=clicks[0][0],clicks[0][1]
            if x1>x:
                direction=1
            elif x1<x:
                direction=0
            if x1==x and y1==y:
                x0,y0=x,y
                del clicks[0]
        else:
            ch.clip_draw(0,direction*100+200,100,100,x,y)
    else:
        ch.clip_draw(frame*100,direction*100,100,100,x,y)
        per=1/num_of_moves
        x,y=(1-per*t)*x0+per*t*x1,(1-per*t)*y0+per*t*y1
        t=(t+1)%(num_of_moves+1)
        frame=(frame+1)%8
    for click in clicks:
        hand.draw(click[0],click[1])
    update_canvas()
    handle_events()
    delay(0.03)
close_canvas()