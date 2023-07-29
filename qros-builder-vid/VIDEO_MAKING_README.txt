After building the png qr codes run the following in the qrs directory:

ffmpeg -framerate 30 -i qr_%09d.png -vf "scale=850:850,setsar=1" -an -c:v libx264 -pix_fmt yuv420p output.mp4

checking frames

ffmpeg -i output.mp4 -vframes 10 frame%03d.png
