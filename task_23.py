#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    move_right()
    while not wall_is_on_the_right():
        move_right()
    for i in range(10):
        if not wall_is_beneath() and not wall_is_above():
            break
        while  wall_is_above():
            move_left()
        if not wall_is_beneath() and not wall_is_above():
            break
        move_up()
        fill_cell()
        if not wall_is_beneath() and not wall_is_above() and not wall_is_on_the_right() and not wall_is_on_the_left():
            break
        while not wall_is_above():
            fill_cell()
            move_up()
        fill_cell()
        if not wall_is_beneath() and not wall_is_above():
            break
        while not wall_is_beneath():
            move_down()
        move_left()
        if not wall_is_beneath() and not wall_is_above():
            break



if __name__ == '__main__':
    run_tasks()
