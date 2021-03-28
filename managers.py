#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Jam
## File description:
## jamgame manager functions
##

import pygame as pg
import random as rng
from  myEnums import *
from     tool import getText

def chatting(p1, p2):
    return ((p1[0] > p2[0] - 16 and p1[0] < p2[0] + 16) and\
            (p1[1] > p2[1] - 16 and p1[1] < p2[1] + 16))

def frndManager(evt, pPos, nPpl, stat, iTxt, lang):
    if (evt.type == pg.KEYUP and evt.key == pg.K_RETURN):
        for x in range(len(nPpl)):
            if (chatting(pPos, nPpl[x][0])):
                stat[1] += 1
                if (nPpl[x][2] == sts.F_UNKN and rng.randint(0, 99) < 21):
                    nPpl[x][1] = pg.image.load('assets/img/friend.png')
                    nPpl[x][2] = sts.F_FRND
                    stat[0] += 1
                    break
    if (evt.type == pg.KEYUP and evt.key == pg.K_BACKSPACE):
        for x in range(len(nPpl)):
            if (chatting(pPos, nPpl[x][0])):
                stat[1] += 1
                if (nPpl[x][2] == sts.F_UNKN and rng.randint(0, 99) < 84):
                    nPpl[x][1] = pg.image.load('assets/img/penemy.png')
                    nPpl[x][2] = sts.F_ENMY
                    stat[0] -= 1
                    break
    if (evt.type == pg.KEYUP and evt.key == pg.K_l):
        if   (lang == lng.FR): lang = lng.EN
        elif (lang == lng.EN): lang = lng.FR
        iTxt = getText(lang)
#        elif (lang == lng.EN): lang = lng.DE
#        elif (lang == lng.DE): lang = lng.IT
#        elif (lang == lng.IT): lang = lng.FR
    return (nPpl, stat[0], stat[1], iTxt, lang)

def posManager(pPos, pMov):
    nCha = False

    pPos[0] += pMov[0]
    pPos[1] += pMov[1]
    if (pPos[0] < 100):  pPos[0] = 100
    if (pPos[1] < 100):  pPos[1] = 100
    if (pPos[0] > 1091): pPos[0] = 1091
    if (pPos[1] > 791):  pPos[1] = 791
    if (pPos[0] < 110 and (pPos[1] > 425 and pPos[1] < 475)):
        pPos[0] = 1081
        nCha = True
    if (pPos[0] > 1081 and (pPos[1] > 425 and pPos[1] < 475)):
        pPos[0] = 110
        nCha = True
    if (pPos[1] < 110 and (pPos[0] > 575 and pPos[0] < 625)):
        pPos[1] = 781
        nCha = True
    if (pPos[1] > 781 and (pPos[0] > 575 and pPos[0] < 625)):
        pPos[1] = 110
        nCha = True
    return (pPos, nCha)

def moveManager(evt, pMov, pSpe, nbFr):
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
    return (pMov, 5 + nbFr * 0.1)
