# QROS BUILDER

This project is about encoding a binary file into a sequence of QR codes, generating a video from these QR codes, and then decoding the video back into the original file.

## Process Breakdown

Here's how our script works:

1. **Input Data**: The input to this script is a binary file (for example, an image file). We read this file as binary data.

2. **Data Compression**: The binary data is compressed using the `gzip` module to reduce the size of the data that needs to be encoded in the QR codes.

3. **Base64 Encoding**: After compression, the data is converted to a format that can be safely included in a QR code. This is achieved by encoding the compressed data as a base64 string. The base64 encoding scheme represents binary data in an ASCII string format.

4. **Chunking**: The base64 string can be quite large for big files. To handle this, we break the string into smaller chunks. Each chunk is 376 characters long. This chunk size works well with the `ERROR_CORRECT_M` level of error correction in QR code generation and is a multiple of 4, which is important for correct base64 encoding and decoding.

5. **QR Code Generation**: For each chunk, we generate a QR code. We use the `qrcode` library for this, setting the error correction level to `ERROR_CORRECT_M`. This level allows up to 15% of the data to be corrected if it's corrupted, providing a good balance between data capacity and error tolerance.

6. **Video Generation**: We use OpenCV's video writer function to create a video from the QR codes. Each frame of the video is a QR code that encodes a chunk of the base64 string. The video file format is MP4, and the resolution of the video is 730x730 pixels. This resolution ensures that the QR codes are clear and unaltered.

7. **QR Code Decoding**: The video is then read frame by frame. Each frame (a QR code) is decoded to get the base64 string back. We use the `pyzbar` library for decoding the QR codes.

8. **Base64 Decoding and Data Decompression**: The base64 string chunks are concatenated to get the complete base64 string, which is then decoded back to the compressed binary data. The compressed data is decompressed using `gzip` to get back the original binary data. This data is written to an output file.

## Setup and Run

You'll need Python 3.6 or later and the following Python packages installed:

- `cv2` (opencv-python)
- `numpy`
- `qrcode`
- `pyzbar`

To run the script, put your input file in the same directory as the script and replace `'kolibri.img'` in the script with your file name.

Then, simply run the script with Python:

```bash
python3 qros-builder.py
```

The output file will be named `decoded_kolibri.img`.