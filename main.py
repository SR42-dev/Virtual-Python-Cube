"""
setup.bat source code :

pip install opencv-python
pip install Pillow
pip install pyzbar
pip install qrcode

"""

# Import from different libraries
from pyzbar.pyzbar import decode
from tkinter import *
from random import *
from PIL import *
import random
import qrcode
import time
import cv2
import os

# cr is the abbreviation for solved cube

# Color definition
red='red'
orange='orange'
white='white'
green='green'
yellow='yellow'
blue='blue'

# Definition of lists
CC=[]  # cube in progress
CCstr = '' # CC in string form
cm1=[] # cube after movement 1
qrdatastr = '' # QR data string 

# Graphics part

a = 800
b = 1100
i = int(a/12)
j = int(a/12)
x = int(a/22.5)
y = int(b/30)

window1 = Tk()
window1.title("Virtual Python Cube")
window1.geometry(str(b - 150) + "x" + str(a))
canvas1 = Canvas(window1, width=b , height=a)
canvas1.pack(side=LEFT)

# Function to convert between CC and CCstr formats

def CCconvert(a) :

    global CC
    global CCstr

    # a = 0 => CC to CCstr conversion
    # a = 1 => CCstr to CC conversion

    if a == 0 :

        for i in CC :

            for j in i :

                for k in j :

                    if k == red :

                        CCstr += 'r'

                    elif k == orange :

                        CCstr += 'o'

                    elif k == white :

                        CCstr += 'w'

                    elif k == green :

                        CCstr += 'g'

                    elif k == yellow :

                        CCstr += 'y'

                    elif k == blue :

                        CCstr += 'b'

    elif a == 1 :

        i = 0
        j = 0
        while j <= 5 :

            k = 0
            while k <= 2:

                l = 0
                while l <= 2 :

                    if CCstr[i] == 'r' :

                        CC[j][k][l] = red

                    elif CCstr[i] == 'o' :

                        CC[j][k][l] = orange

                    elif CCstr[i] == 'w' :

                        CC[j][k][l] = white

                    elif CCstr[i] == 'g' :

                        CC[j][k][l] = green

                    elif CCstr[i] == 'y' :

                        CC[j][k][l] = yellow

                    elif CCstr[i] == 'b' :

                        CC[j][k][l] = blue
                    
                    i += 1
                    l += 1

                    if i > 53 :

                        break
                    
                k += 1
                    
            j += 1
            


# cube function for solution

def cube_solve() :
    global cr,red,orange,white,green,yellow,blue,CC
    cr=[[[red,red,red],[red,red,red],[red,red,red]],
        [[orange,orange,orange],[orange,orange,orange],[orange,orange,orange]],
        [[white,white,white],[white,white,white],[white,white,white]],
        [[green,green,green],[green,green,green],[green,green,green]],
        [[yellow,yellow,yellow],[yellow,yellow,yellow],[yellow,yellow,yellow]],
        [[blue,blue,blue],[blue,blue,blue],[blue,blue,blue]]]
    CC=cr

cube_solve()

def cube_init():
    
    c = 2*x
    d = 2*y
    
# Creation of faces with the abbreviations F for face and C for square, face 1

    F1C1=canvas1.create_polygon(c+4.32*x ,  d+2*y ,     c+2.66*x ,  d+2.66*y , c+1*x ,    d+2*y ,    c+2.66*x ,    d+1.34*y  ,outline='black' ,  fill=CC [0] [0] [0])
    F1C2=canvas1.create_polygon(c+5.98*x ,  d+2.66*y ,  c+4.32*x ,  d+3.33*y , c+2.66*x , d+2.66*y , c+4.32*x ,    d+2*y     ,outline='black' ,  fill=CC [0] [0] [1])
    F1C3=canvas1.create_polygon(c+7.66*x ,  d+3.34*y ,  c+6*x ,     d+4*y ,    c+4.32*x , d+3.33*y , c+5.98*x ,    d+2.66*y  ,outline='black' ,  fill=CC [0] [0] [2])
    F1C4=canvas1.create_polygon(c+5.98*x ,  d+1.34*y ,  c+4.32*x ,  d+2*y ,    c+2.66*x , d+1.34*y , c+4.32*x ,    d+0.66*y  ,outline='black' ,  fill=CC [0] [1] [0])
    F1C5=canvas1.create_polygon(c+7.66*x ,  d+2*y ,     c+5.98*x ,  d+2.66*y , c+4.32*x , d+2*y ,    c+5.98*x ,    d+1.34*y  ,outline='black' ,  fill=CC [0] [1] [1])
    F1C6=canvas1.create_polygon(c+9.32*x ,  d+2.67*y ,  c+7.66*x ,  d+3.34*y , c+5.98*x , d+2.66*y , c+7.64*x ,    d+2*y     ,outline='black' ,  fill=CC [0] [1] [2])
    F1C7=canvas1.create_polygon(c+7.66*x ,  d+0.66*y ,  c+5.98*x ,  d+1.34*y , c+4.32*x , d+0.67*y , c+6*x ,       d+0*y     ,outline='black' ,  fill=CC [0] [2] [0])
    F1C8=canvas1.create_polygon(c+9.32*x ,  d+1.33*y ,  c+7.64*x ,  d+2*y ,    c+5.98*x , d+1.34*y , c+7.66*x ,    d+0.66*y  ,outline='black' ,  fill=CC [0] [2] [1])
    F1C9=canvas1.create_polygon(c+11*x ,    d+2*y ,     c+9.32*x ,  d+2.67*y , c+7.64*x , d+2*y ,    c+9.32*x ,    d+1.33*y  ,outline='black' ,  fill=CC [0] [2] [2])

