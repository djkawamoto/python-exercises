# !usr/local/bin/python2
# The Tech Academy
# Python Course step 67 of 79
# shutil drill by Daniel Kawamoto

import shutil
import os

def MoveTextFiles():
    src = os.listdir("/Users/danielkawamoto/Desktop/PyShutilDrill/A/")
    dst = "/Users/danielkawamoto/Desktop/PyShutilDrill/B/"
    for _file in src:
        if _file.endswith(".txt"):
            print ('Old location:\t'+os.path.join(os.path.abspath('A/%s'% _file)))
            shutil.move(os.path.join(os.path.abspath('A/%s'% _file)), dst)
            print ('New location:\t'+os.path.join(os.path.abspath('B/%s'% _file))+'\n\t')
        else:
            print('This shouldn\'t be printed')
MoveTextFiles()
