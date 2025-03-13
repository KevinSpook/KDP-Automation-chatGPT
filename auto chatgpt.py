import time
from time import sleep
from pynput.keyboard import Key,Controller
from pynput import keyboard
import random
from random import randrange
import winsound
import subprocess
import os

keyboard = Controller()

def on_press(key):
    if key == keyboard.Key.esc:
        break
        
def restart_script():
    subprocess.run(["python", "test.py"])
            
def pressrel():
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
def name(horror):
    time.sleep(5)
    keyboard.type(horror)
    pressrel

def first(one):
    time.sleep(1)
    keyboard.type(one)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def second(two):
    time.sleep(1)
    keyboard.type(two)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def gogo(next):
    time.sleep(1)
    keyboard.type(next)
    keyboard.press(Key.enter)
    time.sleep(0.4)
    keyboard.release(Key.enter)
    time.sleep(0.4)

num = 18

def rubbish(lpa):
    for num in range(num):
        sleep(1)
        gogo(next='Write me the next chapter for this 20 chapter long book')
        time.sleep(1)
        if num >=18:
            break


def finale(last):
    time.sleep(1)
    keyboard.type(last)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def syn(op):
    time.sleep(1)
    keyboard.type(op)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    

def your_code_to_run():
    name(horror='Can you give me some creative and origional video game names thats horror themed with a good plot, captivating ending.')
    random_number = random.randint(1, 10)
    oggabooga = "From the previous choices youve gave me, may you please write a 20 chapter story for number " +str(random_number)
    second(two='Write me the first chapter for this 20 chapter book')
    finale(last='write me the final chapter for this book')
    syn(op='write me the synopsis of this book')
    first(one=oggabooga)

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press) as listener:
        while True:
            your_code_to_run()

time.sleep(5)
duration = 700  # milliseconds
freq = 300  # Hz
winsound.Beep(freq, duration)
