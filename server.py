import socket
import os
from pathlib import Path

# This function is structured to handle large files efficiently:
# 1. It receives the filename and file size separately before the actual data.
# 2. It uses a loop to receive data in chunks, which is memory-efficient for large files.
# 3. It keeps track of remaining data to ensure the entire file is received
def receive_file(conn, save_path):
    # First, receive the filename
    filename = conn.recv(1024).decode().strip()
    print(f"Receiving file: {filename}")

    # Construct the full file path
    full_path = os.path.join(save_path, filename)

    # Receive the file size
    file_size = int(conn.recv(1024).decode())

    # Receive the file data
    with open(full_path, 'wb') as file:
        remaining = file_size
        while remaining:
            data = conn.recv(min(1024, remaining))
            file.write(data)
            remaining -= len(data)

    print(f"File received and saved as: {full_path}")

if __name__ == '__main__':
    # Defining Socket
    host = '127.0.0.1'
    port = 8080

    # Specify the directory to save received files
    # Save in the user's Documents directory
    save_directory = str(Path.home() / "Documents" / "received_files")
    os.makedirs(save_directory, exist_ok=True)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)  # Only listen for a single connection

    print('Server is running. Waiting for a client to connect...')

    while True:
        conn, addr = sock.accept()
        print(f'Connected with client: {addr}')

        receive_file(conn, save_directory)

        # Closing the Connection
        conn.close()
        print("Connection closed. ")
