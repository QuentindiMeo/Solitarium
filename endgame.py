#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Jam
## File description:
## jamgame end
##

import time
import pygame as pg
from      sys import exit
from  myEnums import lng
from     tool import txt

def getFinalScore(friends, interac, runtime):
    print (friends, interac, runtime)
    if (runtime < 5): sco = 0
    else:
        sco = 10
    msg = ["You might.", "yes"]
    return (str(sco), msg)

def x(nb, n):
    if (n == 1):
        return 182 - 42 * (len(str(nb)) - 1)
    return 486 - 14 * (len(str(nb)) - 1)

def endGame(scr, fnts, stat, lang):
    quitting = False
    gFnt = pg.font.Font('assets/txt.ttf', 77)
    (fSco, footnote) = getFinalScore(stat[0], stat[1], round(time.time() - stat[2], 2))

    pg.mixer.music.unload()
    scr.fill([22, 22, 22])
    scr.blit(txt(fnts[1], "SOLITARIUM", [24, 119, 242]), [460, 16])
    scr.blit(txt(gFnt, "You made " + str(stat[0]) + " friends."), [x(stat[0], 1), 256])
    scr.blit(txt(fnts[0], "Final score: " + fSco), [x(fSco, 2), 360])
    for i in range(len(footnote)):
        scr.blit(txt(fnts[0], footnote[i]), [600 - 7.5 * len(footnote[i]), 540 + i * 30])
    pg.display.update()
    while (quitting == False):
        for event in pg.event.get():
            if (event.type == pg.KEYDOWN and\
                (event.key == pg.K_q or event.key == pg.K_ESCAPE)):
                quitting = True
