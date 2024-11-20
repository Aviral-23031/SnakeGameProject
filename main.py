import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard

screen  = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_segments()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.score_change()
        snake.extends()
        food.refresh()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 260 or snake.head.ycor() < -280 :
        scoreboard.reset()
        snake.reset()

    #Detect Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()