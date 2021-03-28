#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Jam
## File description:
## jamgame end
##

import random as rng
import   time
import pygame as pg
from     math import exp, log
from      sys import exit
from  myEnums import lng, fin
from     tool import txt

def getFinale(friends, interac, runtime, iMsg):
    sco = 0
    rtm = runtime / 3
    rtl = runtime / 9

    if (runtime > 3.14 and friends > 0):
        sco = log(friends) + 22 if (friends < 8)\
            else 27 * (1 / exp(friends)) ** 0.025
        sco = exp(int(sco)) ** 0.2 * (1 + (interac / friends) / 10)
    if   (friends > 7)  : msg = iMsg[fin.S_TMFRIENDS.value]
    elif (friends < 0)  : msg = iMsg[fin.S_NGFRIENDS.value]
    elif (interac > rtm): msg = iMsg[fin.S_TMINTERAC.value]
    elif (not interac)  : msg = iMsg[fin.S_NOINTERAC.value]
    elif (not friends)  : msg = iMsg[fin.S_NOFRIENDS.value]
    elif (interac < rtl): msg = iMsg[fin.S_TLINTERAC.value]
    elif (friends < 8 and\
          interac < rtm): msg = iMsg[rng.randint(fin.S_ALLGOODMN.value, fin.S_ALLGOODMX.value)]
    elif (friends < 4)  : msg = iMsg[fin.S_TLFRIENDS.value]
    else                : msg = []
#    print (  "f=", friends, "\ti=", interac, "\tt=", runtime,\
#           "\ts=", str(int(sco)), sep="")
    return (str(int(sco)), msg)

def x(nb, n = 2):
    return 600 - (20.5 if n == 1 else 7.5) * float(nb)

def endGame(scr, fnts, stat, iTxt):
    quitting = False
    gFnt = pg.font.Font('assets/txt.ttf', 70)
    (fSco, footnote) = getFinale(stat[0], stat[1], round(time.time() - stat[2], 2), iTxt[5:])

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
