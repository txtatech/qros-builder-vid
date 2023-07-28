# qros-builder-vid
Builds KolibriOS from qr codes embedded in a video and launches the small assembly written OS in qemu.

This is a video version fork of: https://github.com/txtatech/qros-builder

Step 1:

Build the qr codes from the .img file

python3 qros-ii-step-1.py

Step 2: *MOVE ORIGINAL IMG FILE BEFORE THIS STEP*

Build a new .img file from the qr codes and launch it with qemu.

python3 qros-ii-step-2.py

or to build the img file and run qemu afterward

python3 qros-ii-step-2_qemu.py


### NOTES:
The README has the wrong ffmpeg command. The correct command is:

ffmpeg -framerate 30 -i qr_%09d.png -vf "scale=730:730,setsar=1" -an -c:v libx264 -pix_fmt yuv420p output.mp4

Good for testing from terminal:

qemu-system-i386 -m 512 -fda kolibri.img -boot a

Needed in script:
qemu_command = ["qemu-system-i386", "-m", "512", "-boot", "a", "-fda", img_file_path]

In the qros-ii-step-1.py file the chunk_size=376 must always be divisible by four or it will cause gzip to error during decompression.

![Example-1](https://github.com/txtatech/qros-builder-vid/blob/main/qros-builder-vid/examples/Example-1.png)
