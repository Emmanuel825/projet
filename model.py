#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 13:57:07 2026

@author: mrodri07
"""
from tkinter import *
from functools import *

global WIDTH
global HEIGHT
global main
WIDTH = 450
HEIGHT = 450
if WIDTH < HEIGHT :
    MIN = WIDTH
    WIDTH = HEIGHT
    HEIGHT = MIN

global ROI 
global TOUR
global FOU
global OR
global ARGENT
global CAVALIERS
global LANCES
global PION
ROI = 8
TOUR = 7
FOU = 6
OR = 5
ARGENT = 4
CAVALIERS = 3
LANCES = 2
PION = 1
global Sente
Sente = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1],[0,6,0,0,0,0,0,7,0],[2,3,4,5,8,5,4,3,2]]
global Gote
Gote = [[2,3,4,5,8,5,4,3,2],[0,7,0,0,0,0,0,6,0],[1,1,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
global grille
grille =[[2,3,4,5,8,5,4,3,2],[0,7,0,0,0,0,0,6,0],[1,1,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1],[0,6,0,0,0,0,0,7,0],[2,3,4,5,8,5,4,3,2]]
global cnv
global label
main = Tk()
cnv = Canvas(main, width=WIDTH, height=HEIGHT, bg='ivory')
#label = Label(main,text = "Le Sente commence",font = ("Arial",14))

