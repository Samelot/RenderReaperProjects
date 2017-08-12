# use python3!!
# python3 -m tabnanny -v render-project-tracks.py

import sys
import os
import subprocess
import argparse
import glob

if sys.platform == "win32":
    FFMPEG_BIN = "ffmpeg.exe"
    MOVE = "move "
    MKDIR = "md "
    REAPER = r"C:\Program Files\REAPER (x64)\reaper.exe"
elif sys.platform == 'linux' or sys.platform == 'linux2':
    FFMPEG_BIN = "ffmpeg"
    MOVE = "mv "
    MKDIR = "mkdir "
elif sys.platform == 'darwin':
    FFMPEG_BIN = "ffmpeg"
    MOVE = "mv "
    MKDIR = "mkdir "
    REAPER = "/Applications/REAPER64.app/Contents/MacOS/REAPER"

def render(projectsDir):
    # home = os.path.expanduser("~")

    reaperProjectsArray = []

    winPATH = r"C:\Users\Pixel Academy\Documents\Reaper\sam\sam.rpp"
    macPATH = r"/Users/samenglander/_dev/RenderReaperProjects/Andorra/AndorraQuantizeFinal.rpp"

    if projectsDir:
        projectsDir = projectsDir       
    else:
        projectsDir = os.path.dirname(os.path.realpath(__file__))

    target = projectsDir + "/*/*.RPP"
    
    for f in glob.iglob(target):
    	reaperProjectsArray.append(f)

    for i in range(len(reaperProjectsArray)):
    	cmd = [REAPER, '-renderproject', reaperProjectsArray[i]]
    	output = subprocess.check_output(cmd)

    # print(len(reaperProjectsArray))

    #cmd = [REAPER, '-h']
    # cmd = [REAPER, '-renderproject', target]
    #cmd = [REAPER, '-cfgfile', 'REAPER.ini', '-renderproject', winPATH]
    
    #output = subprocess.check_output(cmd)
    # output = subprocess.call(cmd)
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='?', action='store')
    args = parser.parse_args()
    return (args.input)
    
if __name__ == '__main__':
    p = main()
    render(p)