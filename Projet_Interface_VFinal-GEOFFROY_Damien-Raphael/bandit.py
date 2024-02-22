from cgitb import text
from tempfile import TemporaryDirectory
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image #pip install pillow
import pygame #pip install pygame
from pygame import mixer
import time 
import random
import tkinter.font as font

#
#class Bandit (bandit):
#	def draw(self):
#		imgpath = (Image.open("voleur.png"))
#		imgpath = imgpath.resize((self.width,self.height), Image.BILINEAR)
#		self.img = ImageTk.PhotoImage(imgpath)
#		#si bandit étage
#		y = (self.wagons[self.pos].height*2.5)-(self.height/1.5)
#		if (self.upper):
#			y = (self.wagons[self.pos].height*2.5)-self.wagons[self.pos].height
#		self.canvas.create_image(self.wagons[self.pos].x, y, anchor="sw", image=self.img)
