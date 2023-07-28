# Refactored script with automatic version selection, 15% error correction, and a dynamic chunk size

import qrcode
import gzip
import base64
import os

# Path to the 'kolibri.img' file
img_file_path = 'kolibri.img'

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # Increased error correction to 15%
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

def compress_and_generate_base64_qr(file_path, chunk_size=376):  # Dynamic chunk size
    # Read the file as binary
    with open(file_path, 'rb') as f:
        data = f.read()

    # Compress the data
    compressed_data = gzip.compress(data)

    # Encode the compressed data as base64
    encoded_data_base64 = base64.urlsafe_b64encode(compressed_data).decode("utf-8")

    # Print the total size of base64 data before splitting
    print(f"Total size of base64 data before splitting: {len(encoded_data_base64)}")

    # Split the encoded_data_base64 into chunks
    chunks = [encoded_data_base64[i:i+chunk_size] for i in range(0, len(encoded_data_base64), chunk_size)]

    for i, chunk in enumerate(chunks):
        # Print the size of each chunk
        print(f"Size of chunk {i}: {len(chunk)}")

        # Generate a QR code from each chunk
        file_name = f"qrs/qr_{i:09d}.png"  # Updated file name schema
        generate_qr_code(chunk, file_name)

# Generate the QR codes
compress_and_generate_base64_qr(img_file_path)
