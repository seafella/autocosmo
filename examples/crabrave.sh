#!/bin/sh
# dependencies: ffmpeg (ppplay), sox

wget https://justine.lol/printvideo.com
chmod +x ./printvideo.com

wget https://justine.lol/crabrave.mpg
./printvideo.com -ts crabrave.mpg

# wget http://75.119.140.255:8083/videos/1703213347___discord001___1186105773500158024___1187396127855739001_-_-_-___output_video.mp4_captions.mp4_title.mp4_final.mp4
# ffmpeg -i 1703213347___discord001___1186105773500158024___1187396127855739001_-_-_-___output_video.mp4_captions.mp4_title.mp4_final.mp4 saysee.mpg
# ./printvideo.com -ts saysee.mpg
