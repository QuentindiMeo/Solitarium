#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Jam
## File description:
## main jamgame
##

from enum import Enum
import pygame as pg

class lng(Enum):
    FR = 0
    EN = 1
    DE = 2
    IT = 3

def collide(p1, p2):
    return ((p1[0] > p2[0] - 64 and p1[0] < p2[0] + 64) and\
            (p1[1] > p2[1] - 64 and p1[1] < p2[1] + 64))

def frndManager(evt, nPpl, lang):
    if (evt.type == pg.KEYUP and evt.key == pg.K_RETURN):
        e = 1
    if (evt.type == pg.KEYUP and evt.key == pg.K_BACKSPACE):
        e = 1
    if (evt.type == pg.KEYUP and evt.key == pg.K_l):
        if   (lang == lng.FR): lang = lng.EN
        elif (lang == lng.EN): lang = lng.DE
        elif (lang == lng.DE): lang = lng.IT
        elif (lang == lng.IT): lang = lng.FR
    return (nPpl, lang)

def posManager(pPos, pMov):
    pPos[0] += pMov[0]
    pPos[1] += pMov[1]
    if (pPos[0] < 100):  pPos[0] = 100
    if (pPos[1] < 100):  pPos[1] = 100
    if (pPos[0] > 1091): pPos[0] = 1091
    if (pPos[1] > 791):  pPos[1] = 791
    return pPos

def calc_pSpe(nbFr):
    return 5 + nbFr * 0.1

def movManager(evt, pMov, pSpe, nbFr):
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
    return (pMov, calc_pSpe(nbFr))