# Creation face 2 :

    F2C1=canvas1.create_polygon(c+22*x ,    d+2*y ,     c+20.32*x , d+2.67*y , c+18.64*x , d+2*y ,    c+20.32*x ,  d+1.33*y  ,outline='black' ,  fill=CC [1] [0] [0])
    F2C2=canvas1.create_polygon(c+20.32*x , d+2.67*y ,  c+18.66*x , d+3.34*y , c+16.98*x , d+2.66*y , c+18.64*x ,  d+2*y     ,outline='black' ,  fill=CC [1] [1] [0])
    F2C3=canvas1.create_polygon(c+18.66*x , d+3.34*y ,  c+17*x ,    d+4*y ,    c+15.32*x , d+3.33*y , c+16.98*x ,  d+2.66*y  ,outline='black' ,  fill=CC [1] [2] [0])
    F2C4=canvas1.create_polygon(c+20.32*x , d+1.33*y ,  c+18.64*x , d+2*y ,    c+16.98*x , d+1.34*y , c+18.66*x ,  d+0.66*y  ,outline='black' ,  fill=CC [1] [0] [1])
    F2C5=canvas1.create_polygon(c+18.66*x , d+2*y ,     c+16.98*x , d+2.66*y , c+15.32*x , d+2*y ,    c+16.98*x ,  d+1.34*y  ,outline='black' ,  fill=CC [1] [1] [1])
    F2C6=canvas1.create_polygon(c+16.98*x , d+2.66*y ,  c+15.32*x , d+3.33*y , c+13.66*x , d+2.66*y , c+15.32*x ,  d+2*y     ,outline='black' ,  fill=CC [1] [2] [1])
    F2C7=canvas1.create_polygon(c+18.66*x , d+0.66*y ,  c+16.98*x , d+1.34*y , c+15.32*x , d+0.67*y , c+17*x ,     d+0*y     ,outline='black' ,  fill=CC [1] [0] [2])
    F2C8=canvas1.create_polygon(c+16.98*x , d+1.34*y ,  c+15.32*x , d+2*y ,    c+13.66*x , d+1.34*y , c+15.32*x ,  d+0.67*y  ,outline='black' ,  fill=CC [1] [1] [2])
    F2C9=canvas1.create_polygon(c+15.32*x , d+2*y ,     c+13.66*x , d+2.66*y , c+12*x ,    d+2*y ,    c+13.66*x ,  d+1.34*y  ,outline='black' ,  fill=CC [1] [2] [2])


# Creation face 3 :

    F3C1=canvas1.create_polygon(c+2.66*x ,  d+5.03*y ,  c+1*x ,     d+4.36*y ,  c+1*x ,    d+2*y ,    c+2.66*x ,   d+2.66*y  ,outline='black' ,  fill=CC [2] [0] [0])
    F3C2=canvas1.create_polygon(c+2.66*x ,  d+7.36*y ,  c+1*x ,     d+6.66*y ,  c+1*x ,    d+4.36*y , c+2.66*x ,   d+5.03*y  ,outline='black' ,  fill=CC [2] [0] [1])
    F3C3=canvas1.create_polygon(c+2.66*x ,  d+9.66*y ,  c+1*x ,     d+9*y ,     c+1*x ,    d+6.66*y , c+2.66*x ,   d+7.32*y  ,outline='black' ,  fill=CC [2] [0] [2])
    F3C4=canvas1.create_polygon(c+4.32*x ,  d+5.69*y ,  c+2.66*x ,  d+5.03*y ,  c+2.66*x , d+2.66*y , c+4.32*x ,   d+3.33*y  ,outline='black' ,  fill=CC [2] [1] [0])
    F3C5=canvas1.create_polygon(c+4.32*x ,  d+8.02*y ,  c+2.66*x ,  d+7.36*y ,  c+2.66*x , d+5.03*y , c+4.32*x ,   d+5.69*y  ,outline='black' ,  fill=CC [2] [1] [1])
    F3C6=canvas1.create_polygon(c+4.32*x ,  d+10.33*y , c+2.66*x ,  d+9.66*y ,  c+2.66*x , d+7.36*y , c+4.32*x ,   d+8.02*y  ,outline='black' ,  fill=CC [2] [1] [2])
    F3C7=canvas1.create_polygon(c+6*x ,     d+6.33*y ,  c+4.32*x ,  d+5.69*y ,  c+4.32*x , d+3.33*y , c+6*x ,      d+4*y     ,outline='black' ,  fill=CC [2] [2] [0])
    F3C8=canvas1.create_polygon(c+6*x ,     d+8.66*y ,  c+4.32*x ,  d+8.02*y ,  c+4.32*x , d+5.69*y , c+6*x ,      d+6.33*y  ,outline='black' ,  fill=CC [2] [2] [1])
    F3C9=canvas1.create_polygon(c+6*x ,     d+11*y ,    c+4.32*x ,  d+10.33*y , c+4.32*x , d+8.02*y , c+6*x ,      d+8.66*y  ,outline='black' ,  fill=CC [2] [2] [2])

