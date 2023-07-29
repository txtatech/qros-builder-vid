import qrcode
import gzip
import base64
import os
import glob
from PIL import Image
from pyzbar.pyzbar import decode

def decode_qr_code(file_name):
    # Open the image file
    img = Image.open(file_name)

    # Decode the QR code
    data = decode(img)[0].data.decode("utf-8")

    return data

def decode_base64_and_decompress_qr(dir_path):
    # Get the file names of all the QR codes in the directory
    file_names = sorted(glob.glob(os.path.join(dir_path, '*.png')))

    # Initialize an empty string to store all the chunks
    encoded_data_base64 = ''

    for i, file_name in enumerate(file_names):
        # Decode the QR code
        chunk = decode_qr_code(file_name)

        # Append the chunk to the encoded_data_base64 string
        encoded_data_base64 += chunk

        # Print the size of each chunk
        print(f"Size of chunk {i}: {len(chunk)}")

    # Decode the base64 data
    compressed_data = base64.urlsafe_b64decode(encoded_data_base64)

    # Decompress the data
    data = gzip.decompress(compressed_data)

    # Print the size of the decompressed data
    print(f"Size of decompressed data: {len(data)} bytes")

    # Write the decompressed data to a new file
    with open('decoded_disk.img', 'wb') as f:
        f.write(data)

    # Print the total number of chunks decoded
    print(f"Total number of chunks: {len(file_names)}")

# Decode the QR codes
decode_base64_and_decompress_qr('qrs')
