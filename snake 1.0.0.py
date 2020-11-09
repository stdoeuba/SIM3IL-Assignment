# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 17:49:02 2020
Home Assignment - SIM3IL 
Programmming the game snake
@author: domin
"""
    #adding bibs
from turtle import *
from random import randrange
from freegames import square, vector


    #adding vectors
food    = vector(0, 0)
snake   = [vector(10, 0)]
aim     = vector(0, -10)

