import turtle

wn = turtle.Screen()

#turtle module to add graphics and to open windows good for basic games or could use pygames

wn.title("pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)
#these 3 could be one genralized function
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
#paddle b 
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

paddle_ball=turtle.Turtle()
paddle_ball.speed(0)
paddle_ball.shape("square")
paddle_ball.color("white")

paddle_ball.penup()
paddle_ball.goto(0,0)
paddle_ball.dx = .3
paddle_ball.dy = .3

def paddle_a_up():
    #paddle_a is name of object we made
    #ycor returns y cordinate 
    y = paddle_a.ycor( )
    #add 20 pixels tp y 
    y+= 20
    paddle_a.sety(y)
    #listen for keyboard input


def paddle_a_down():
    #paddle_a is name of object we made
    #ycor returns y cordinate 
    y = paddle_a.ycor( )
    #add 20 pixels tp y 
    y-= 20
    paddle_a.sety(y)
    #listen for keyboard input

def paddle_b_up():
    #paddle_a is name of object we made
    #ycor returns y cordinate 
    y = paddle_b.ycor( )
    #add 20 pixels tp y 
    y+= 20
    paddle_b.sety(y)
    #listen for keyboard input





def paddle_b_down():
    #paddle_a is name of object we made
    #ycor returns y cordinate 
    y = paddle_b.ycor( )
    #add 20 pixels tp y 
    y-= 20
    paddle_b.sety(y)
    #listen for keyboard input

wn.listen()
#c
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
while True:
    wn.update()

    paddle_ball.setx(paddle_ball.xcor()+paddle_ball.dx)
    paddle_ball.sety(paddle_ball.ycor()+paddle_ball.dy)

    if paddle_ball.ycor()>290:
        paddle_ball.sety(290)
        paddle_ball.dy += -1
        
    
    if paddle_ball.ycor()< -290:
        paddle_ball.sety(-290)
        paddle_ball.dy += -1

    if paddle_ball.xcor()>390:
        paddle_ball.goto(0)
        paddle_ball.dx += -1

#paddle a 

#paddle b 
