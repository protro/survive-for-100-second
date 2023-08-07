import pgzrun
import random
import easygui as g
import time
WIDTH = 600  
HEIGHT = 800 
t = 0 
pIndex=0
try:
    ship = int(str(g.enterbox(msg="what kind of plane(1-9)?", title="100 second")))
    time.sleep(1)
    title = g.msgbox(msg="use k to become small",title="special",ok_button="OK")
    time.sleep(1)
    islose=False
    lives=3
    win=False
    if ship == 1:
        hero = [Actor('0'), Actor('0.1'), Actor('hero_blowup')]
    if ship == 2:
        hero = [Actor('1'), Actor('0.1'), Actor('hero_blowup')]
    if ship == 3:
        hero = [Actor('2'), Actor('0.1'), Actor('hero_blowup')]
    if ship == 4:
        hero = [Actor('3'), Actor('0.1'), Actor('hero_blowup')]
    if ship == 5:
        hero = [Actor('4'), Actor('0.1'), Actor('hero_blowup')]
    if ship == 6:
        hero = [Actor('5'), Actor('0.1'), Actor('hero_blowup')]
    if ship == 7:
        hero = [Actor('6'), Actor('0.1'), Actor('hero_blowup')]
    if ship == 8:
        hero = [Actor('7'), Actor('0.1'), Actor('hero_blowup')]
    if ship == 9:
        hero = [Actor('8'), Actor('0.1'), Actor('hero_blowup')]
    if ship > 9 or ship < 1:
        hero = [Actor('7'), Actor('0.1'), Actor('hero_blowup')]

    bg1 = Actor('background')
    bg1.x = WIDTH / 2
    bg1.y = HEIGHT / 2
    bg2 = Actor('background')
    bg2.x = WIDTH / 2
    bg2.y = -HEIGHT / 2
    class Ball:
        x = None
        y = None
        vx = None   
        vy = None   
        radius = None   
        color = None    

        def __init__(self, x, y, vx, vy, radius, color):
            self.x = x
            self.y = y
            self.vx = vx
            self.vy = vy
            self.radius = radius
            self.color = color

        def draw(self):
            screen.draw.filled_circle((self.x, self.y), self.radius, self.color)

        def update(self):
            self.x += self.vx 
            self.y += self.vy

            if self.x > WIDTH-self.radius or self.x < self.radius:
                self.vx = -self.vx

            if self.y > HEIGHT-self.radius or self.y < self.radius:
                self.vy = -self.vy


    balls = [] 


    def draw():
        global pIndex,t
        screen.fill('white')
        bg1.draw()
        bg2.draw() 
        for ball in balls:
            ball.draw() 

        if islose == False:
            hero[pIndex].draw()
        else:
            hero[2].draw()
            if pIndex == 0:
                hero[2].x = hero[0].x
                hero[2].y = hero[0].y
            if pIndex == 1:
                hero[2].x = hero[1].x
                hero[2].y = hero[1].y
        screen.draw.text('time:' + str(t), (10, 10),fontsize=30, color='red', fontname='main')
        screen.draw.text('lives:' + str(lives), (WIDTH-150, 10),fontsize=30, color='red', fontname='main')
        if islose:
            screen.draw.text('fail', (200, HEIGHT / 2),
                             fontsize=70, color='red', fontname='main')
        if win:
            screen.draw.text('win', (2500, HEIGHT / 2),
                             fontsize=70, color='red', fontname='main')

    def update():
        global pIndex,lives,islose,win
        if lives<=0:
            islose=True  
            return 
        if t==100:
            win=True
            return
        for ball in balls:
            ball.update()
            if pIndex==1:
                if abs(hero[pIndex].x - ball.x)< 8 and abs(hero[pIndex].y - ball.y)< 8:
                    ball.x=99999
                    ball.y=99999
                    lives-=1
            if pIndex==0:
                if abs(hero[pIndex].x - ball.x)< 16 and abs(hero[pIndex].y - ball.y)< 16:
                    ball.x=99999
                    ball.y=99999
                    lives-=1
        if bg1.y > HEIGHT / 2 + HEIGHT:
            bg1.y = -HEIGHT / 2
        if bg2.y > HEIGHT / 2 + HEIGHT:
            bg2.y = -HEIGHT / 2
        bg1.y += 1
        bg2.y += 1           
        if keyboard.k:
            pIndex = 1
        else:
            pIndex = 0
        print(lives)



    def count(): 
        global t
        t+=1
        if lives<=0:
            islose=True  
            return 
        if t==100:
            win=True
            return
        if t % 1==0 :
            x=WIDTH//2
            y=random.randint(5,HEIGHT//10)
            vx = random.choice([10,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3])
            vy = random.choice([10,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3,-3,-2,-1,1,2,3])
            r = 3
            ball =Ball(x,y,vx,vy,r,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            balls.append(ball)
        clock.schedule_unique(count,1)

    def on_mouse_move(pos):
        global pIndex
        if islose == False:
            if pIndex == 0:

                hero[0].x = pos[0]
                hero[0].y = pos[1]
                hero[1].x = 9999
                hero[1].y = 9999
            if pIndex == 1:

                hero[0].x = 9999
                hero[0].y = 9999
                hero[1].x = pos[0]
                hero[1].y = pos[1]

    count()
    pgzrun.go()
except:
    title = g.msgbox(msg="can only enter a number",title="error",ok_button="OK")
    

