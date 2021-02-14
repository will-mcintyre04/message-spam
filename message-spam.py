#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 18:06:24 2021

@author: williammcintyre
"""

# Spam Messages Code
# Will McIntyre
# February 8th, 2021

import pyautogui, time
time.sleep(5)
f = ""
f = f.split("-")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
