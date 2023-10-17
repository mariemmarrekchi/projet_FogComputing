from PIL import Image
import os
import socket

# Function to send an image
def send_image(client_socket, image_path):
    with open(image_path, 'rb') as image_file:
        data = image_file.read()
        client_socket.sendall(data)

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a port
server_socket.bind(('192.168.88.230', 8082))  # Listen on all available network interfaces

# Listen for incoming connections
server_socket.listen(1)

print("Server is listening for incoming connection...")

# Accept an incoming connection
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

# Image file path to send
image_path = 'part0.jpg'  # Replace with your image file path

# Send the image to the client
send_image(client_socket, image_path)
print(f"Image sent to {client_address}")

# Close the client socket
client_socket.close()

# Close the server socket
server_socket.close()