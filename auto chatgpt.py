import time
from time import sleep
from pynput.keyboard import Key,Controller
from random import randrange

keyboard = Controller()

def name(horror):
    time.sleep(5)
    keyboard.type(horror)
    keyboard.press(Key.enter)
    time.sleep(0.2)
    keyboard.release(Key.enter)

name(horror='Can you give me some creative and origional video game names thats horror themed')

def first(one):
    time.sleep(15)
    keyboard.type(one)
    keyboard.press(Key.enter)
    time.sleep(0.2)
    keyboard.release(Key.enter)

first(one='Can you give me a 20 chapter book for one of the choises you gave me previously, randomly pick one please.')

def second(two):
    time.sleep(15)
    keyboard.type(two)
    keyboard.press(Key.enter)
    time.sleep(0.2)
    keyboard.release(Key.enter)

second(two='Write me the first chapter for this 20 chapter book')

def gogo(next):
    time.sleep(1)
    keyboard.type(next)
    keyboard.press(Key.enter)
    time.sleep(0.2)
    keyboard.release(Key.enter)

num = 18
for num in range(num):
   sleep(15)
   gogo(next='Write me the next chapter for this 20 chapter long book')
   time.sleep(1)
   if num >=18:
       break


def finale(last):
    time.sleep(15)
    keyboard.type(last)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
finale(last='write me the final chapter for this book')


def syn(op):
    time.sleep(15)
    keyboard.type(op)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
syn(op='write me the synopsis of this book')

time.sleep(11)
import winsound
duration = 100  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)