# Creation face 4 :

    F4C1=canvas1.create_polygon(c+7.66*x ,  d+5.69*y ,  c+6*x ,     d+6.33*y ,   c+6*x ,    d+4*y ,    c+7.66*x ,  d+3.33*y  ,outline='black' ,  fill=CC [3] [0] [0])
    F4C2=canvas1.create_polygon(c+7.66*x ,  d+8.02*y ,  c+6*x ,     d+8.66*y ,   c+6*x,     d+6.33*y , c+7.66*x,   d+5.69*y  ,outline='black' ,  fill=CC [3] [0] [1])
    F4C3=canvas1.create_polygon(c+7.66*x ,  d+10.33*y , c+6*x ,     d+11*y ,     c+6*x ,    d+8.66*y , c+7.66*x ,  d+8.02*y  ,outline='black' ,  fill=CC [3] [0] [2])
    F4C4=canvas1.create_polygon(c+9.32*x ,  d+5.04*y ,  c+7.66*x ,  d+5.7*y ,    c+7.66*x , d+3.34*y , c+9.32*x ,  d+2.67*y  ,outline='black' ,  fill=CC [3] [1] [0])
    F4C5=canvas1.create_polygon(c+9.32*x ,  d+7.34*y ,  c+7.66*x ,  d+8*y ,      c+7.66*x , d+5.7*y ,  c+9.32*x ,  d+5.04*y  ,outline='black' ,  fill=CC [3] [1] [1])
    F4C6=canvas1.create_polygon(c+9.32*x ,  d+9.67*y ,  c+7.66*x ,  d+10.33*y ,  c+7.66*x , d+8*y ,    c+9.32*x ,  d+7.33*y  ,outline='black' ,  fill=CC [3] [1] [2])
    F4C7=canvas1.create_polygon(c+11*x ,    d+4.36*y ,  c+9.32*x ,  d+5.04*y ,   c+9.32*x , d+2.67*y , c+11*x ,    d+2*y     ,outline='black' ,  fill=CC [3] [2] [0])
    F4C8=canvas1.create_polygon(c+11*x ,    d+6.67*y ,  c+9.32*x ,  d+7.34*y ,   c+9.32*x , d+5.04*y , c+11*x ,    d+4.36*y  ,outline='black' ,  fill=CC [3] [2] [1])
    F4C9=canvas1.create_polygon(c+11*x ,    d+9*y ,     c+9.32*x ,  d+9.67*y ,   c+9.32*x , d+7.33*y , c+11*x ,    d+6.66*y  ,outline='black' ,  fill=CC [3] [2] [2])
  
# Creation face 5   :

    F5C1=canvas1.create_polygon(c+18.66*x , d+5.66*y ,  c+17*x ,    d+6.33*y ,  c+17*x ,    d+4*y ,    c+18.66*x , d+3.33*y  ,outline='black' ,  fill=CC [5] [0] [0])
    F5C2=canvas1.create_polygon(c+18.66*x , d+8*y ,     c+17*x ,    d+8.66*y ,  c+17*x ,    d+6.33*y , c+18.66*x , d+5.66*y  ,outline='black' ,  fill=CC [5] [0] [1])
    F5C3=canvas1.create_polygon(c+18.66*x , d+10.33*y , c+17*x ,    d+11*y ,    c+17*x ,    d+8.66*y , c+18.66*x , d+8*y     ,outline='black' ,  fill=CC [5] [0] [2])
    F5C4=canvas1.create_polygon(c+20.32*x , d+5*y ,     c+18.66*x , d+5.66*y ,  c+18.66*x , d+3.33*y , c+20.32*x , d+2.66*y  ,outline='black' ,  fill=CC [5] [1] [0])
    F5C5=canvas1.create_polygon(c+20.32*x , d+7.33*y ,  c+18.66*x , d+8*y ,     c+18.66*x , d+5.66*y , c+20.32*x , d+5*y     ,outline='black' ,  fill=CC [5] [1] [1])
    F5C6=canvas1.create_polygon(c+20.32*x , d+9.66*y ,  c+18.66*x , d+10.33*y , c+18.66*x , d+8*y ,    c+20.32*x , d+7.33*y  ,outline='black' ,  fill=CC [5] [1] [2])
    F5C7=canvas1.create_polygon(c+22*x ,    d+4.36*y ,  c+20.32*x , d+5*y ,     c+20.32*x , d+2.66*y , c+22*x ,    d+2*y     ,outline='black' ,  fill=CC [5] [2] [0])
    F5C8=canvas1.create_polygon(c+22*x ,    d+6.66*y ,  c+20.32*x , d+7.33*y ,  c+20.32*x , d+5*y ,    c+22*x ,    d+4.36*y  ,outline='black' ,  fill=CC [5] [2] [1])
    F5C9=canvas1.create_polygon(c+22*x ,    d+9*y ,     c+20.32*x , d+9.66*y ,  c+20.32*x , d+7.33*y , c+22*x ,    d+6.66*y  ,outline='black' ,  fill=CC [5] [2] [2])
