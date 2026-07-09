#First game
#Snake game

#Imports
import turtle
import time
delay = 0.1
score = 0
highscore = 0
import random as rd


#Functions

def move():

    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

wn = turtle.Screen()
wn.title("Snake game by @LarshVakil")
wn.bgcolor('green')
wn.setup(height=820,width=820)
wn.tracer(0)


#Pen


pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0 Highscore:0" , align="center", font  =("Courier" , 24 , "normal"))
#Controls

wn.listen()
wn.onkeypress(go_up , "w")
wn.onkeypress(go_down , "s")
wn.onkeypress(go_left , "a")
wn.onkeypress(go_right , "d")



#Making snake

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("purple")
head.shapesize(1.2)
head.penup()
head.goto(0,0)
head.direction = 'stop'
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
food.direction = 'stop'

segments = []

while True:

    for segment in segments:
         if head.distance(segment)< 20:
            time.sleep(1)          
            head.goto(0, 0)        
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score:{} Highscore:{}".format(score, highscore), align="center", font=("Courier", 24, "normal"))
            break
              
         
    if head.distance(food) <20:
        
        score += 1 
        if score> highscore:
             highscore = score

        pen.clear()
        pen.write("Score:{} Highscore:{} ".format(score, highscore), align="center", font=("Courier", 24, "normal"))

        x = rd.randint(-290,290)
        y = rd.randint(-290,290)
        food.goto(x,y)

        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("black")
        segment.penup()
        segments.append(segment )

        delay -=0.001
#Moving the last segments first 
    for i in range(len(segments )-1 ,0 ,-1):
            x = segments[i-1].xcor()
            y = segments[i-1].ycor()
            segments[i].goto(x,y)

    if len(segments)>0:
            x = head.xcor()
            y= head.ycor()
            segments[0].goto(x,y)

    if head.xcor() > 390 or head.xcor() < -390 or head.ycor() > 390 or head.ycor() < -390:
        time.sleep(1)          
        head.goto(0, 0)        
        head.direction = "stop"
        for segment in segments:
             segment.goto(1000,1000)

        segments.clear()
        score = 0
        delay = 0.1





    wn.update()
    move()
    time.sleep(delay)


wn.mainloop()

