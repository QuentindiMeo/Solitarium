#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Jam
## File description:
## main jamgame
##

import pygame as pg
import random as rng
from managers import *
from tool     import *

def main():
    pg.init()
    scr = pg.display.set_mode([1200, 900])
    pg.display.set_caption("Solitarium")
    pg.display.set_icon(pg.image.load('assets/charac.png'))
#    pg.mixer.music.load('')
#    pg.mixer.music.play(-1)
    fFnt = pg.font.Font('assets/txt.ttf', 26)
    sFnt = pg.font.Font('assets/txt.ttf', 48)
    pImg = pg.image.load('assets/player.png')
    pBor = pg.image.load('assets/border.png')
    pPos = [591, 441]
    pMov = [  0,   0]
    pSpe = 5
    nbFr = 0
    inTheRoom = 1
    nPos = []
    nPpl = []
    tBub = [[0, -300], pg.image.load('assets/bubble.png'), []]
    lang = lng.FR

    def txt(font, msg, color = [255, 255, 255]):
        return font.render(msg, True, color)

    noEsc = True
    while (noEsc):
        for event in pg.event.get():
            if (event.type == pg.QUIT or\
                (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)):
                noEsc = False
            (pMov, pSpe) = movManager(event, pMov, pSpe, nbFr)
            (nPpl, lang) = frndManager(event, nPpl, lang)
        pPos = posManager(pPos, pMov)
#        if (inTheRoom < 10 and rng.randint(0, 255) == 0):
        if (inTheRoom < 10 and rng.randint(0, 2) == 0):
            newNpc = genNewNPC(nPos)
            nPos.append(newNpc)
            nPpl.append([newNpc, pg.image.load('assets/charac.png'), sts.F_UNKN])
            inTheRoom += 1
        scr.fill([22, 22, 22])
        scr.blit(txt(sFnt, "SOLITARIUM", [24, 119, 242]), [460, 16])
        scr.blit(txt(fFnt, "Friends: " + str(nbFr)), [32, 28])
        scr.blit(pBor, [80,80])
        for ppl in nPpl:
            scr.blit(ppl[1], ppl[0])
        tBub = get_tBub(pPos, nPpl, tBub, lang)
        scr.blit(tBub[1], tBub[0])
        for i in range(len(tBub[2])):
            scr.blit(txt(fFnt, tBub[2][i]), [tBub[0][0] + 9, tBub[0][1] + 6 + i * 30])
        scr.blit(pImg, pPos)
        pg.display.update()

if (__name__ == "__main__"):
    main()
