#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:04:59 2020

@author: applelover
"""

import cv2 as cv #Using the open CV library to carry out all the image and video operations cv2 which is the name of the opencv library,cv is the name followed u wanted to give to this library used to refer the functions and objects of this library.For simplicity we use cv.In case we dont use it cv2.function_name() ,cv2 is the prefix instead of cv

import numpy as np#package of python as np for simplicity.Important to conduct all the array packages on the image
#press any key to close the image on display n the stop the script
img = cv.imread('hazard10.jpg')
img1 = cv.imread('hazard10.jpg',0)  ## The flag, 0, will load the image in grayscale mode
#if u pass the integer 0 as the 2nd argument the image is loaded in the grayscale mode if u pass the integer -1 as the flag the image is loaded as it is including the alpha channel if u pass the integer 1 as the flag the image is loaded as the color image and any transparency of the image will be neglected note that 1 is the default flag if 2nd argument is not provided.
#Now assign the loaded grayscale image to a new variable img1 
cv.imshow('image',img)#to display the img1 image to dislay in window named img1
cv.imshow('image1',img1)
cv.imwrite('grayhazard.jpg',img1)#save grayscale image.first argument is the file name and the 2nd argument is the image u wanted to save in the file u specified.
#here u will save the grayscale image stored in img1 in the file name grayhazard.jpg.This will save the image in the jpg format in the working directory

cv.waitKey(0)
cv.destroyAllWindows()
 
#You will now read the image with 'hazard10.jpg' in the working folder.
#To read the image you will use the imread function of the open cv-library.
#To Call the function of the open cv-library you will have to prefix it with the library name which will be renamed as CV.
#The input for the imread function should be the file name as a string in case the file is in the same directory as the code else you will have to provide the entire path for the file as a string.
#Here the name of the file is 'hazard10.jpg' which you have to include in quotes to pass it as string you will assign output of read function to a variable named as  img to access image for further operation.
#using the function show  cv.imshow to display an image on the window.
#The window automatically fit to the image size.
#The first argument in the function is the window name in which the image will be displayed. This is a string.
#The second argument will be the image. You can create as many windows as you wish but with different window name.
#You will end the program by closing the image Windows by pressing any key on the keyboard. CV. Waitkey is a keyboard binding function. It's Argument is time in milisecond.
#The function aWait for specific milliseconds for any keyboard event. If you press any key in that  specified time the program continues. For zero the program will wait indefinitely for keystroke. It can also be set to detect specific keystrokes.
#if key q is pressed CV.destroyAll Windows destroyed all the windows you had created. If you want to destroy any specific window use the function CV.destroywindow where you pass the exact window name as the argument

