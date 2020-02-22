#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    for j in range(4):
        if not wall_is_on_the_right():
            move_right(1)
        for i in range(3):
            move_down(n=1)
            fill_cell()
        move_right(n=1)
        move_up(n=1)
        fill_cell()
        move_left(n=2)
        fill_cell()
        move_up(n=2)
        move_right(4)
    move_right()
    for i in range(3):
        move_down(n=1)
        fill_cell()
    move_right(n=1)
    move_up(n=1)
    fill_cell()
    move_left(n=2)
    fill_cell()
    move_up(1)




if __name__ == '__main__':
    run_tasks()
