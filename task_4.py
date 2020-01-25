#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if wall_is_beneath():
        move_down()
    if wall_is_above():
        move_up()
    if wall_is_on_the_left():
        move_left()
    if wall_is_on_the_right():
        move_right
        
    pass


if __name__ == '__main__':
    run_tasks()
