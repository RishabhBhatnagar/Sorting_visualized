#imports.
from tkinter import Tk
from tkinter import Canvas
from time import sleep as delay
import os          #os for playing sound.

from bubble_sort import bubble_sort
from merge_sort import merge_sort
from comb_sort import comb_sort
from shell_sort import shell_sort

from dimensions import *
import dimensions

class stick:
    def __init__(self, number, stick_width = 2):
        self.number = number
        self.color = number
        self.sound = number
        self.stick_width = stick_width
    def get_height(self, max):
        self.height = self.number/max
        self.freq = min_freq + (max_freq-min_freq)*self.height
        return self.height
    def update(self, x1, x2, y):
        self.x1 = x1
        self.x2 = x2
        self.y = y

class window:
    def __init__(self, root, x, y):
        self.root = root
        self.height = y
        self.width = x
        self.canvas = Canvas(root, width = self.width, height = self.height)
        self.canvas.pack()

def draw_stick(canvas, a_stick, max, x1 = 'nan', x2 = 'nan', y = 'nan', color = 'green'):
    global last_x
    if x1 == 'nan' : 
        x1 = last_x
        last_x += stick_width
    if x2 == 'nan' : 
        x2 = last_x
    if y == 'nan' : 
        y = a_stick.get_height(max)*dims['y']
    a_stick.update(x1, x2, y)
    return canvas.create_rectangle(x1, 0, x2, y, fill = color)

def update(window, stick, stick_rect, color, num = 'nan'):
    if num == 'nan' : 
        num = stick.number
        y = stick.y
    else:
        stick.number = num
        y = stick.get_height(max)*dims['y']
    x1, x2 = stick.x1, stick.x2
    window.canvas.delete(stick_rect)
    return (stick, window.canvas.create_rectangle(x1, 0, x2, y, fill = color))

#initial setup.
root = Tk()

N = int(dims['x']/stick_width)
root.geometry(str(dims['x'])+'x'+str(dims['y']))
window = window(root, dims['x'], dims['y'])


#array setup.
max = N
from random import shuffle
a = list(range(1, N+1))
shuffle(a)

sticks = []
drawn_sticks = []
for num in a:
    sticks.append(stick(num))
for stk in sticks:
    current_stick_rect = draw_stick(window.canvas, stk, max, color = 'red')
    drawn_sticks.append((stk, current_stick_rect))

def replace(i, color, num = 'nan', time = 0.001):
    import random
    if i<len(drawn_sticks):
        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, drawn_sticks[i][0].freq))
        (stk, stk_rect) = drawn_sticks[i]
        drawn_sticks[i] = update(window, stk, stk_rect, color = color, num = num)
        delay(time)
        root.update_idletasks()
        root.update()

def anim(i, num, time = 0.001):
    replace(i, 'black', num, time)
    replace(i, 'red', num, time)
    
dimensions.anim = anim

a = drawn_sticks

shell_sort(anim, a, 0.0001)
comb_sort(anim, a, 0.000001)
merge_sort(anim, a, 0.000001)
bubble_sort(anim, a, 0)

window.root.mainloop()
