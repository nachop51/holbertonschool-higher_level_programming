#!/usr/bin/python3
""" Base module for models """
import json
from os.path import exists
import csv


class Base:
    """ Class attribute to count the number of instances """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor method for the instance """
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id    

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            string = "[]"
        else:
            string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])
        with open(filename, "w") as f:
            f.write(string)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creates an instance with all attributes already set """
        if cls.__name__ == "Square":
            dummy = cls(1)
        elif cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Loads and returns list of instances from a file """
        filename = cls.__name__ + ".json"
        if exists(filename):
            with open(filename, "r") as f:
                return [cls.create(**obj) for obj
                        in cls.from_json_string(f.read())]
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Saves a list of instances to a csv file """
        if list_objs:
            filename = cls.__name__ + ".csv"
            with open(filename, "w") as file:
                if "Rectangle" in filename:
                    fields = ["id", "width", "height", "x", "y"]
                elif "Square" in filename:
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Loads and returns a list of instances from a csv file """
        filename = cls.__name__ + ".csv"
        if exists(filename):
            if "Rectangle" in filename:
                fields = ["id", "width", "height", "x", "y"]
            elif "Square" in filename:
                fields = ["id", "size", "x", "y"]
            list_objs = []
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if len(fields) == 4:
                        new_instance = cls(1)
                    elif len(fields) == 5:
                        new_instance = cls(1, 1)
                    for i, field in enumerate(row):
                        setattr(new_instance, fields[i], int(row[field]))
                    list_objs.append(new_instance)
        return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draws the figure instance """
        from turtle import Turtle, Screen
        from time import sleep

        screen = Screen()
        screen.colormode(255)
        t = Turtle(shape="turtle")
        t.color(Base.random_color())
        t.width(10)
        t.speed(1)
        list_rectangles.extend(list_squares)
        for obj in (list_rectangles):
            t.shape("turtle")
            t.penup()
            t.color(Base.random_color())
            sleep(1)
            t.goto(obj.x, obj.y)
            t.pendown()
            t.forward(obj.width)
            t.shape("circle")
            t.right(90)
            t.forward(obj.height)
            t.shape("triangle")
            t.right(90)
            t.forward(obj.width)
            t.shape("arrow")
            t.right(90)
            t.forward(obj.height)
            t.right(90)

        screen.exitonclick()

    @staticmethod
    def random_color():
        """ Returns a random """
        from random import randint

        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        color = (r, g, b)
        return color
