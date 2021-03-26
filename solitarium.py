#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Jam
## File description:
## main jamgame
##

import pygame as pg
import random
from movManager import *

def genNewNPC(fkf):
    pos = [random.randint(200, 991), random.randint(200, 691)]

    def collideAny(p, arr):
        for occP in arr:
            if ((p[0] > occP[0] - 64 and p[0] < occP[0] + 64) and\
                (p[1] > occP[1] - 64 and p[1] < occP[1] + 64)):
#                print (pos, "collides", occP)
                return True
        return False

    while (collideAny(pos, fkf)):
        pos = [random.randint(100, 1091), random.randint(100, 791)]
    return pos

def dispEnt(scr, eImg, ePos):
    scr.blit(eImg, ePos)

def main():
    pg.init()
    scr = pg.display.set_mode([1200, 900])
    pg.display.set_caption("Solitarium")
    pg.display.set_icon(pg.image.load('assets/player.png'))
#    pg.mixer.music.load('')
#    pg.mixer.music.play(-1)
    fnt  = pg.font.Font('assets/txt.ttf', 26)
    sFnt = pg.font.Font('assets/txt.ttf', 48)
    pImg = pg.image.load('assets/player.png')
    pBor = pg.image.load('assets/border.png')
    pPos = [591, 441]
    pMov = [  0,   0]
    pSpe = 5
    nbFr = 0
    inTheRoom = 1
    fkf = []

    def txt(font, msg, color = [255, 255, 255]):
        return font.render(msg, True, color)

    running = True
    while (running):
        for event in pg.event.get():
            if (event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)):
                running = False
            (pMov, pSpe) = movManager(event, pMov, pSpe)
        pPos = posManager(pPos, pMov)
        if (inTheRoom < 10 and random.randint(0, 256) == 0):
            fkf.append(genNewNPC(fkf))
            inTheRoom += 1
        scr.fill([22, 22, 22])
        dispEnt(scr, txt(sFnt, "SOLITARIUM", [24, 119, 242]), [460, 16])
        dispEnt(scr, txt(fnt, "Friends: " + str(nbFr)), [32, 28])
        dispEnt(scr, pBor, [80,80])
        dispEnt(scr, pImg, pPos)
        for npc in fkf:
            dispEnt(scr, pImg, npc)
        pg.display.update()

if (__name__ == "__main__"):
    main()
