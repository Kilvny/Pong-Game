import turtle
import winsound

def window_init():
    window = turtle.Screen()
    window.setup(width=800,height=500)
    window.bgcolor('gray')
    window.tracer(0)
    window.title('MyPythonWindow')
    return window

class shape(turtle.Turtle):

    playerOneScore = 0
    playerTwoScore = 0    
    def __init__(self,name, shape: str = ..., undobuffersize: int = ..., visible: bool = ...) -> None:
        super().__init__(shape, undobuffersize, visible )
        self.name = name
        # self.color = color
        self.penup() # to make it-won't draw lines behind it when it moved
        self.speed(0) # 'fastest' : 0
        
    def defaultPosition(self,x:float,y:float):
        self.goto(x,y)
        if x == 0 and y == 0: # in case the shape is the ball 
            self.xAxis = 0.4 # how fast the shape disipline
            self.yAxis = 0.4 # how fast on y axis

    def shapeSize(self,width:float,length:float):
        self.shapesize(width,length)
    
    def moveUp(self):
        y = self.ycor() # Return the turtle's y coordinate
        y += 20 # move on the y coordinate by this value
        self.sety(y)

    def moveDown(self):
        y = self.ycor() 
        y -= 20 
        self.sety(y)

    def moveBall(self,scoreboard):
        self.setx(self.xcor()+self.xAxis)
        self.sety(self.ycor()+self.yAxis)
        if self.ycor() > 240:
            self.sety(240) # ball rebounds 
            self.yAxis *= -1 
            winsound.PlaySound('D:/python/python games/PongGame/bounce.wav',winsound.SND_ASYNC)            
        if self.xcor() > 390:
            self.goto(0,0) # ball goes to origin and reverse it's direction 
            self.xAxis *= -1
            self.playerOneScore +=1
            scoreboard.clear()
            scoreboard.write(f'Player One :{self.playerOneScore} Player Two :{self.playerTwoScore}',align='center',font=('Courier',24,'normal'))
            winsound.PlaySound('D:/python/python games/PongGame/Goal.wav',winsound.SND_ASYNC)
        if self.ycor() < -240: # same for y
            self.sety(-240)
            self.yAxis *= -1
            winsound.PlaySound('D:/python/python games/PongGame/bounce.wav',winsound.SND_ASYNC)            
        if self.xcor() < -390: # same for x
            self.goto(0,0)
            self.xAxis *= -1
            self.playerTwoScore +=1
            scoreboard.clear()
            scoreboard.write(f'Player One :{self.playerOneScore} Player Two :{self.playerTwoScore}',align='center',font=('Courier',24,'normal'))
            winsound.PlaySound('D:/python/python games/PongGame/Goal.wav',winsound.SND_ASYNC)
            


    def didPaddleXball(self,ball):
        # for the right of the screen
        if (ball.xcor() > 340 and ball.xcor() < 350)                                                                                         and (ball.ycor() < self.ycor() + 40 ) and (ball.ycor() > self.ycor() - 40):
            ball.setx(340)
            ball.xAxis *= -1
            winsound.PlaySound('D:/python/python games/PongGame/paddle.wav',winsound.SND_ASYNC)            

        # for the left 
        if (ball.xcor() < -340 and ball.xcor() > -350)                                                                                         and (ball.ycor() < self.ycor() + 40 ) and (ball.ycor() > self.ycor() - 40):
            ball.setx(-340)
            ball.xAxis *= -1
            winsound.PlaySound('D:/python/python games/PongGame/paddle.wav',winsound.SND_ASYNC)            









def game_init(win):
    global playerOnePaddle,playerTwoPaddle,ball,scoreboard


    playerOnePaddle = shape(name='P1',shape='square',visible=True,undobuffersize=100)

    playerTwoPaddle = shape(name='P2',shape='square',visible=True,undobuffersize=100)

    ball = shape(name='ball',shape='circle',visible=True,undobuffersize=100)

    scoreboard = shape(name='scoreboard',shape='square',undobuffersize=100)    

    # paddle one : 
    playerOnePaddle.defaultPosition(-350,0)
    playerOnePaddle.shapeSize(5,1)
    playerOnePaddle.color('red')
    # paddle two:
    playerTwoPaddle.defaultPosition(350,0)
    playerTwoPaddle.shapeSize(5,1)
    playerTwoPaddle.color('red')
    # ball: 
    ball.defaultPosition(0,0)
    # score sheet setting: 
    scoreboard.speed(0)
    scoreboard.color('white')
    scoreboard.hideturtle()
    scoreboard.defaultPosition(0,200)
    scoreboard.write(f'Player One :0 Player Two :0',align='center',font=('Courier',24,'normal'))

    # move the paddles : 
    # onkeypress: (fun: () -> object, key: str | None = ...) -> None Bind fun to key-press event of key if key is clicked 
    
    win.listen()
    win.onkeypress(playerOnePaddle.moveUp,key='w') 
    win.onkeypress(playerOnePaddle.moveDown,'s') 
    win.onkeypress(playerTwoPaddle.moveUp,'Up') 
    win.onkeypress(playerTwoPaddle.moveDown,'Down') 

           




if __name__ == '__main__':
    win = window_init()
    game_init(win)

    while True:
        win.update()
        ball.moveBall(scoreboard=scoreboard)
        playerTwoPaddle.didPaddleXball(ball)
        playerOnePaddle.didPaddleXball(ball)























           
            # paddle one : 
    # playerOnePaddle = shape(name='P1',shape='square',visible=True,undobuffersize=100)
    # playerOnePaddle.defaultPosition(-350,0)
    # playerOnePaddle.shapeSize(5,1)
    # playerOnePaddle.color('red')
    # # paddle two:
    # playerTwoPaddle = shape(name='P2',shape='square',visible=True,undobuffersize=100)
    # playerTwoPaddle.defaultPosition(350,0)
    # playerTwoPaddle.shapeSize(5,1)
    # playerTwoPaddle.color('red')
    # def p1moveUp():
    #     y = playerOnePaddle.ycor()
    #     y += 20
    #     playerOnePaddle.sety(y)
    # def p1moveDown():
    #     y = playerOnePaddle.ycor()
    #     y -= 20
    #     playerOnePaddle.sety(y)
    # def p2moveUp():
    #     y = playerTwoPaddle.ycor()
    #     y += 20
    #     playerTwoPaddle.sety(y)
    # def p2moveDown():
    #     y = playerTwoPaddle.ycor()
    #     y -= 20
    #     playerTwoPaddle.sety(y)
    # win.listen()
    # win.onkeypress(p1moveUp,key='w')
    # win.onkeypress(p1moveDown,key='s')
    # win.onkeypress(p2moveUp,key='Up')
    # win.onkeypress(p2moveDown,key='Down')