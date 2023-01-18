import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def create_car(self):
        # create car
        car = Turtle('square')
        car.penup()
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        car.setheading(180)
        car.setx(300)
        car.sety(random.randint(-250, 250))

        self.cars.append(car)

    def remove_out_of_sight_cars(self):
        # list comprehension that keeps just the cars that are in the viewport
        self.cars = [car for car in self.cars if -400 < car.xcor() <= 600]


    def turtle_hit(self, turtle_object):
        # loops through all the cars
        for car in self.cars:

            # print(f"Distance: {car.position()}")
            # if car is very close to the turtle
            if car.distance(turtle_object) < 20:
                return True
        else:
            return False

    def new_game(self):
        for car in self.cars:
            car.hideturtle()
        self.cars = []