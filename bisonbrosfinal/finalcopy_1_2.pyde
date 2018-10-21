def setup():
    global x, y, back_counter, background_1, bison1, bison2, buck1, powerup, direction, b1, b2, b3, pirates, px, py, play, bb_logo, play_logo, contact, selectMode, background_1, grow, score, var_left, win
    size(600, 385)
    bb_logo = loadImage("bisonbroslogo.png")
    play_logo = loadImage("play_word.png")
    image(bb_logo, 20, 5, 600, 200)
    play = False
    x = 0
    y = 270
    px = 600
    py = 260
    back_counter = 0
    background_1 = loadImage("background1.png")
    b1 = True
    b2 = False 
    b3 = False
    background(background_1)
    bison1 = loadImage("bison1.png")
    #buck1 = loadImage("dollar.png")
    powerup = loadImage("apic.jpg")
    bison2 = loadImage("bison2.gif")
    image(bison1, x, y)
    image(powerup, x, y)
    #image(buck1, x, y)
    image(bison2, x, y)
    direction = 0
    pirates = loadImage("0.png")
    pirates.resize(100, 70)
    size(600,385)
    background(255)
    contact = False
    score = 0
    grow = False
    var_left = 0
    win = False
    
def draw():
    global x, y, back_counter, background_1, bison1, bison2, buck1, powerup, direction, b1, b2, b3, pirates, px, py, play, bb_logo, play_logo, contact, score, grow, background_1, var_left, win
    image(bb_logo, 20, 5, 600, 200)
    fill(random(50,200), 247, 165)
    rect(240,250,150,50,7)
    image(play_logo,235,250,160,70)
    if mousePressed:
        if mouseY >= 250 and mouseY <= 300:
            play = True
    if play == True:
        fill(255)
        
        global play_logo, selectMode
        fill(random(50,200), 247, 165)
        rect(240,250,150,50,7)
        image(play_logo,235,250,160,70)
                
        if b1 == True:
            if direction == 1:
                if y > 230:
                    y = y - 2
                if y < 231:
                    direction = 2
            
            if direction == 2:
                if y <= 272:
                    y = y + 2
                    
        background(background_1)
        
        if back_counter == 0:
            image(powerup, 300, 230)
            if x >= 250 and x <= 290 and y <= 232 and y >= 229:
                powerup.resize(1,1)
                score += 1

        if back_counter == 1:
            image(powerup, 250, 264)
            if x >= 210 and x <= 232 and y <= 264 and y >= 263:
                powerup.resize(1,1)
                score += 1
        
        image(bison1, x, y)
        
        textSize(15)
        text("Bison Bucks:",50,40)
        text(str(score),50,60)
            
        if keyPressed == True:
            if keyCode == LEFT:
                x = x - 2  
                if x < 0:
                    x = 0
                    
            if keyCode == RIGHT:
                x = x + 2 
                
            if keyCode == UP:
                direction = 1
            
        print(x, y)
        
        if x >= 600 and back_counter == 0:
            powerup.resize(30,30)
            contact = False
            px = 500
            py = 290
            image(pirates, px, py)
            var_left = 0
            b1 = False
            b2 = True
            background_1 = loadImage("background2.jpg")
            powerup = loadImage("apic.jpg")
            x = 0
            y = 302
            back_counter += 1
        elif x >= 600 and back_counter == 1:
            b1 = False
            b2 = False
            b3 = True
            background_1 = loadImage("background3.jpg")
            x = 0
            y = 294
            back_counter += 1
            
        elif x >= 225 and back_counter == 2:
            background(0)
            win = True
            bison1.resize(1,1)
            
        if win == True:
            background_1 = loadImage("youwin2.png")
            background(background_1)

            
            
            
        if b2 == True:
            if direction == 1:
                if y > 262:
                    y = y - 2
                if y < 263:
                    direction = 2
            if direction == 2:
                if y <= 300:
                    y = y + 2
        if b3 == True:
            if direction == 1:
                if y > 254:
                    y = y - 2
                if y < 255:
                    direction = 2
            if direction == 2:
                if y <= 292:
                    y = y + 2
            
        
        var_left = 0
        image(pirates, px, py)
        if var_left == 0:
            px -= 1
        var_left = 0
        if px <= x + 15:
            if py <= y - 5:
                contact = True
        if contact == True:
            px = px + 20 
            py = py - 20
        if px >= x + 400 and contact == True:
            score += 15
            contact = False
                
