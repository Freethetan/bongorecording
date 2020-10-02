#!/usr/bin/env python3
# -*- coding: utf8 -*-

import ffmpeg
import sys
import os

fname="Recording"
fext=".mp4"

def helpinfo():
        print('''
This script merge the video and the audio from bongo recordings
 *normally its separated [screencast,sound]
USAGE:
        ''')
        print(" "+sys.argv[0]+" dir_path")
        print(" otput will be "+fname+fext)

def mergecontent(vpath,apath,outpath):
        vinput = ffmpeg.input(vpath)
        ainput = ffmpeg.input(apath)
        (
                ffmpeg
                .concat(vinput, ainput)
                .output(outpath)
                .run()
        )

def getcontentfiles(path):
        files=[];
        for filename in os.listdir(videofile):
                if filename.endswith(fext):
                        files.append(os.path.join(videofile,filename))
        return files
if len(sys.argv) == 1:
        helpinfo();
        sys.exit();

videofile = sys.argv[1]
'''Change into subdirectory in case it is a top directory'''
if os.path.isdir(videofile) and os.path.isdir(os.path.join(videofile,"meetingFiles")):
        videofile = os.path.join(videofile,"meetingFiles");
'''Get bongo files that contain video and audio'''
contfiles = getcontentfiles(videofile)
'''Get next lecture number'''
prefix="";
if os.path.isfile(fname+fext):
        num=1;
        while os.path.isfile(fname+str(num)+fext):
                num+=1;
        prefix=str(num)

mergecontent(contfiles[0],contfiles[1],fname+str(prefix)+fext)
