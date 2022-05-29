'''

                    Python Initialization Script

                    @andre

'''


# Native Modules

import re # Regular Expressions
import os # Operating System
import sys # System-specific
import math # Mathematics
import random as rand # Pseudo-random Number Generator
import time # Time
import importlib # Import Machinery
import inspect # Extract Information from Live Objects

# Project Modules

import keyboard # Keyboard
import requests # HTTP
from bitstring import Bits # Analysis of Binary Data
import pandas as pd # Data Analysis
import scipy as sp # Scientific Library
import numpy as np # Scientific Computing
from numpy import *
from numpy.fft import fft, ifft
import matplotlib as mp # Plotting Package
from matplotlib.pyplot import *
import dill # Extended Pickle Module

#

scriptnm = "initfile"
scriptdir = "D:\\andre\\.Env\\Python\\"
scriptpath = scriptdir + scriptnm + ".py"
sys.path.append(scriptdir)
import initfile

'''

    Functions

    
'''

def mask(x, n):
    f = "{:0" + str(n) + "b}"
    y = f.format(x)
    z = Bits(bin=y)
    return z.bin

def unmask(x, n):
    f = "{:0" + str(n) + "b}"
    y = f.format(x)
    z = Bits(bin=y)
    return z.int

class u:

    # Math

    def plot(lambd, a=-10, b=10, hold=0):
        x = np.linspace(a, b, abs(int(a - b))*100)
        m = np.linspace(int(a), int(b), abs(int(a - b))+1)
        X = lambd(x)
        plot(x, X, 'g')
        M = lambd(m)
        scatter(m, M, c='green')
        grid()

        for i in range(len(m)):
            print('{:f} \t {:f}'.format(m[i], M[i]))
        print('------------------------')

        if hold == 0:
            show()

    def quadratica(a, b, c):
        B = b**2-4*a*c
        x1 = (-b-sqrt(complex(B)))/(2*a)
        x2 = (-b+sqrt(complex(B)))/(2*a)
        return (x1, x2)

    def gauss(x, mean, sigma):
        return (1/(sigma*sqrt(2*pi)))*exp(-0.5*((x-mean)/sigma)**2)

    # Util

    def convert_bytes_to_csv(name, type, separ):
        open(name + ".bin", "wb").write(bytearray(np.fromstring(open(name +
                                                                     ".txt").read(), dtype=type, sep=separ)))

'''

 System


'''

# Workaround (Windows)

import readline
if not hasattr(readline, 'redisplay'):
    readline.redisplay = lambda: None

#

def cls():
    os.system('cls')
    
def dir():
    os.system('dir')

class initscript:

    def reload(self):
        importlib.reload(initfile)

    def edit(self, reld=1):
        os.system('micro' + ' ' + scriptpath)
        if reld:
            self.reload()

    def save(self, func, edit=0):
        code = dill.source.getsource(func)
        print(code)
        code = "\n" + code
        ans = input('Would you like to write this object to the init file?\n')
        if ans in ['yes', 'Yes', 'y', 'Y']:
            file = open(scriptpath, "a")
            file.write(code)
            file.close()
        elif ans in ['no', 'No', 'n', 'N']:
            print("Ok")
        else:
            print ("No Answer Given")

        if edit:
            self.edit()
        
init = initscript()

'''

Welcome Screen


'''

hamster = r"""
           //\                     /\\
          ////\\\\             ////\\\\
         //     \\\\_________////     \\
        //        ----     ----        \\	   
       //         ___      __         \\
        //        | ||     | ||        \\
     ///          |_||     |_||          \\\
    //              _________              \\
   ///  * *    ----|    |    |----    * *  \\\
   \\\   * *   ----|   | |   |----   * *   ///
    \\\            \ _/___\_ /            ///
      \\\                                ///
         \\\                          ///
"""

def boost(shout=0):
    text = "You can do this tiger!"
    if shout:
        return text.upper()
    else:
        return text

os.system("cls")

welcome = "Olá\n"

print(welcome)

'''

    Saved Objects


'''
#
