import turtle

bcolor = 'cyan'
bshadow = ''
gcolor = '#9acedc'
gshadow = ''

s = turtle.getscreen()
i = turtle.Turtle()


def body():
    i.pensize(20)
    i.speed(15)
    i.fillcolor(bcolor)
    i.begin_fill()
    i.right(90)
    i.forward(50)
    i.right(180)
    i.circle(40, -180)
    i.right(180)
    i.forward(200)
    i.right(180)
    i.circle(100, -180)
    i.backward(20)
    i.left(15)
    i.circle(500, -20)
    i.backward(20)
    i.circle(40, -180)
    i.left(7)
    i.backward(50)
    i.up()
    i.left(90)
    i.forward(10)
    i.right(90)
    i.down()
    i.right(240)
    i.circle(50, -70)
    i.end_fill()


def glass():
    i.up()
    i.right(230)
    i.forward(100)
    i.left(90)
    i.forward(20)
    i.right(90)
    i.down()
    i.fillcolor(gcolor)
    i.begin_fill()
    i.right(150)
    i.circle(90, -55)
    i.right(180)
    i.forward(1)
    i.right(180)
    i.circle(10, -65)
    i.right(180)
    i.forward(110)
    i.right(180)
    i.circle(50, -190)
    i.right(170)
    i.forward(80)
    i.right(180)
    i.circle(45, -30)
    i.end_fill()


def backpack():
    i.up()
    i.right(60)
    i.forward(100)
    i.right(90)
    i.forward(75)
    i.fillcolor(bcolor)
    i.begin_fill()
    i.down()
    i.forward(30)
    i.right(255)
    i.circle(300, -30)
    i.right(260)
    i.forward(30)
    i.end_fill()


body()
glass()
backpack()

i.screen.exitonclick()
