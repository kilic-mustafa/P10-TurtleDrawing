import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Polygon")

turtle_instance = turtle.Turtle()
num_sides = 6
angle = 360.0 / num_sides
side_length = 100

for i in range(num_sides):
    turtle_instance.forward(side_length)
    turtle_instance.left(angle)

turtle.done()