def setup():
    size(400, 400)
    textSize(120)
    textAlign(CENTER)
    fill(255)

def draw():
    print(mouseX, mouseY)
    
    if mousePressed:
        text("D", width/2-75, height/2)
        text("T", width/2+75, height/2)
   
     #najeżdżanie    
    if (mouseX >= 90 and mouseX <= 163 and mouseY >= 113 and mouseY <= 200):
        fill(255, 255, 0)
        text("D", width/2-75, height/2)
        fill(250)
        
    if (mouseX >= 237 and mouseX <= 311 and mouseY >= 113 and mouseY <= 200):
        fill(255, 255, 0)
        text("T", width/2+75, height/2)
        fill(250)
        
        
 
    if keyPressed:
        if key == "d" or key == "D": #klikam d i sie koloruje
            text("D", width/2-75, height/2)
            fill(255, 0, 255)
                
        if key == "t" or key == "T": #klikam t i sie koloruje
            text("T", width/2+75, height/2)
            fill(255, 0, 255)


        if keyCode == 39: #prawa strzałka i zmienia kolor
            text("T", width/2+75, height/2)
            fill(255, 0, 0)

        
        if keyCode == 37: #lewa i zmienia
            text("T", width/2+75, height/2)
            fill(255, 0, 0)
    


        
    s = createShape() #dziwnepodkreślenie
    s.beginShape()
    s.fill(0,0,255,100)
    s.noStroke()
    s.vertex(50, (height/4)*3)
    s.vertex(width/2-20, (height/4)*3+30)
    s.vertex(width/4, (height/4)*3)
    s.vertex(width-2, (height/4)*3)
    s.vertex(width, (height/5)*3)
    s.endShape(CLOSE)
    shape(s,25,25)
