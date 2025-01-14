import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("orange")
drawing_board.title("Star")

turtle_instance = turtle.Turtle()
for i in range(5):
    turtle_instance.forward(200)
    turtle_instance.left(144)
turtle.done()