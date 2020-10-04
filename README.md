# bongorecording
This script merge the video and the audio from bongo recordings  
*normally it's separated [screencast,sound]
<p>
<b>INSTALL dependency</b><br>
1. <code>pip install ffmpeg-python</code><br>
2. (Optionall) You can add location of your bongorecording.py folder to PATH environment variable to be able run it system wide
</p>
<p>
<b>RUN</b><br>
   <code>bongorecording.py path_to_unzipped_folder</code><br>
   It will merge content and save it in a current directory as Recording.mp4
</p>
<p>
<b>Unix systems only:</b><br>
  As it relays on ffmpeg library, you can merge contents manually with command:<br>
  <code>ffmpeg -i screencast.mp4 -i audio.mp4 -c:v copy -c:a Lecture.mp4</code>
<p>
Please report here if there is something wrong with this script<br>
Thank you
