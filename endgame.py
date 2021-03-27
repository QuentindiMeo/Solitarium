#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Jam
## File description:
## jamgame end
##

import pygame as pg
from      sys import exit
from  myEnums import lng
from     tool import txt

def endGame(scr, fnts, stat, lang):
    quitting = False

    pg.mixer.music.unload()
    scr.fill([22, 22, 22])
    scr.blit(txt(fnts[1], "SOLITARIUM", [24, 119, 242]), [460, 16])
    pg.display.update()
    while (quitting == False):
        for event in pg.event.get():
            if (event.type == pg.KEYDOWN and event.key == pg.K_q):
                quitting = True
