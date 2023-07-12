import os
import time
import winsound
from threading import Thread, Event
from time import sleep

ev = Event()


def func():
    ev.wait()
    sign = ['mARIO',
            'MaRIO.',
            'MArIO..',
            'MARiO...',
            'MARIo',
            'mARIO.',
            'MaRIO..',
            'MArIO...',
            'MARiO',
            'MARIo.',
            'mARIO..',
            'MaRIO...',
            'MArIO',
            'MARiO.',
            'MARIo..',
            'mARIO...',
            'MaRIO',
            'MArIO.',
            'MARiO..',
            'MARIo...'
            ]
    i = 0

    while True:
        print(f'HAVE FUN WITH {sign[i]}.')
        time.sleep(0.5)
        os.system('cls||clear')
        i = (i + 1) % len(sign)


th1 = Thread(target=func)

th1.start()
ev.set()

winsound.Beep(660, 214)
winsound.Beep(660, 214)
time.sleep(0.214)
winsound.Beep(660, 214)
time.sleep(0.214)
winsound.Beep(523, 214)
winsound.Beep(660, 428)
winsound.Beep(784, 428)
time.sleep(0.428)
winsound.Beep(392, 428)
time.sleep(0.428)

while True:
    winsound.Beep(523, 428)
    time.sleep(0.214)
    winsound.Beep(392, 428)
    time.sleep(0.214)
    winsound.Beep(330, 428)
    time.sleep(0.214)
    winsound.Beep(440, 428)
    winsound.Beep(494, 428)
    winsound.Beep(466, 214)
    winsound.Beep(440, 428)

    winsound.Beep(392, 321)
    winsound.Beep(660, 321)
    winsound.Beep(784, 321)
    winsound.Beep(880, 428)
    winsound.Beep(698, 214)
    winsound.Beep(784, 214)
    time.sleep(0.214)
    winsound.Beep(659, 428)
    winsound.Beep(523, 214)
    winsound.Beep(587, 214)
    winsound.Beep(494, 428)
    time.sleep(0.214)
