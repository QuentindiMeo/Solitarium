#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Jam
## File description:
## jamgame tool functions
##

import random as rng
from myEnums  import *
from managers import lng

def pickText(state, lang):
    fil = open('assets/text/dialog' + str(lang.value) + '.txt')
    stk = []
    nls = 0

    for s in fil:
        if (s == "\n"):
            nls += 1
            if (nls > state): break
            stk = []
            continue
        stk.append(s[: len(s) - 1])
    fil.close()
    stk = stk[rng.randint(0, len(stk) - 1)]
    return stk.split(';')

def get_tBub(p, nPpl, tBub, lang):
    for cPpl in nPpl:
        if ((p[0] > cPpl[0][0] - 16 and p[0] < cPpl[0][0] + 16) and\
            (p[1] > cPpl[0][1] - 16 and p[1] < cPpl[0][1] + 16)):
            tBub[0] = [cPpl[0][0] - 93, cPpl[0][1] - 119]
            if (tBub[2] == []): tBub[2] = pickText(cPpl[2].value, lang)
            return tBub
    return [[0, -300], tBub[1], []]

def collideAny(p, arr):
    for occP in arr:
        if ((p[0] > occP[0] - 96 and p[0] < occP[0] + 96) and
            (p[1] > occP[1] - 96 and p[1] < occP[1] + 96)):
            return True
    return False

def genNewNPC(ppl):
    pos = [rng.randint(220, 1041), rng.randint(220, 741)]

    while (collideAny(pos, ppl)):
        pos = [rng.randint(220, 1041), rng.randint(220, 741)]
    return pos

def txt(font, msg, color = [255, 255, 255]):
    return font.render(msg, True, color)
