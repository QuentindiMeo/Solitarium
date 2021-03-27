#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Jam
## File description:
## jamgame tool functions
##

import random as rng
from enum import Enum

class sts(Enum):
    F_UNKN = 0
    F_FRND = 1
    F_ENMY = 2

def pickText(state):
    fil = open('assets/dialog.txt')
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

def get_tBub(p, nPpl, tBub):
    for cPpl in nPpl:
        if ((p[0] > cPpl[0][0] - 9 and p[0] < cPpl[0][0] + 9) and\
            (p[1] > cPpl[0][1] - 9 and p[1] < cPpl[0][1] + 9)):
            tBub[0] = [cPpl[0][0] - 93, cPpl[0][1] - 119]
            if (tBub[2] == []): tBub[2] = pickText(sts.F_ENMY.value)
#            if (tBub[2] == []): tBub[2] = pickText(cPpl[2].value)
            return tBub
    return [[0, -300], tBub[1], []]

def genNewNPC(ppl):
    pos = [rng.randint(200, 991), rng.randint(200, 691)]

    def collideAny(p, arr):
        for occP in arr:
            if ((p[0] > occP[0] - 64 and p[0] < occP[0] + 64) and\
                (p[1] > occP[1] - 64 and p[1] < occP[1] + 64)):
#                print (pos, "collides", occP)
                return True
        return False

    while (collideAny(pos, ppl)):
        pos = [rng.randint(100, 1091), rng.randint(100, 791)]
    return pos
