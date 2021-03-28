#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Jam
## File description:
## jamgame end
##

import random as rng
import time
import pygame as pg
from     math import exp, log
from      sys import exit
from  myEnums import lng
from     tool import txt

def getFinalScore(friends, interac, runtime, iTxt):
    sco = 0
    if (runtime > 5 and friends):
        sco = log(friends) + 22 if (friends < 8)\
        else 27 * (1 / exp(friends)) ** 0.025
        sco = exp(int(sco)) ** 0.2 * (1 + (interac / friends) / 10)
    if (1):
        msg = iTxt[rng.randint(5, len(iTxt) - 1)]
    print (  "f=", friends, "\ti=", interac, "\tt=", runtime,\
           "\ts=", str(int(sco)), sep="")
    return (str(int(sco)), msg)

def x(nb, n = 2):
    return 600 - (20.5 if n == 1 else 7.5) * float(nb)

def endGame(scr, fnts, stat, iTxt):
    quitting = False
    gFnt = pg.font.Font('assets/txt.ttf', 70)
    (fSco, footnote) = getFinalScore(stat[0], stat[1], round(time.time() - stat[2], 2), iTxt)

    pg.mixer.music.stop()
    scr.fill([22, 22, 22])
    scr.blit(txt(fnts[1], "SOLITARIUM", [24, 119, 242]), [460, 16])
    scr.blit(txt(gFnt, iTxt[2][0] + str(stat[0]) + iTxt[2][1]), [x(len(str(stat[0])) + len(iTxt[2][0]) + len(iTxt[2][1]), 1), 256])
    scr.blit(txt(fnts[0], iTxt[3] + fSco), [x(len(str(fSco)) + len(iTxt[3]), 2), 360])
    for i in range(len(footnote)):
        scr.blit(txt(fnts[0], footnote[i]), [x(len(footnote[i])), 540 + i * 30])
    scr.blit(txt(fnts[0], iTxt[4]), [x(len(iTxt[4])), 777])
    while (quitting == False):
        pg.display.update()
        for event in pg.event.get():
            if (event.type == pg.KEYUP and\
                (event.key == pg.K_q or event.key == pg.K_ESCAPE)):
                quitting = True
            if (event.type == pg.KEYUP and event.key == pg.K_r):
                return False
    return True
