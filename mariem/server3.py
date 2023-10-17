import os
import threading
from PIL import Image
import socket

# Function to split an image into 3 parts vertically
def split_image(image_path, output_dir):
    img = Image.open(image_path)
    img = img.convert("RGB")
    width, height = img.size
    part_width = width
    part_height = height // 3  # Divide the height into three equal parts

    image_parts = []

    for i in range(3):  # Split into three vertical parts
        upper = i * part_height
        lower = (i + 1) * part_height
        part = img.crop((0, upper, part_width, lower))
        part_path = os.path.join(output_dir, f'part_{i}.png')
        part.save(part_path)
        image_parts.append(part_path)

    return image_parts

# Function to handle a client connection
def handle_client(client_socket, image_part_path):
    with open(image_part_path, 'rb') as image_part_file:
        data = image_part_file.read()
        client_socket.sendall(data)
    client_socket.close()

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to your server's IP address and a port
server_socket.bind(('192.168.88.162', 8085))

# Listen for incoming connections (up to 4 clients)
server_socket.listen(4)

print("Server is listening for incoming connections...")

#get adresses hosts
adress1='192.168.88.230'
adress2='192.168.88.216'
adress3='192.168.88.223'
# List of client IP addresses
client_addresses = [adress1, adress2, adress3]

# Split the image into 3 parts
output_dir = 'parts'  # Directory to save the parts
os.makedirs(output_dir, exist_ok=True)
image_part_paths = split_image('dog.jpg', output_dir)

# Accept connections from up to 3 clients
for i in range(3):
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Create a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, image_part_paths[i]))
    client_thread.start()

# Close the server socket
server_socket.close()
