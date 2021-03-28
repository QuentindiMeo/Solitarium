#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Jam
## File description:
## jamgame enums
##

from enum import Enum

class lng(Enum):
    FR = 0
    EN = 1
    DE = 2
    IT = 3

class sts(Enum):
    F_UNKN = 0
    F_FRND = 1
    F_ENMY = 2

class gui(Enum):
    I_FRND = 0
    I_LIFE = 1
    I_NBFR = 2
    I_FSCO = 3
    I_INPT = 4

class fin(Enum):
    S_TMFRIENDS = 0
    S_TMINTERAC = 1
    S_NGFRIENDS = 2
    S_NOFRIENDS = 3
    S_NOINTERAC = 4
    S_ALLGOODMN = 5
    S_ALLGOODMX = 7
    S_TLFRIENDS = 8
    S_TLINTERAC = 9
