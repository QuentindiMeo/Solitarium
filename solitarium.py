#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## Jam
## File description:
## main jamgame
##

import random as rng
from      sys import argv as av
from endgame  import *
from managers import *
from tool     import genNewNPC, get_tBub

def main():
    pg.init()
    scr = pg.display.set_mode([1200, 900])
    pg.display.set_caption("Solitarium")
    pg.display.set_icon(pg.image.load('assets/charac.png'))
    pg.mixer.music.load('assets/debbiesdaydream.wav')
    pg.mixer.music.play()
    fFnt = pg.font.Font('assets/txt.ttf', 26)
    sFnt = pg.font.Font('assets/txt.ttf', 48)
    pImg = pg.image.load('assets/player.png')
    pBor = pg.image.load('assets/border.png')
    pPos = [591, 441]
    pMov = [  0,   0]
    pSpe = 5
    nbFr = 0
    nbIt = 0
    inTheRoom = 1
    nPos = []
    nPpl = []
    tBub = [[0, -300], pg.image.load('assets/bubble.png'), []]
    lang = lng.FR
    noEsc = True

    while (noEsc):
        for event in pg.event.get():
            if (event.type == pg.QUIT or\
                (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)):
                noEsc = False
            if (event.type == pg.KEYDOWN and event.key == pg.K_e):
                endGame(scr, [fFnt, sFnt], [nbFr, nbIt], lang)
                noEsc = False
            (pMov, pSpe) = moveManager(event, pMov, pSpe, nbFr)
            (nPpl, nbIt, lang) = frndManager(event, pPos, nPpl, nbIt, lang)
        pPos = posManager(pPos, pMov)
#        if (inTheRoom < 10 and rng.randint(0, 255) == 0):
        if (inTheRoom < 32 and rng.randint(0, 1) == 0):
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
            scr.blit(txt(fFnt, tBub[2][i]), [tBub[0][0] + 9, tBub[0][1] + 7 + i * 30])
        scr.blit(pImg, pPos)
        if (noEsc): pg.display.update()

if (__name__ == "__main__"):
    if ("-h" in av or "--help" in av):
        print ("\n\tWelcome to Solitarium\n\n \033[1mUSAGE\033[0m\n\t./Solita"
        "rium\n\n \033[1mDESCRIPTION\033[0m\n\tThis experimental game is about"
        " overconnectivity. Enter an initial\n\troom, make friends  or  enemie"
        "s  and  eventually live a happy life\n\tmoving into the other rooms!"
        "\n\n \033[1mINPUTS\033[0m\n\t\033[1mup, down, left, right\033[0m\n\t"
        "\tMove around the room.\n\n\t\033[1mReturn\033[0m\n\t\tPay huge respe"
        "ct to the person you just met.\n\n\t\033[1mBackspace\033[0m\n\t\tStra"
        "ight up  insult the person you just met.\n\n\t\033[1ml\033[0m\n\t\tCh"
        "ange the game's language (FR/EN).\n\n\t\033[1me\033[0m\n\t\tPut an en"
        "d to the ongoing game (then press 'q' to quit).\n\n\t\033[1mEscape"
        "\033[0m\n\t\tExit the game.\n\n \033[1mAUTHOR\033[0m\n\tWritten by Qu"
        "entin di Meo.\n\n \033[1mREPORTING BUGS\033[0m\n\tReport any bug or "
        "functioning error to <quentin.di-meo@epitech.eu>\n")
        exit(0)
    main()
