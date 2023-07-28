import cv2
from pyzbar.pyzbar import decode
import base64
import gzip

# Open the video capture
video_capture = cv2.VideoCapture('qr-test.mp4')

def safe_base64_decode(data):
    data = data.decode("utf-8")  # Decode the bytes to a string
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += '=' * (4 - missing_padding)
    return base64.urlsafe_b64decode(data)

# Initialize an empty list to hold the data from each QR code in the video
data_chunks = []
prev_chunk = None

while True:
    # Read a frame from the video
    ret, frame = video_capture.read()

    # Check if the frame was read successfully
    if not ret:
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Decode QR codes from the frame
    decoded_objects = decode(gray_frame)

    # Process the decoded data and append to data_chunks
    for obj in decoded_objects:
        decoded_data = safe_base64_decode(obj.data)
        if decoded_data != prev_chunk:
            data_chunks.append(decoded_data)
            prev_chunk = decoded_data

    # Exit the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Finished processing frames, releasing video capture...")
video_capture.release()

print("Concatenating and decompressing data...")
data = b''.join(data_chunks)

try:
    # Decompress the full data
    decompressed_data = gzip.decompress(data)
    with open("kolibri.img", "wb") as out_file:
        out_file.write(decompressed_data)
    print("Data decompressed and written to 'kolibri.img'.")
except Exception as e:
    print(f"Exception occurred during decompression: {e}")

print("Finished.")
