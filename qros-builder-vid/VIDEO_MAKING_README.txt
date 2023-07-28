After building the png qr codes run the following in the qrs directory:

ffmpeg -i output.mp4 -vframes 10 frame%03d.png
