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
f = "Once upon a time there was a lovely princess. But she had an enchantment upon her of a fearful sort, which could only be broken by Love's first kiss. She was locked away in a castle guarded by a terrible fire breathing dragon. Many brave knights had attempted to free her from this dreadful prison, but none prevailed. She waited in the dragon's keep in the highest room of the tallest tower for her true love and true love's first kiss. Like that's ever going to happen. What a loony. Shrek Beware Stay out I think he's in here. All right. Lets get it! Hold on. Do you know what that thing can do to you? Yeah. He'll groan into your bones for his brains. Well actually that would be a giant. Now Ogres, huh, they are much worse. They'll make a soup from your freshly peeled skin. They'll chew your livers, squeeze the jelly from your eyes. Actually, it's quite good on toast. Back, back beast, back! I warned you! Right. This is the part, where you run away. Yeah! And stay out. Wanted. Fairytale creatures. Right, this one is full. Take it away. Give me that. Your fine days are over. -25 pieces of silver for the witch. Next. -Come on. Sit down there! And be quiet! This cage is so small. You wouldn't turn me in. I'll never be stubborn again. I can change. Please, give me another chance. Oh, shut up! Next. What do we got? This little wooden puppet. I'm not a puppet, I'm a real boy. Five shillings for the possessed toy. Take it away. No! Please, don't let them do it! Next. What do you got? Well, I've got a talking donkey! Right. Well that's good for ten schillings, if you can prove it. Oh, go ahead fella. Well? He's just a li..., just a little nervous. He's really quite a chatterbox. You boneheaded donkey! That's it. I have heard enough. Guards! No, no, he talks, he does! I can talk. I love to talk. I've talked to... Get her out of my sight! -No, no, I swear! Hey, I can fly. -He can fly! -He can fly! He can talk! -That's right, fool! Now I'm a flying, talking donkey! You might have seen house fly, maybe even a superfly. But I bet you ain't never seen a donkey fly! Seize him! Get him! This way! Hurry! You there. Ogre. -I. By the order of lord Farquaad. I am authorized to place you both under arrest. And transport you to designated resettlement facility. Oh really? You and what army? Can I say something to you? Listen, you were really, really something, back there. Incredible."
f = f.split(".")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