# Creation face 6 :

    F6C1=canvas1.create_polygon(c+13.66*x , d+5*y ,     c+12*x ,    d+4.36*y ,  c+12*x ,    d+2*y ,    c+13.66*x , d+2.66*y  ,outline='black' ,  fill=CC [4] [2] [0])
    F6C2=canvas1.create_polygon(c+13.66*x , d+7.32*y ,  c+12*x ,    d+6.66*y ,  c+12*x ,    d+4.36*y , c+13.66*x , d+5*y     ,outline='black' ,  fill=CC [4] [2] [1])
    F6C3=canvas1.create_polygon(c+13.66*x , d+9.66*y ,  c+12*x ,    d+9*y ,     c+12*x ,    d+6.66*y , c+13.66*x , d+7.32*y  ,outline='black' ,  fill=CC [4] [2] [2])
    F6C4=canvas1.create_polygon(c+15.32*x , d+5.66*y ,  c+13.66*x , d+5*y ,     c+13.66*x , d+2.66*y , c+15.32*x , d+3.33*y  ,outline='black' ,  fill=CC [4] [1] [0])
    F6C5=canvas1.create_polygon(c+15.32*x , d+8*y ,     c+13.66*x , d+7.32*y ,  c+13.66*x , d+5*y ,    c+15.32*x , d+5.66*y  ,outline='black' ,  fill=CC [4] [1] [1])
    F6C6=canvas1.create_polygon(c+15.32*x , d+10.33*y , c+13.66*x , d+9.66*y ,  c+13.66*x , d+7.32*y , c+15.32*x , d+8*y     ,outline='black' ,  fill=CC [4] [1] [2])
    F6C7=canvas1.create_polygon(c+17*x ,    d+6.33*y ,  c+15.32*x , d+5.66*y ,  c+15.32*x , d+3.33*y , c+17*x ,    d+4*y     ,outline='black' ,  fill=CC [4] [0] [0])
    F6C8=canvas1.create_polygon(c+17*x ,    d+8.66*y ,  c+15.32*x , d+8*y ,     c+15.32*x , d+5.66*y , c+17*x ,    d+6.33*y  ,outline='black' ,  fill=CC [4] [0] [1])
    F6C9=canvas1.create_polygon(c+17*x ,    d+11*y ,    c+15.32*x , d+10.33*y , c+15.32*x , d+8*y ,    c+17*x ,    d+8.66*y  ,outline='black' ,  fill=CC [4] [0] [2])


    
# Functions defining movements

# This function performs a forward movement of the first column

