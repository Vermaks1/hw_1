#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    move_right(2)
    for i in range(3):
        move_down()
        fill_cell()
    move_right()
    move_up()
    for i in range(3):
        fill_cell()
        move_left()
    move_up()
    move_right()


if __name__ == '__main__':
    run_tasks()
