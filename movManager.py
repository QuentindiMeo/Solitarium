#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Jam
## File description:
## main jamgame
##

import pygame as pg

def posManager(pPos, pMov):
    pPos[0] += pMov[0]
    pPos[1] += pMov[1]
    if (pPos[0] < 0):    pPos[0] = 0
    if (pPos[1] < 0):    pPos[1] = 0
    if (pPos[0] > 1192): pPos[0] = 1192
    if (pPos[1] > 892):  pPos[1] = 892
    return pPos

def movManager(evt, pMov, pSpe):
    if (evt.type == pg.KEYDOWN):
        if (evt.key == pg.K_RIGHT):
            pMov[0] = pSpe
        if (evt.key == pg.K_LEFT):
            pMov[0] = -pSpe
        if (evt.key == pg.K_DOWN):
            pMov[1] = pSpe
        if (evt.key == pg.K_UP):
            pMov[1] = -pSpe
    if (evt.type == pg.KEYUP and (evt.key == pg.K_RIGHT or evt.key == pg.K_LEFT)):
        pMov[0] = 0
    if (evt.type == pg.KEYUP and (evt.key == pg.K_DOWN  or evt.key == pg.K_UP)):
        pMov[1] = 0
    if (evt.type == pg.KEYDOWN and evt.key == pg.K_c):
        pSpe = (25 if (pSpe == 5) else 5)
    return (pMov, pSpe)
