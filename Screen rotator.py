#Pls check the Readme file before using it there you will find which module you need to install and everything else.
import rotatescreen #pip install rotate-screen

screen = rotatescreen.get_primary_display()

screen.rotate_to(0) #replace 0 with any angle as 90, 180 or 270 at which you want your screen to be rotated
