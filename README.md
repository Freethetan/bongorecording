# bongorecording
This script merge the video and the audio from bongo recordings  
*normally its separated [screencast,sound]

# INSTALL dependency
1. pip install ffmpeg-python

# Run 
1. bongorecording.py path_to_unzipped_folder

As it relays on ffmpeg library, you can merge contents manually with command:
# ffmpeg -i screencast.mp4 -i audio.mp4 -c:v copy -c:a Lecture.mp4



Please report here if there is something wrong with this script
Thank you
