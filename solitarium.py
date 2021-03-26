#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Jam
## File description:
## main jamgame
##

import pygame as pg
from movManager import *

def dispEnt(scr, eImg, ePos):
    scr.blit(eImg, ePos)

def main():
    pg.init()
    scr = pg.display.set_mode([1200, 900])
    pg.display.set_caption("Solitarium")
    pg.display.set_icon(pg.image.load('assets/player.png'))
#    pg.mixer.music.load('')
#    pg.mixer.music.play(-1)
    pImg = pg.image.load('assets/player.png')
    pBor = pg.image.load('assets/border.png')
    pPos = [370, 480]
    pMov = [  0,   0]
    pSpe = 5
    font = pg.font.Font('assets/txt.ttf', 26)
    nbFr = 0

    def txt(font, msg, color = [255, 255, 255]):
        return font.render(msg, True, color)

    running = True
    while (running):
        for event in pg.event.get():
            if (event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)):
                running = False
            (pMov, pSpe) = movManager(event, pMov, pSpe)
        pPos = posManager(pPos, pMov)
        scr.fill([22, 22, 22])
        dispEnt(scr, pImg, pPos)
        dispEnt(scr, pBor, [80,80])
        dispEnt(scr, txt(font, "Friends: " + str(nbFr)), [22, 20])
        pg.display.update()

if (__name__ == "__main__"):
    main()
