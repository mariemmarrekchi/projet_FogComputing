import socket
import os

# Function to receive an image part and save it
def receive_image_part(client_socket, part_name):
    with open(part_name, 'wb') as part_file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            part_file.write(data)

# Create a TCP socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server (replace 'server_ip_here' with the server's IP address)
server_address = ('192.168.88.162', 8085)
client_socket.connect(server_address)

# Create a directory to save received image parts
output_dir = 'received_parts'
os.makedirs(output_dir, exist_ok=True)

# Receive and save image parts from the server
part_name = "part0.png"
receive_image_part(client_socket, os.path.join(output_dir, part_name))
print(f"Received and saved {part_name}")

# Close the client socket
client_socket.close()
