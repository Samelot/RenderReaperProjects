import sys
import os
import subprocess
import argparse
import glob

if sys.platform == "win32":
    FFMPEG_BIN = "ffmpeg.exe"
    MOVE = "move "
    MKDIR = "md "
    REAPER = "\Program Files\REAPER (x64)"
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

    if projectsDir:
		projectsDir = projectsDir     	
    else:
    	projectsDir = os.path.dirname(os.path.realpath(__file__))
   
    target = projectsDir + "/*/*.RPP"
    for f in glob.iglob(target):
		print f
    
    cmd = [REAPER, '-h']
    #output = subprocess.check_output(cmd)
    #output = subprocess.call(cmd)
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', nargs='?', action='store')
    args = parser.parse_args()
    return (args.input)
    
if __name__ == '__main__':
    p = main()
    render(p)