#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    for i in range(5):
        while not cell_is_filled() and not wall_is_on_the_right():
            fill_cell()
            move_right()
        fill_cell()
        if not wall_is_beneath():
            move_down()
        while not cell_is_filled() and not wall_is_on_the_left():
            fill_cell()
            move_left()
        fill_cell()
        if not wall_is_beneath():
            move_down()
        while not wall_is_on_the_left():
            move_left()



if __name__ == '__main__':
    run_tasks()
