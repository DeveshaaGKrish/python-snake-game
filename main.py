from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

def main():
    #screen setup
    screen = Screen()
    screen.tracer(0)
    screen.setup(width=600, height=600)
    screen.title("Deveshaa's Snake Game")
    screen.bgcolor("#003066")

    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()
    # event listener and updation
    screen.listen()
    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.right, key="Right")
    screen.onkey(fun=snake.left, key="Left")

    # game loop
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 20:
            scoreboard.update_score()
            food.update_food()
            snake.grow()

        # Detect collision with wall
        if snake.head.xcor() > 295 or snake.head.ycor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() < -295:
            game_is_on = False
            scoreboard.game_over()

        # Detect collison with sanke body
        for snake_body in snake.all_segments[1:]:
            if snake.head.distance(snake_body) < 10:
                game_is_on = False
                scoreboard.game_over()


    screen.exitonclick()

if __name__ == '__main__':
    main()