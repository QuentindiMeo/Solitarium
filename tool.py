#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Jam
## File description:
## jamgame tool functions
##

import random as rng
from enum import Enum
from managers import collide, lng

class sts(Enum):
    F_UNKN = 0
    F_FRND = 1
    F_ENMY = 2

def pickText(state, lang):
    fil = open('assets/txt/dialog' + str(lang.value) + '.txt')
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
        if ((p[0] > cPpl[0][0] - 9 and p[0] < cPpl[0][0] + 9) and\
            (p[1] > cPpl[0][1] - 9 and p[1] < cPpl[0][1] + 9)):
            tBub[0] = [cPpl[0][0] - 93, cPpl[0][1] - 119]
            if (tBub[2] == []): tBub[2] = pickText(cPpl[2].value, lang)
            return tBub
    return [[0, -300], tBub[1], []]

def collideAny(p, arr):
    for occP in arr:
        if (collide(p, occP)):
            return True
    return False

def genNewNPC(ppl):
    pos = [rng.randint(220, 1041), rng.randint(220, 741)]

    while (collideAny(pos, ppl)):
        pos = [rng.randint(100, 1041), rng.randint(100, 741)]
    return pos
