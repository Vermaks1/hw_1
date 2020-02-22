#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    fill_cell()
    for i in range(12):
        move_down()
        fill_cell()
        for j in range(i+1):
            move_right(n=j+1)
            fill_cell()
            move_left(n=j+1)
    move_down()



if __name__ == '__main__':
    run_tasks()
