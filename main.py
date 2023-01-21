# pip3 install keyboard
# pip3 install pynput
# pip3 install table-logger
# pip3 install "numpy<1.24"

import keyboard
import time

import math
import datetime
import random
from table_logger import TableLogger

tbl = TableLogger()

tbl(1, 'Row1', datetime.datetime.now(), math.pi)
tbl(2, 'Row2', datetime.datetime.now(), 1/3)
tbl(3, 'Row3', datetime.datetime.now(), random.random())

pos_x = 0
pos_y = 0

# def on_press(key):
#   if (key == 'left')

while True:
    if keyboard.is_pressed('left'):
        if pos_x > 0:
            pos_x -= 1
    if keyboard.is_pressed('right'):
        if pos_x < 2:
            pos_x += 1

    if keyboard.is_pressed('down'):

        time.sleep(0.4)
    if keyboard.is_pressed('up'):

        time.sleep(0.4)
    if keyboard.is_pressed('escape'):

        break
    time.sleep(0.4)
