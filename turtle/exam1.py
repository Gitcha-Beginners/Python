import turtle

turtle.shape("turtle")
original_xcor = turtle.xcor()
original_ycor = turtle.ycor()
speed = 2
while True:
    turtle.forward(speed)
    turtle.left(10)
    speed += 0.1
    if turtle.distance(original_xcor, original_ycor) > 90:
        break

turtle.exitonclick()
