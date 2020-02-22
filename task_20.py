#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    for i in range(11):
        for i in range(27):
            move_right()
            fill_cell()
        move_down()
        for i in range(27):
            fill_cell()
            move_left()
    move_right()
    move_down()





if __name__ == '__main__':
    run_tasks()