def Mvt1():
    global CC,cm1
    cm1=[[[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]], 
         [[CC[5][2][2],CC[5][2][1],CC[5][2][0]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[2][2][0],CC[2][1][0],CC[2][0][0]],[CC[2][2][1],CC[2][1][1],CC[2][0][1]],[CC[2][2][2],CC[2][1][2],CC[2][0][2]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
         [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[0][0][2],CC[0][0][1],CC[0][0][0]]]]

    CC=cm1

    cube_init ()
    

# This function performs a backward movement of the first column
def Mvt2():
    global CC,cm2
    
    cm2=[[[CC[5][2][0],CC[5][2][1],CC[5][2][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
         [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[2][0][2],CC[2][1][2],CC[2][2][2]],[CC[2][0][1],CC[2][1][1],CC[2][2][1]],[CC[2][0][0],CC[2][1][0],CC[2][2][0]]],
         [[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[4][2][0],CC[4][1][0],CC[4][0][0]],[CC[4][2][1],CC[4][1][1],CC[4][0][1]],[CC[4][2][2],CC[4][1][2],CC[4][0][2]]],
         [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[1][0][0],CC[1][0][1],CC[1][0][2]]]]
    CC=cm2

    cube_init ()
        
# Mvt3 corresponds to the forward movement of the 2nd column

def Mvt3():
    global CC,cm3
    cm3=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[5][1][2],CC[5][1][1],CC[5][1][0]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
         [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
         [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[0][1][2],CC[0][1][1],CC[0][1][0]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm3

    cube_init ()
        
# Mvt4 corresponds to the backward movement of the 2nd column

def Mvt4():
    global CC,cm4

    cm4=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]], 
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
         [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
         [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm4

    cube_init ()
        

# Mvt5 corresponds to the forward movement of the 3rd column

def Mvt5 ():
    global CC ,cm5
    cm5=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[5][0][2],CC[5][0][1],CC[5][0][0]]],
         [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
         [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[4][0][2],CC[4][1][2],CC[4][2][2]],[CC[4][0][1],CC[4][1][1],CC[4][2][1]],[CC[4][0][0],CC[4][1][0],CC[4][2][0]]],
         [[CC[0][2][2],CC[0][2][1],CC[0][2][0]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm5

    cube_init ()
        

# Mvt6 corresponds to the backward movement of the 3rd column

def Mvt6():
   global CC,cm6
   cm6=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[5][0][2],CC[5][0][1],CC[5][0][0]]],
        [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
        [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
        [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
        [[CC[4][2][0],CC[4][1][0],CC[4][0][0]],[CC[4][2][1],CC[4][1][1],CC[4][0][1]],[CC[4][2][2],CC[4][1][2],CC[4][0][2]]],
        [[CC[1][2][2],CC[1][2][1],CC[1][2][0]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
   CC=cm6

   cube_init ()
    
# Mvt7 corresponds to the movement to the left of the 1st line

def Mvt7():
    global CC ,cm7
    cm7=[[[CC[0][0][2],CC[0][1][2],CC[0][2][2]],[CC[0][0][1],CC[0][1][1],CC[0][2][1]],[CC[0][0][0],CC[0][1][0],CC[0][2][0]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[3][0][0],CC[2][0][1],CC[2][0][2]],[CC[3][1][0],CC[2][1][1],CC[2][1][2]],[CC[3][2][0],CC[2][2][1],CC[2][2][2]]],
         [[CC[4][0][0],CC[3][0][1],CC[3][0][2]],[CC[4][1][0],CC[3][1][1],CC[3][1][2]],[CC[4][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[5][0][0],CC[4][0][1],CC[4][0][2]],[CC[5][1][0],CC[4][1][1],CC[4][1][2]],[CC[5][2][0],CC[4][2][1],CC[4][2][2]]],
         [[CC[2][0][0],CC[5][0][1],CC[5][0][2]],[CC[2][1][0],CC[5][1][1],CC[5][1][2]],[CC[2][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm7

    cube_init ()


# Mvt8 corresponds to the movement to the right of the 1st line

def Mvt8():
    global CC ,cm8
    cm8=[[[CC[0][2][0],CC[0][1][0],CC[0][0][0]],[CC[0][2][1],CC[0][1][1],CC[0][0][1]],[CC[0][2][2],CC[0][1][2],CC[0][0][2]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[5][0][0],CC[2][0][1],CC[2][0][2]],[CC[5][1][0],CC[2][1][1],CC[2][1][2]],[CC[5][2][0],CC[2][2][1],CC[2][2][2]]],
         [[CC[2][0][0],CC[3][0][1],CC[3][0][2]],[CC[2][1][0],CC[3][1][1],CC[3][1][2]],[CC[2][2][0],CC[3][2][1],CC[3][2][2]]],
         [[CC[3][0][0],CC[4][0][1],CC[4][0][2]],[CC[3][1][0],CC[4][1][1],CC[4][1][2]],[CC[3][2][0],CC[4][2][1],CC[4][2][2]]],
         [[CC[4][0][0],CC[5][0][1],CC[5][0][2]],[CC[4][1][0],CC[5][1][1],CC[5][1][2]],[CC[4][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm8

    cube_init ()


# Mvt9 corresponds to the movement to the left of the 2nd line
def Mvt9():
    global CC ,cm9
    cm9=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
         [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
         [[CC[2][0][0],CC[3][0][1],CC[2][0][2]],[CC[2][1][0],CC[3][1][1],CC[2][1][2]],[CC[2][2][0],CC[3][2][1],CC[2][2][2]]],
         [[CC[3][0][0],CC[4][0][1],CC[3][0][2]],[CC[3][1][0],CC[4][1][1],CC[3][1][2]],[CC[3][2][0],CC[4][2][1],CC[3][2][2]]],
         [[CC[4][0][0],CC[5][0][1],CC[4][0][2]],[CC[4][1][0],CC[5][1][1],CC[4][1][2]],[CC[4][2][0],CC[5][2][1],CC[4][2][2]]],
         [[CC[5][0][0],CC[2][0][1],CC[5][0][2]],[CC[5][1][0],CC[2][1][1],CC[5][1][2]],[CC[5][2][0],CC[2][2][1],CC[5][2][2]]]]
    CC=cm9

    cube_init ()
        

# Mvt 10 corresponds to the movement to the right of the 2nd line

def Mvt10():
    global CC ,cm10
    cm10=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
          [[CC[1][0][0],CC[1][0][1],CC[1][0][2]],[CC[1][1][0],CC[1][1][1],CC[1][1][2]],[CC[1][2][0],CC[1][2][1],CC[1][2][2]]],
          [[CC[2][0][0],CC[5][0][1],CC[2][0][2]],[CC[2][1][0],CC[5][1][1],CC[2][1][2]],[CC[2][2][0],CC[5][2][1],CC[2][2][2]]],
          [[CC[3][0][0],CC[2][0][1],CC[3][0][2]],[CC[3][1][0],CC[2][1][1],CC[3][1][2]],[CC[3][2][0],CC[2][2][1],CC[3][2][2]]],
          [[CC[4][0][0],CC[3][0][1],CC[4][0][2]],[CC[4][1][0],CC[3][1][1],CC[4][1][2]],[CC[4][2][0],CC[3][2][1],CC[4][2][2]]],
          [[CC[5][0][0],CC[4][0][1],CC[5][0][2]],[CC[5][1][0],CC[4][1][1],CC[5][1][2]],[CC[5][2][0],CC[4][2][1],CC[5][2][2]]]]
    CC=cm10

    cube_init ()
    

# Mvt 11 corresponds to the movement to the left of the 3rd line

def Mvt11():
    global CC ,cm11
    cm11=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
          [[CC[1][2][0],CC[1][1][0],CC[1][0][0]],[CC[1][2][1],CC[1][1][1],CC[1][0][1]],[CC[1][2][2],CC[1][1][2],CC[1][0][2]]],
          [[CC[2][0][0],CC[2][0][1],CC[3][0][2]],[CC[2][1][0],CC[2][1][1],CC[3][1][2]],[CC[2][2][0],CC[2][2][1],CC[3][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[4][0][2]],[CC[3][1][0],CC[3][1][1],CC[4][1][2]],[CC[3][2][0],CC[3][2][1],CC[4][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[5][0][2]],[CC[4][1][0],CC[4][1][1],CC[5][1][2]],[CC[4][2][0],CC[4][2][1],CC[5][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[2][0][2]],[CC[5][1][0],CC[5][1][1],CC[2][1][2]],[CC[5][2][0],CC[5][2][1],CC[2][2][2]]]]
    CC=cm11

    cube_init ()
      

# Mvt 12 corresponds to the movement to the right of the 3rd line

def Mvt12():
    global CC ,cm12
    cm12=[[[CC[0][0][0],CC[0][0][1],CC[0][0][2]],[CC[0][1][0],CC[0][1][1],CC[0][1][2]],[CC[0][2][0],CC[0][2][1],CC[0][2][2]]],
          [[CC[1][0][2],CC[1][1][2],CC[1][2][2]],[CC[1][0][1],CC[1][1][1],CC[1][2][1]],[CC[1][0][0],CC[1][1][0],CC[1][2][0]]],
          [[CC[2][0][0],CC[2][0][1],CC[5][0][2]],[CC[2][1][0],CC[2][1][1],CC[5][1][2]],[CC[2][2][0],CC[2][2][1],CC[5][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[2][0][2]],[CC[3][1][0],CC[3][1][1],CC[2][1][2]],[CC[3][2][0],CC[3][2][1],CC[2][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[3][0][2]],[CC[4][1][0],CC[4][1][1],CC[3][1][2]],[CC[4][2][0],CC[4][2][1],CC[3][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[4][0][2]],[CC[5][1][0],CC[5][1][1],CC[4][1][2]],[CC[5][2][0],CC[5][2][1],CC[4][2][2]]]]
    CC=cm12

    cube_init ()
     

def Mvt13():
    global CC,cm13
    cm13=[[[CC[4][2][0],CC[0][0][1],CC[0][0][2]],[CC[4][2][1],CC[0][1][1],CC[0][1][2]],[CC[4][2][2],CC[0][2][1],CC[0][2][2]]],
          [[CC[1][0][0],CC[1][0][1],CC[2][0][0]],[CC[1][1][0],CC[1][1][1],CC[2][0][1]],[CC[1][2][0],CC[1][2][1],CC[2][0][2]]],
          [[CC[0][2][0],CC[0][1][0],CC[0][0][0]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[1][2][2],CC[1][1][2],CC[1][0][2]]],
          [[CC[5][0][2],CC[5][1][2],CC[5][2][2]],[CC[5][0][1],CC[5][1][1],CC[5][2][1]],[CC[5][0][0],CC[5][1][0],CC[5][2][0]]]]
    CC=cm13

    cube_init ()     
        
def Mvt14():
    global CC,cm14
    cm14=[[[CC[2][0][2],CC[0][0][1],CC[0][0][2]],[CC[2][0][1],CC[0][1][1],CC[0][1][2]],[CC[2][0][0],CC[0][2][1],CC[0][2][2]]],
          [[CC[1][0][0],CC[1][0][1],CC[4][2][2]],[CC[1][1][0],CC[1][1][1],CC[4][2][1]],[CC[1][2][0],CC[1][2][1],CC[4][2][0]]],
          [[CC[1][0][2],CC[1][1][2],CC[1][2][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[0][0][0],CC[0][1][0],CC[0][2][0]]],
          [[CC[5][2][0],CC[5][1][0],CC[5][0][0]],[CC[5][2][1],CC[5][1][1],CC[5][0][1]],[CC[5][2][2],CC[5][1][2],CC[5][0][2]]]]
    CC=cm14

    cube_init ()
  
        
def Mvt15():
    global CC,cm15
    cm15=[[[CC[0][0][0],CC[4][1][0],CC[0][0][2]],[CC[0][1][0],CC[4][1][1],CC[0][1][2]],[CC[0][2][0],CC[4][1][2],CC[0][2][2]]],
          [[CC[1][0][0],CC[2][1][0],CC[1][0][2]],[CC[1][1][0],CC[2][1][1],CC[1][1][2]],[CC[1][2][0],CC[2][1][2],CC[1][2][2]]],
          [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[0][2][1],CC[0][1][1],CC[0][0][1]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[1][2][1],CC[1][1][1],CC[1][0][1]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm15

    cube_init ()    
        

def Mvt16():
    global CC,cm16
    cm16=[[[CC[0][0][0],CC[2][1][2],CC[0][0][2]],[CC[0][1][0],CC[2][1][1],CC[0][1][2]],[CC[0][2][0],CC[2][1][0],CC[0][2][2]]],
          [[CC[1][0][0],CC[4][1][2],CC[1][0][2]],[CC[1][1][0],CC[4][1][1],CC[1][1][2]],[CC[1][2][0],CC[4][1][0],CC[1][2][2]]],
          [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[1][0][1],CC[1][1][1],CC[1][2][1]],[CC[2][2][0],CC[2][2][1],CC[2][2][2]]],
          [[CC[3][0][0],CC[3][0][1],CC[3][0][2]],[CC[3][1][0],CC[3][1][1],CC[3][1][2]],[CC[3][2][0],CC[3][2][1],CC[3][2][2]]],
          [[CC[4][0][0],CC[4][0][1],CC[4][0][2]],[CC[0][0][1],CC[0][1][1],CC[0][2][1]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm16

    cube_init ()
    

def Mvt17():
    global CC,cm17
    cm17=[[[CC[0][0][0],CC[0][0][1],CC[4][0][0]],[CC[0][1][0],CC[0][1][1],CC[4][0][1]],[CC[0][2][0],CC[0][2][1],CC[4][0][2]]],
          [[CC[2][2][0],CC[1][0][1],CC[1][0][2]],[CC[2][2][1],CC[1][1][1],CC[1][1][2]],[CC[2][2][2],CC[1][2][1],CC[1][2][2]]],
          [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[0][2][2],CC[0][1][2],CC[0][0][2]]],
          [[CC[3][2][0],CC[3][1][0],CC[3][0][0]],[CC[3][2][1],CC[3][1][1],CC[3][0][1]],[CC[3][2][2],CC[3][1][2],CC[3][0][2]]],
          [[CC[1][2][0],CC[1][1][0],CC[1][0][0]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm17

    cube_init ()


def Mvt18():
    global CC,cm18
    cm18=[[[CC[0][0][0],CC[0][0][1],CC[2][2][2]],[CC[0][1][0],CC[0][1][1],CC[2][2][1]],[CC[0][2][0],CC[0][2][1],CC[2][2][0]]],
          [[CC[4][0][2],CC[1][0][1],CC[1][0][2]],[CC[4][0][1],CC[1][1][1],CC[1][1][2]],[CC[4][0][0],CC[1][2][1],CC[1][2][2]]],
          [[CC[2][0][0],CC[2][0][1],CC[2][0][2]],[CC[2][1][0],CC[2][1][1],CC[2][1][2]],[CC[1][0][0],CC[1][1][0],CC[1][2][0]]],
          [[CC[3][0][2],CC[3][1][2],CC[3][2][2]],[CC[3][0][1],CC[3][1][1],CC[3][2][1]],[CC[3][0][0],CC[3][1][0],CC[3][2][0]]],
          [[CC[0][0][2],CC[0][1][2],CC[0][2][2]],[CC[4][1][0],CC[4][1][1],CC[4][1][2]],[CC[4][2][0],CC[4][2][1],CC[4][2][2]]],
          [[CC[5][0][0],CC[5][0][1],CC[5][0][2]],[CC[5][1][0],CC[5][1][1],CC[5][1][2]],[CC[5][2][0],CC[5][2][1],CC[5][2][2]]]]
    CC=cm18

    cube_init ()
    

# Buttons 

# Creation of buttons allowing movements

def buttons():
     
    Bmvt1 = Button(window1, text="Mvt1", bg= 'red' , font= "Helvetica 12 bold" , command=Mvt1 , image = photo)
    Bmvt1_window1 = canvas1.create_window(3.5*x, 105, window=Bmvt1)

    Bmvt2 = Button(window1, text="Mvt2", bg= 'red' , font= "Helvetica 12 bold" , command=Mvt2 , image = photo2)
    Bmvt2_window1 = canvas1.create_window(23.25*x, 430, window=Bmvt2)

    Bmvt3 = Button(window1, text="Mvt3", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt3 , image = photo)
    Bmvt3_window1 = canvas1.create_window(5.25*x, 80, window=Bmvt3)
    
    Bmvt4 = Button(window1, text="Mvt4", bg= 'red' , font= "Helvetica 12 bold" , command=Mvt4 , image = photo2)
    Bmvt4_window1 = canvas1.create_window(21.5*x, 455, window=Bmvt4)

    Bmvt5 = Button(window1, text="Mvt5", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt5 , image = photo)
    Bmvt5_window1 = canvas1.create_window(7*x, 55 , window=Bmvt5)
    
    Bmvt6 = Button(window1, text="Mvt6", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt6 , image = photo2)
    Bmvt6_window1 = canvas1.create_window(20*x, 475 , window=Bmvt6)

    Bmvt7 = Button(window1, text="Mvt7", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt7 , image = photo3)
    Bmvt7_window1 = canvas1.create_window(2*x, 180, window=Bmvt7)

    Bmvt8 = Button(window1, text="Mvt8", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt8 , image = photo1)
    Bmvt8_window1 = canvas1.create_window(25*x, 180 , window=Bmvt8)

    Bmvt9 = Button(window1, text="Mvt9", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt9 , image = photo3)
    Bmvt9_window1 = canvas1.create_window(2*x, 265, window=Bmvt9)

    Bmvt10 = Button(window1, text="Mvt10", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt10 , image = photo1)
    Bmvt10_window1 = canvas1.create_window(25*x, 265, window=Bmvt10)

    Bmvt11 = Button(window1, text="Mvt11", bg= 'red' , font= "Helvetica 12 bold" , command=Mvt11 , image = photo3)
    Bmvt11_window1 = canvas1.create_window(2*x, 350, window=Bmvt11)

    Bmvt12 = Button(window1, text="Mvt12", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt12 , image = photo1)
    Bmvt12_window1 = canvas1.create_window(25*x , 350, window=Bmvt12)

    Bmvt13 = Button(window1, text="Mvt13", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt13 , image = photo2)
    Bmvt13_window1 = canvas1.create_window(3.5*x , 460, window=Bmvt13)

    Bmvt14 = Button(window1, text="Mvt14", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt14 , image = photo)
    Bmvt14_window1 = canvas1.create_window(20*x, 65 , window=Bmvt14)

    Bmvt15 = Button(window1, text="Mvt15", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt15 , image = photo2)
    Bmvt15_window1 = canvas1.create_window(5.25*x , 480, window=Bmvt15)

    Bmvt16 = Button(window1, text="Mvt16", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt16 , image = photo)
    Bmvt16_window1 = canvas1.create_window(21.5*x , 85, window=Bmvt16)

    Bmvt17 = Button(window1, text="Mvt17", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt17 , image = photo2)
    Bmvt17_window1 = canvas1.create_window(7*x , 500, window=Bmvt17)

    Bmvt18 = Button(window1, text="Mvt18", bg= 'red', font= "Helvetica 12 bold"  , command=Mvt18 , image = photo)
    Bmvt18_window1 = canvas1.create_window(23.25*x , 108, window=Bmvt18)


# Function that shuffles

def shuffle_cube():

    i = 0

    while i < 30 : # 30 iterations

        j = random.randint(1,19)

        if j == 1 :

            Mvt1()

        elif j == 2 :

            Mvt2()

        elif j == 3 :

            Mvt3()

        elif j == 4 :

            Mvt4()

        elif j == 5 :

            Mvt5()

        elif j == 6 :

            Mvt6()

        elif j == 7 :

            Mvt7()

        elif j == 8 :

            Mvt8()

        elif j == 9 :

            Mvt9()

        elif j == 10 :

            Mvt10()

        elif j == 11 :

            Mvt11()

        elif j == 11 :

            Mvt2()

        elif j == 12 :

            Mvt12()

        elif j == 13 :

            Mvt13()

        elif j == 14 :

            Mvt14()

        elif j == 15 :

            Mvt15()

        elif j == 16 :

            Mvt16()

        elif j == 17 :

            Mvt17()

        else :

            Mvt18()

        i += 1

# Function that solves the cube by reset

def solve_cube() :

    global CCstr
    CCstr = 'rrrrrrrrrooooooooowwwwwwwwwgggggggggyyyyyyyyybbbbbbbbb'
    CCconvert(1)
    cube_init()

# Function that creates a save using a QR code

def QR_save() :
    
    global CCstr
    
    if os.path.exists("save.jpg"):
          os.remove("save.jpg")
          
    CCconvert(0)
    img = qrcode.make(CCstr)
    img.show()
    img.save("save.jpg")

 
    
# Reads QR data from file and sets cube
    
def QRread1(): 

    global qrdatastr
    global CCstr

    def BarcodeReader(image): 

        global qrdatastr
        img = cv2.imread(image) 
        detectedBarcodes = decode(img) 
       

        if not detectedBarcodes:
            
            print("Waiting for QR code ...")
            
        else: 
        
        
            for barcode in detectedBarcodes:   
             
                (x, y, w, h) = barcode.rect 
                cv2.rectangle(img, (x-10, y-10), (x + w+10, y + h+10), (255, 0, 0), 2) 
                if barcode.data!=" ": 
        
                    qrdata = barcode.data
                    qrdatastr = str(qrdata)[2:56]
                  
        cv2.imshow("QR Save Code", img) 
        
    
  
    if __name__ == "__main__": 
   
        image="save.jpg"
        BarcodeReader(image)

    CCstr = qrdatastr
    CCconvert(1)
    cube_init ()

# Reads QR data from camera and sets cube

def QRread2():

    global qrdatastr
    global CCstr

    def BarcodeReader(image): 

        global qrdatastr
        
        img = image
        cv2.imshow("Image", img) 
    
        detectedBarcodes = decode(img) 
       
    
        if not detectedBarcodes: 
            print("Waiting for QR code ...")
            cv2.imshow("Image", img) 
        else : 
        
          
            for barcode in detectedBarcodes:   
            
            
                (x, y, w, h) = barcode.rect 
              
         
                cv2.rectangle(img, (x-10, y-10), (x + w+10, y + h+10),  (0, 0, 255), 5) 
              
                if barcode.data!=" ": 
                
                    dir1 = barcode.data
                    qrdatastr = str(dir1)[2:56]
                    print("QR code detected")
                    cv2.imshow("Image", img) 
    

    window2 = cv2.VideoCapture(0)
    qrdatastr = ''

    while qrdatastr == '' :

        a, b = window2.read()
        BarcodeReader(b)
        k = cv2.waitKey(100)

        if qrdatastr != '' :

            window2.release()
            cv2.destroyAllWindows()
            break

    CCstr = qrdatastr
    CCconvert(1)
    cube_init ()
        
# arrow image definition
photo = PhotoImage(file='arrowup.png')
photo1 = PhotoImage(file='arrowright.png')
photo2 = PhotoImage(file='arrowdown.png')
photo3 = PhotoImage(file='arrowleft.png')


# Creation of the button used to close the window
close = Button(window1, text="Exit", bd= 10 , activebackground ='red',command=window1.destroy)
close_window1 = canvas1.create_window(40, 40, window=close)

# Creation of the button used to shuffle
shuffle = Button(window1, text="Shuffle", bd= 10 , activebackground ='red',command=shuffle_cube)
shuffle_window1 = canvas1.create_window(185, 570, window=shuffle)

# Creation of the button used to solve
solve = Button(window1, text="Solve", bd= 10 , activebackground ='red',command=solve_cube)
solve_window1 = canvas1.create_window(185, 630, window=solve)

# Creation of the button used to create and display QR code
QRSave = Button(window1, text="QR Save", bd= 10 , activebackground ='red',command=QR_save)
QRSave_window1 = canvas1.create_window(470, 600, window=QRSave)

# Creation of the button used to read previously generated QR code
qrread = Button(window1, text = "QR Reload from File", bd= 10 , activebackground ='red', command = QRread1)
qrread_window1 = canvas1.create_window(755 , 570, window=qrread)

# Creation of the button used to read previously generated QR code
imageqr = Button(window1, text="QR Reload from Image", bd= 10 , activebackground ='red', command=QRread2)
imageqr_window1 = canvas1.create_window(755, 630, window=imageqr)

# Title
phrase = Label(canvas1, text="Virtual Python Cube", fg='black', font= "Helvetica 22 bold")
phrase.pack()
canvas1.create_window(485, 40, window=phrase)

cube_init()
buttons()

window1.mainloop()

